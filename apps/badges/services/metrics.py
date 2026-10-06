"""Compute raw metrics used by badge progress evaluators."""

from __future__ import annotations

from datetime import datetime, time, timedelta

from django.conf import settings
from django.utils import timezone

from apps.badges.topics import (
    SQL_TOPIC_LABELS,
    is_python_exercise,
    topic_for_exercise,
)
from apps.courses.models import Course
from apps.exercises.models import Exercise, ExerciseAttempt
from apps.progress.models import LectureProgress, StudentStreak
from apps.social.models import UserActivity


def _solved_qs(user):
    return ExerciseAttempt.objects.filter(
        student=user,
        is_correct=True,
        exercise__is_published=True,
        exercise__is_skill_test=False,
    )


def problems_solved(user) -> int:
    return _solved_qs(user).values("exercise_id").distinct().count()


def difficulty_solved(user, difficulty: str) -> int:
    return (
        _solved_qs(user)
        .filter(exercise__difficulty=difficulty)
        .values("exercise_id")
        .distinct()
        .count()
    )


def course_solves(user, course_slug: str, *, include_skill_tests: bool = False) -> int:
    qs = ExerciseAttempt.objects.filter(
        student=user,
        is_correct=True,
        exercise__is_published=True,
        exercise__module__course__slug=course_slug,
    )
    if not include_skill_tests:
        qs = qs.filter(exercise__is_skill_test=False)
    return qs.values("exercise_id").distinct().count()


def courses_active(user, *, min_solves: int = 5, include_skill_tests: bool = True) -> int:
    """Count courses where the user has at least min_solves distinct correct answers."""
    from django.db.models import Count

    qs = ExerciseAttempt.objects.filter(
        student=user,
        is_correct=True,
        exercise__is_published=True,
        exercise__module__course__is_published=True,
    )
    if not include_skill_tests:
        qs = qs.filter(exercise__is_skill_test=False)
    rows = (
        qs.values("exercise__module__course_id")
        .annotate(n=Count("exercise_id", distinct=True))
        .filter(n__gte=min_solves)
    )
    return rows.count()


def solved_exercise_ids(user) -> set[int]:
    return set(_solved_qs(user).values_list("exercise_id", flat=True).distinct())


def topic_problem_counts(user) -> dict[str, int]:
    ids = solved_exercise_ids(user)
    if not ids:
        return {}
    exercises = Exercise.objects.filter(pk__in=ids).select_related("module", "module__course")
    counts: dict[str, int] = {}
    for ex in exercises:
        topic = topic_for_exercise(ex)
        if topic:
            counts[topic] = counts.get(topic, 0) + 1
        if is_python_exercise(ex):
            counts["python_any"] = counts.get("python_any", 0) + 1
    return counts


def distinct_sql_topics(user) -> int:
    counts = topic_problem_counts(user)
    return sum(1 for t in SQL_TOPIC_LABELS if counts.get(t, 0) > 0)


def current_streak(user) -> int:
    streak = StudentStreak.objects.filter(student=user).first()
    return int(streak.current_streak) if streak else 0


def longest_streak(user) -> int:
    streak = StudentStreak.objects.filter(student=user).first()
    if not streak:
        return 0
    return max(int(streak.current_streak or 0), int(streak.longest_streak or 0))


def lessons_completed(user) -> int:
    return LectureProgress.objects.filter(student=user, completed=True).count()


def courses_fully_completed(user) -> int:
    completed = 0
    courses = Course.objects.filter(is_published=True).prefetch_related("modules__lectures")
    done_ids = set(
        LectureProgress.objects.filter(student=user, completed=True).values_list("lecture_id", flat=True)
    )
    for course in courses:
        lecture_ids = [
            lec.pk
            for mod in course.modules.all()
            if mod.is_published
            for lec in mod.lectures.all()
            if lec.is_published
        ]
        if lecture_ids and all(lid in done_ids for lid in lecture_ids):
            completed += 1
    return completed


def night_window() -> tuple[time, time]:
    start_h = int(getattr(settings, "BADGE_NIGHT_START_HOUR", 21))
    end_h = int(getattr(settings, "BADGE_NIGHT_END_HOUR", 2))
    return time(start_h % 24, 0), time(end_h % 24, 0)


def in_night_window(dt: datetime) -> bool:
    local = timezone.localtime(dt)
    start, end = night_window()
    t = local.time()
    if start <= end:
        return start <= t < end
    return t >= start or t < end


def night_activity_count(user) -> int:
    count = 0
    for ts in (
        ExerciseAttempt.objects.filter(student=user, is_correct=True, exercise__is_skill_test=False)
        .values_list("created_at", flat=True)
        .iterator(chunk_size=500)
    ):
        if in_night_window(ts):
            count += 1
    for ts in (
        LectureProgress.objects.filter(student=user, completed=True, completed_at__isnull=False)
        .values_list("completed_at", flat=True)
        .iterator(chunk_size=500)
    ):
        if in_night_window(ts):
            count += 1
    return count


def _activity_dates(user) -> set:
    dates = set(UserActivity.objects.filter(user=user, count__gt=0).values_list("date", flat=True))
    for ts in LectureProgress.objects.filter(
        student=user, completed=True, completed_at__isnull=False
    ).values_list("completed_at", flat=True)[:2000]:
        dates.add(timezone.localtime(ts).date())
    for ts in (
        ExerciseAttempt.objects.filter(student=user, is_correct=True, exercise__is_skill_test=False)
        .values_list("created_at", flat=True)[:5000]
    ):
        dates.add(timezone.localtime(ts).date())
    return dates


def perfect_week_progress(user) -> int:
    dates = _activity_dates(user)
    best = 0
    seen_mondays: set = set()
    for d in dates:
        monday = d - timedelta(days=d.weekday())
        if monday in seen_mondays:
            continue
        seen_mondays.add(monday)
        week = {monday + timedelta(days=i) for i in range(7)}
        best = max(best, len(week & dates))
    return best


def has_perfect_week(user) -> bool:
    return perfect_week_progress(user) >= 7
