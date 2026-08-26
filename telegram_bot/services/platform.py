from __future__ import annotations

from asgiref.sync import sync_to_async
from django.core.files.base import ContentFile
from django.utils import timezone

from apps.access.services import access_service
from apps.accounts.models import Announcement, DirectMessage, SupportTicket, TelegramAccount, User
from apps.analytics.services import dashboard_overview, student_rows, teacher_students
from apps.courses.models import Course, Lecture, Module
from apps.exercises.models import Exercise, ExerciseAttempt
from apps.exercises.services import RateLimited, exercise_service
from apps.homework.models import HomeworkAssignment, HomeworkSubmission
from apps.homework.services import homework_service
from apps.progress.models import LectureProgress
from apps.progress.services import progress_service


@sync_to_async
def list_courses(user: User) -> list[dict]:
    rows = []
    for course in Course.objects.all().order_by("order", "id"):
        decision = access_service.evaluate(user, course)
        stats = progress_service.course_stats(user, course) if decision.allowed and user.is_student else None
        rows.append(
            {
                "id": course.pk,
                "title": course.title,
                "description": course.description[:400],
                "allowed": decision.allowed,
                "reason": decision.reason,
                "published": course.is_published and course.is_visible,
                "percent": (stats or {}).get("percent", 0),
            }
        )
    return rows


@sync_to_async
def course_modules(user: User, course_id: int) -> tuple[str, list[dict]]:
    course = Course.objects.filter(pk=course_id).first()
    if not course:
        return "not_found", []
    decision = access_service.evaluate(user, course)
    if not decision.allowed:
        return decision.reason, []
    modules = []
    for module in course.modules.all():
        md = access_service.evaluate(user, module)
        modules.append(
            {
                "id": module.pk,
                "title": module.title,
                "allowed": md.allowed,
                "published": module.is_published,
                "percent": progress_service.module_percent(user, module) if md.allowed and user.is_student else 0,
            }
        )
    return course.title, modules


@sync_to_async
def module_items(user: User, module_id: int) -> tuple[str, list[dict], list[dict]]:
    module = Module.objects.filter(pk=module_id).select_related("course").first()
    if not module:
        return "not_found", [], []
    decision = access_service.evaluate(user, module)
    if not decision.allowed:
        return decision.reason, [], []
    lectures = []
    completed = set(
        LectureProgress.objects.filter(student=user, completed=True, lecture__module=module).values_list(
            "lecture_id", flat=True
        )
    )
    for lecture in module.lectures.all():
        ld = access_service.evaluate(user, lecture)
        practice = lecture.practice_exercises.filter(is_published=True).first()
        lectures.append(
            {
                "id": lecture.pk,
                "title": lecture.title,
                "allowed": ld.allowed,
                "completed": lecture.pk in completed,
                "practice_id": practice.pk if practice else None,
                "has_hw": hasattr(lecture, "homework_assignment") and bool(getattr(lecture, "homework_assignment", None)),
            }
        )
    extras = []
    for ex in module.exercises.filter(is_published=True, lecture__isnull=True):
        extras.append(
            {
                "id": ex.pk,
                "title": ex.title,
                "allowed": access_service.can_access(user, ex),
            }
        )
    return module.title, lectures, extras


@sync_to_async
def lecture_payload(user: User, lecture_id: int) -> dict | None:
    lecture = Lecture.objects.select_related("module", "module__course").filter(pk=lecture_id).first()
    if not lecture:
        return None
    decision = access_service.evaluate(user, lecture)
    if not decision.allowed:
        return {"error": decision.reason}
    progress_service.touch_lecture(user, lecture)
    user.mark_activity()
    progress = LectureProgress.objects.filter(student=user, lecture=lecture).first()
    practice = lecture.practice_exercises.filter(is_published=True).first()
    homework = getattr(lecture, "homework_assignment", None)
    return {
        "id": lecture.pk,
        "title": lecture.title,
        "course": lecture.course.title,
        "module": lecture.module.title,
        "content": lecture.content,
        "sql_examples": lecture.sql_examples or [],
        "completed": bool(progress and progress.completed),
        "practice_id": practice.pk if practice else None,
        "practice_title": practice.title if practice else None,
        "homework_id": homework.pk if homework else None,
        "homework_title": homework.title if homework else None,
        "next_id": (
            lecture.get_next().pk
            if lecture.get_next() and access_service.can_access(user, lecture.get_next())
            else None
        ),
    }


