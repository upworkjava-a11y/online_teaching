from datetime import timedelta

from django.db.models import Avg, Count, Max, Q
from django.utils import timezone

from apps.accounts.models import User
from apps.courses.models import Course, CourseEnrollment
from apps.exercises.models import Exercise, ExerciseAttempt
from apps.homework.models import HomeworkSubmission
from apps.progress.models import LectureProgress
from apps.progress.services import progress_service


def teacher_courses(user):
    if user.is_admin:
        return Course.objects.all()
    profile = getattr(user, "teacher_profile", None)
    if not profile:
        return Course.objects.none()
    return profile.assigned_courses.all()


def teacher_students(user, course=None):
    courses = teacher_courses(user)
    if course:
        courses = courses.filter(pk=course.pk)
    student_ids = CourseEnrollment.objects.filter(course__in=courses).values_list("student_id", flat=True)
    return User.objects.filter(pk__in=student_ids, role=User.Role.STUDENT)


def student_belongs_to_teacher(teacher, student) -> bool:
    return teacher_students(teacher).filter(pk=student.pk).exists()


def dashboard_overview(user) -> dict:
    students = teacher_students(user)
    now = timezone.now()
    active = students.filter(last_activity_at__gte=now - timedelta(days=7)).count()
    inactive = students.filter(Q(last_activity_at__lt=now - timedelta(days=7)) | Q(last_activity_at__isnull=True)).count()
    currently_learning = students.filter(last_activity_at__gte=now - timedelta(minutes=30)).count()
    courses = teacher_courses(user)
    completed_lectures = LectureProgress.objects.filter(student__in=students, completed=True, lecture__module__course__in=courses).count()
    completed_exercises = (
        ExerciseAttempt.objects.filter(student__in=students, is_correct=True, exercise__module__course__in=courses)
        .values("student", "exercise")
        .distinct()
        .count()
    )
    avg_score = (
        ExerciseAttempt.objects.filter(student__in=students, exercise__module__course__in=courses)
        .values("student", "exercise")
        .annotate(best=Max("score"))
        .aggregate(avg=Avg("best"))
        .get("avg")
        or 0
    )
    pending = HomeworkSubmission.objects.filter(
        student__in=students,
        assignment__lecture__module__course__in=courses,
        status__in=["submitted", "under_review"],
    ).count()
    hw_avg = (
        HomeworkSubmission.objects.filter(
            student__in=students,
            assignment__lecture__module__course__in=courses,
            reviews__isnull=False,
        )
        .annotate(latest_score=Max("reviews__score"))
        .aggregate(avg=Avg("latest_score"))
        .get("avg")
        or 0
    )
    return {
        "total_students": students.count(),
        "active_students": active,
        "inactive_students": inactive,
        "currently_learning": currently_learning,
        "completed_lectures": completed_lectures,
        "completed_exercises": completed_exercises,
        "average_score": round(avg_score or 0, 1),
        "pending_reviews": pending,
        "average_homework_score": round(hw_avg or 0, 1),
    }


def student_rows(user, filters: dict):
    qs = teacher_students(user)
    course = filters.get("course")
    if course:
        qs = qs.filter(enrollments__course=course)
    if filters.get("active") == "active":
        qs = qs.filter(last_activity_at__gte=timezone.now() - timedelta(days=7))
    elif filters.get("active") == "inactive":
        qs = qs.filter(Q(last_activity_at__lt=timezone.now() - timedelta(days=7)) | Q(last_activity_at__isnull=True))
    qs = qs.distinct().order_by("first_name", "last_name")
    rows = []
    for student in qs:
        target_course = course or teacher_courses(user).filter(is_published=True).first()
        stats = progress_service.course_stats(student, target_course) if target_course else {}
        if filters.get("progress_min") and stats.get("percent", 0) < int(filters["progress_min"]):
            continue
        if filters.get("progress_max") and stats.get("percent", 0) > int(filters["progress_max"]):
            continue
        if filters.get("score_min") and stats.get("average_score", 0) < float(filters["score_min"]):
            continue
        if filters.get("score_max") and stats.get("average_score", 0) > float(filters["score_max"]):
            continue
        last_progress = student.course_progress.select_related("last_lecture__module").order_by("-last_activity_at").first()
        latest_hw = student.homework_submissions.order_by("-created_at").first()
        rows.append(
            {
                "student": student,
                "stats": stats,
                "course": target_course,
                "current_module": last_progress.last_lecture.module if last_progress and last_progress.last_lecture else None,
                "homework_status": latest_hw.status if latest_hw else "not_submitted",
            }
        )
    return rows


def progress_distribution(user) -> dict:
    rows = student_rows(user, {})
    buckets = {"0-25": 0, "26-50": 0, "51-75": 0, "76-100": 0}
    for row in rows:
        percent = (row.get("stats") or {}).get("percent") or 0
        if percent <= 25:
            buckets["0-25"] += 1
        elif percent <= 50:
            buckets["26-50"] += 1
        elif percent <= 75:
            buckets["51-75"] += 1
        else:
            buckets["76-100"] += 1
    return buckets


def module_progress_series(user) -> dict:
    course = teacher_courses(user).filter(is_published=True).first()
    students = list(teacher_students(user, course))
    if not course:
        return {"labels": [], "values": []}
    labels = []
    values = []
    for module in course.modules.filter(is_published=True):
        percents = [progress_service.module_percent(student, module) for student in students] or [0]
        labels.append(module.title)
        values.append(round(sum(percents) / len(percents), 1))
    return {"labels": labels, "values": values}


def activity_series(user, days: int = 14) -> dict:
    from datetime import date, datetime, time

    students = teacher_students(user)
    courses = teacher_courses(user)
    labels = []
    lectures = []
    exercises = []
    today = timezone.localdate()
    for offset in range(days - 1, -1, -1):
        day = today - timedelta(days=offset)
        labels.append(day.strftime("%d.%m"))
        lectures.append(
            LectureProgress.objects.filter(
                student__in=students,
                completed=True,
                completed_at__date=day,
                lecture__module__course__in=courses,
            ).count()
        )
        exercises.append(
            ExerciseAttempt.objects.filter(
                student__in=students,
                created_at__date=day,
                exercise__module__course__in=courses,
            ).count()
        )
    return {"labels": labels, "lectures": lectures, "exercises": exercises}


def homework_status_series(user) -> dict:
    students = teacher_students(user)
    courses = teacher_courses(user)
    qs = HomeworkSubmission.objects.filter(student__in=students, assignment__lecture__module__course__in=courses)
    return {
        "labels": ["Yuborilgan", "Tekshirilgan", "Qayta topshirish"],
        "values": [
            qs.filter(status__in=["submitted", "under_review"]).count(),
            qs.filter(status="reviewed").count(),
            qs.filter(status="needs_revision").count(),
        ],
    }


def score_series(user) -> dict:
    rows = student_rows(user, {})
    labels = [str(row["student"]) for row in rows[:12]]
    progress = [(row.get("stats") or {}).get("percent") or 0 for row in rows[:12]]
    scores = [(row.get("stats") or {}).get("average_score") or 0 for row in rows[:12]]
    return {"labels": labels, "progress": progress, "scores": scores}


def difficult_exercises(user):
    courses = teacher_courses(user)
    return (
        Exercise.objects.filter(module__course__in=courses, is_published=True)
        .annotate(
            attempts_count=Count("attempts"),
            correct_count=Count("attempts", filter=Q(attempts__is_correct=True)),
        )
        .order_by("correct_count", "-attempts_count")[:8]
    )
