"""Helpers for the unified profile page."""

from __future__ import annotations

from apps.access.services import OPEN_COURSE_SLUGS
from apps.courses.models import Course
from apps.exercises.models import ExerciseAttempt
from apps.progress.models import LectureProgress
from apps.progress.services import progress_service
from apps.social.models import SocialProfile
from apps.social.services.avatar import get_or_create_profile, resolve_avatar_url


def profile_bio(user) -> str:
    sp = getattr(user, "social_profile", None)
    if sp is None:
        sp = SocialProfile.objects.filter(user=user).first()
    if sp and sp.bio:
        return sp.bio
    student = getattr(user, "student_profile", None)
    if student and student.bio:
        return student.bio
    return ""


def course_progress_rows(user) -> list[dict]:
    courses = Course.objects.filter(
        is_published=True,
        is_visible=True,
        slug__in=OPEN_COURSE_SLUGS,
    ).order_by("order")
    rows = []
    for course in courses:
        stats = progress_service.course_stats(user, course)
        rows.append({"course": course, "stats": stats, "percent": stats.get("percent") or 0})
    return rows


def recent_learning_items(user, limit: int = 8) -> list[dict]:
    items: list[dict] = []
    attempts = (
        ExerciseAttempt.objects.filter(student=user, is_correct=True, exercise__is_published=True)
        .select_related("exercise", "exercise__module", "exercise__module__course")
        .order_by("-created_at")[:limit]
    )
    for a in attempts:
        course_title = a.exercise.module.course.title
        items.append(
            {
                "kind": "exercise",
                "title": a.exercise.title,
                "course": course_title,
                "at": a.created_at,
                "label": f"Yechildi: {a.exercise.title}",
            }
        )
    lectures = (
        LectureProgress.objects.filter(student=user, completed=True, completed_at__isnull=False)
        .select_related("lecture", "lecture__module", "lecture__module__course")
        .order_by("-completed_at")[:limit]
    )
    for lp in lectures:
        items.append(
            {
                "kind": "lesson",
                "title": lp.lecture.title,
                "course": lp.lecture.module.course.title,
                "at": lp.completed_at,
                "label": f"Dars tugallandi: {lp.lecture.title}",
            }
        )
    items.sort(key=lambda x: x["at"], reverse=True)
    return items[:limit]


def ensure_profile(user):
    get_or_create_profile(user)
    return resolve_avatar_url(user)