@sync_to_async
def complete_lecture(user: User, lecture_id: int) -> str:
    lecture = Lecture.objects.select_related("module", "module__course").filter(pk=lecture_id).first()
    if not lecture:
        return "not_found"
    if not access_service.can_access(user, lecture):
        return "forbidden"
    progress_service.complete_lecture(user, lecture)
    user.mark_activity()
    return "ok"


@sync_to_async
def exercise_payload(user: User, exercise_id: int) -> dict | None:
    exercise = Exercise.objects.select_related("module", "module__course", "lecture").filter(pk=exercise_id).first()
    if not exercise or not exercise.is_published:
        return None
    if not access_service.can_access(user, exercise):
        return {"error": "Bu mashq hozircha yopiq."}
    datasets = list(exercise.datasets.all())
    latest = ExerciseAttempt.objects.filter(student=user, exercise=exercise).first()
    return {
        "id": exercise.pk,
        "title": exercise.title,
        "description": exercise.description,
        "task": exercise.task,
        "hints": exercise.hints or [],
        "lecture_id": exercise.lecture_id,
        "solved": bool(latest and latest.is_correct),
        "last_score": latest.score if latest else None,
        "tables": [d.name for d in datasets],
        "previews": [{"name": d.name, "preview": d.preview} for d in datasets],
    }


@sync_to_async
def run_sql(user: User, exercise_id: int, sql: str) -> dict:
    exercise = Exercise.objects.select_related("expected_result", "module").filter(pk=exercise_id).first()
    if not exercise:
        return {"ok": False, "message": "Mashq topilmadi."}
    if not access_service.can_access(user, exercise):
        return {"ok": False, "message": "Ruxsat yo‘q."}
    try:
        attempt = exercise_service.run(user, exercise, sql)
    except RateLimited as exc:
        return {"ok": False, "message": exc.message}
    user.mark_activity()
    preview = attempt.result_preview or {}
    rows = preview.get("rows") or []
    cols = preview.get("columns") or []
    table = ""
    if cols:
        table = " | ".join(str(c) for c in cols) + "\n"
        for row in rows[:8]:
            table += " | ".join(str(c) for c in row) + "\n"
    return {
        "ok": True,
        "correct": attempt.is_correct,
        "score": attempt.score,
        "message": attempt.error_message or preview.get("message") or "",
        "table": table.strip(),
    }


@sync_to_async
def student_progress(user: User) -> list[dict]:
    rows = []
    for course in Course.objects.filter(is_published=True, is_visible=True):
        if not access_service.can_access(user, course):
            continue
        stats = progress_service.course_stats(user, course)
        last = progress_service.last_position(user, course)
        rows.append({"title": course.title, "stats": stats, "last": str(last) if last else "—"})
    return rows


@sync_to_async
def student_scores(user: User) -> list[dict]:
    attempts = (
        ExerciseAttempt.objects.filter(student=user, is_correct=True)
        .select_related("exercise")
        .order_by("-created_at")[:15]
    )
    seen = set()
    rows = []
    for item in attempts:
        if item.exercise_id in seen:
            continue
        seen.add(item.exercise_id)
        rows.append({"title": item.exercise.title, "score": item.score})
    return rows


@sync_to_async
def homework_list(user: User) -> list[dict]:
    rows = []
    for assignment in HomeworkAssignment.objects.filter(is_published=True).select_related("lecture"):
        if not access_service.can_access(user, assignment.lecture):
            continue
        latest = homework_service.latest_for_student(user, assignment)
        rows.append(
            {
                "id": assignment.pk,
                "title": assignment.title,
                "status": latest.status if latest else "yuborilmagan",
                "instructions": assignment.instructions[:500],
            }
        )
    return rows


