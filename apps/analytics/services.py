from datetime import timedelta

from django.db.models import Avg, Count, Max, Q
from django.utils import timezone

from apps.accounts.models import User
from apps.courses.models import Course, CourseEnrollment, Module
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


def skill_test_overview(user, course=None, module=None) -> list[dict]:
    """Talaba × modul bo‘yicha bilim testi xulosasi."""
    courses = teacher_courses(user)
    if course:
        courses = courses.filter(pk=course.pk)
    modules_qs = Module.objects.filter(course__in=courses, is_published=True).order_by("course__order", "order")
    if module:
        modules_qs = modules_qs.filter(pk=module.pk)
    modules = list(modules_qs.select_related("course"))
    students = list(teacher_students(user, course=course).order_by("first_name", "last_name"))
    if not modules or not students:
        return []

    tests_by_module: dict[int, list[int]] = {}
    all_test_ids = []
    for mod in modules:
        ids = list(
            Exercise.objects.filter(module=mod, is_published=True, is_skill_test=True).values_list("id", flat=True)
        )
        tests_by_module[mod.pk] = ids
        all_test_ids.extend(ids)

    correct_pairs = set(
        ExerciseAttempt.objects.filter(
            student_id__in=[s.pk for s in students],
            exercise_id__in=all_test_ids,
            is_correct=True,
        ).values_list("student_id", "exercise_id")
    )
    last_by_pair = {}
    for row in (
        ExerciseAttempt.objects.filter(
            student_id__in=[s.pk for s in students],
            exercise_id__in=all_test_ids,
        )
        .values("student_id", "exercise__module_id")
        .annotate(last_at=Max("created_at"))
    ):
        last_by_pair[(row["student_id"], row["exercise__module_id"])] = row["last_at"]

    rows = []
    for student in students:
        for mod in modules:
            test_ids = tests_by_module.get(mod.pk) or []
            total = len(test_ids)
            if total == 0:
                continue
            done = sum(1 for eid in test_ids if (student.pk, eid) in correct_pairs)
            percent = round((done / total) * 100) if total else 0
            rows.append(
                {
                    "student": student,
                    "module": mod,
                    "course": mod.course,
                    "done": done,
                    "total": total,
                    "percent": percent,
                    "remaining": total - done,
                    "last_at": last_by_pair.get((student.pk, mod.pk)),
                    "status": (
                        "tugallangan"
                        if done >= total
                        else ("boshlangan" if done > 0 else "boshlanmagan")
                    ),
                }
            )
    rows.sort(key=lambda r: (-r["percent"], r["student"].first_name, r["module"].order))
    return rows


def student_skill_test_detail(student, course) -> list[dict]:
    """Bitta talaba uchun modulma-modul batafsil bilim testi."""
    if not course:
        return []
    modules = list(course.modules.filter(is_published=True).order_by("order"))
    result = []
    for mod in modules:
        tests = list(
            Exercise.objects.filter(module=mod, is_published=True, is_skill_test=True)
            .select_related("expected_result")
            .order_by("order", "id")
        )
        if not tests:
            continue
        test_ids = [t.pk for t in tests]
        latest_attempts = {}
        attempt_counts = {
            row["exercise_id"]: row["c"]
            for row in ExerciseAttempt.objects.filter(student=student, exercise_id__in=test_ids)
            .values("exercise_id")
            .annotate(c=Count("id"))
        }
        for attempt in (
            ExerciseAttempt.objects.filter(student=student, exercise_id__in=test_ids)
            .order_by("exercise_id", "-created_at")
        ):
            if attempt.exercise_id not in latest_attempts:
                latest_attempts[attempt.exercise_id] = attempt
        correct_ids = set(
            ExerciseAttempt.objects.filter(
                student=student, exercise_id__in=test_ids, is_correct=True
            ).values_list("exercise_id", flat=True)
        )
        questions = []
        for test in tests:
            latest = latest_attempts.get(test.pk)
            expected = ""
            er = getattr(test, "expected_result", None)
            if er and er.rows and er.rows[0]:
                expected = str(er.rows[0][0])
            questions.append(
                {
                    "exercise": test,
                    "solved": test.pk in correct_ids,
                    "latest": latest,
                    "answer": latest.sql_query if latest else "",
                    "expected": expected,
                    "attempts_count": attempt_counts.get(test.pk, 0),
                }
            )
        done = sum(1 for q in questions if q["solved"])
        total = len(questions)
        result.append(
            {
                "module": mod,
                "done": done,
                "total": total,
                "percent": round((done / total) * 100) if total else 0,
                "questions": questions,
            }
        )
    return result