@sync_to_async
def submit_homework_bytes(user: User, assignment_id: int, filename: str, content: bytes) -> str:
    assignment = HomeworkAssignment.objects.filter(pk=assignment_id).select_related("lecture").first()
    if not assignment:
        return "not_found"
    if not access_service.can_access(user, assignment.lecture):
        return "forbidden"
    if not filename.lower().endswith(".txt"):
        return "bad_type"
    upload = ContentFile(content, name=filename)
    upload.content_type = "text/plain"
    try:
        homework_service.submit(user, assignment, upload)
    except Exception as exc:
        return f"error:{exc}"
    user.mark_activity()
    return "ok"


@sync_to_async
def announcements(limit: int = 8) -> list[dict]:
    qs = Announcement.objects.filter(is_published=True).select_related("author")[:limit]
    return [{"title": a.title, "body": a.body, "author": str(a.author), "at": a.created_at} for a in qs]


@sync_to_async
def inbox(user: User) -> list[dict]:
    qs = DirectMessage.objects.filter(recipient=user).select_related("sender")[:10]
    rows = []
    for msg in qs:
        if msg.read_at is None:
            msg.read_at = timezone.now()
            msg.save(update_fields=["read_at"])
        rows.append({"from": str(msg.sender), "body": msg.body, "at": msg.created_at})
    return rows


@sync_to_async
def create_support(user: User, message: str) -> int:
    ticket = SupportTicket.objects.create(user=user, message=message)
    return ticket.pk


@sync_to_async
def teacher_overview(user: User) -> dict:
    return dashboard_overview(user)


@sync_to_async
def teacher_student_list(user: User) -> list[dict]:
    rows = student_rows(user, {})[:20]
    out = []
    for row in rows:
        st = row["student"]
        stats = row.get("stats") or {}
        out.append(
            {
                "id": st.pk,
                "name": str(st),
                "email": st.email,
                "percent": stats.get("percent", 0),
                "score": stats.get("average_score", 0),
                "hw": row.get("homework_status"),
            }
        )
    return out


@sync_to_async
def pending_homework(user: User) -> list[dict]:
    students = teacher_students(user)
    qs = HomeworkSubmission.objects.filter(
        student__in=students,
        status__in=["submitted", "under_review"],
    ).select_related("student", "assignment")[:15]
    return [
        {
            "id": s.pk,
            "student": str(s.student),
            "title": s.assignment.title,
            "file": s.original_filename,
        }
        for s in qs
    ]


@sync_to_async
def review_homework(user: User, submission_id: int, score: int, feedback: str) -> str:
    submission = HomeworkSubmission.objects.select_related("assignment").filter(pk=submission_id).first()
    if not submission:
        return "not_found"
    if not (user.is_teacher or user.is_admin):
        return "forbidden"
    try:
        homework_service.review(user, submission, score, feedback, "reviewed")
    except Exception as exc:
        return f"error:{exc}"
    return "ok"


@sync_to_async
def send_direct(sender: User, student_id: int, body: str) -> tuple[str, int | None]:
    student = User.objects.filter(pk=student_id, role=User.Role.STUDENT).first()
    if not student:
        return "not_found", None
    DirectMessage.objects.create(sender=sender, recipient=student, body=body)
    acc = TelegramAccount.objects.filter(user=student, notify_enabled=True).first()
    return "ok", acc.telegram_id if acc else None


@sync_to_async
def publish_announcement(author: User, title: str, body: str) -> list[int]:
    Announcement.objects.create(author=author, title=title, body=body, is_published=True)
    ids = list(
        TelegramAccount.objects.filter(notify_enabled=True).values_list("telegram_id", flat=True)
    )
    return ids


@sync_to_async
def telegram_ids_for_users(user_ids: list[int]) -> list[int]:
    return list(
        TelegramAccount.objects.filter(user_id__in=user_ids, notify_enabled=True).values_list("telegram_id", flat=True)
    )
