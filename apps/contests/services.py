from django.db.models import Count, Max, Q
from django.utils import timezone

from apps.dashboard.leaderboard import DIFFICULTY_POINTS
from apps.exercises.models import Exercise, ExerciseAttempt

from .models import Contest, ContestExercise, ContestScore


def exercise_points(exercise: Exercise, override: int = 0) -> int:
    if override:
        return override
    return DIFFICULTY_POINTS.get(exercise.difficulty, 1)


def refresh_contest_score(contest: Contest, student) -> ContestScore:
    links = list(ContestExercise.objects.filter(contest=contest).select_related("exercise"))
    exercise_ids = [link.exercise_id for link in links]
    solved = set(
        ExerciseAttempt.objects.filter(
            student=student,
            exercise_id__in=exercise_ids,
            is_correct=True,
            created_at__gte=contest.starts_at,
            created_at__lte=contest.ends_at,
        ).values_list("exercise_id", flat=True)
    )
    points = 0
    last_at = None
    for link in links:
        if link.exercise_id in solved:
            points += exercise_points(link.exercise, link.points)
    if solved:
        last_at = (
            ExerciseAttempt.objects.filter(
                student=student,
                exercise_id__in=solved,
                is_correct=True,
                created_at__gte=contest.starts_at,
                created_at__lte=contest.ends_at,
            )
            .order_by("-created_at")
            .values_list("created_at", flat=True)
            .first()
        )
    score, _ = ContestScore.objects.update_or_create(
        contest=contest,
        student=student,
        defaults={
            "points": points,
            "solved_count": len(solved),
            "last_solved_at": last_at,
        },
    )
    return score


def contest_leaderboard(contest: Contest, limit: int = 50) -> list[dict]:
    rows = list(
        ContestScore.objects.filter(contest=contest, points__gt=0)
        .select_related("student")
        .order_by("-points", "last_solved_at", "id")[:limit]
    )
    board = []
    for index, row in enumerate(rows, start=1):
        name = row.student.get_full_name().strip() or row.student.email
        board.append(
            {
                "rank": index,
                "student_id": row.student_id,
                "name": name,
                "points": row.points,
                "solved_count": row.solved_count,
                "last_solved_at": row.last_solved_at,
            }
        )
    return board


def active_contests():
    now = timezone.now()
    return Contest.objects.filter(is_published=True, starts_at__lte=now, ends_at__gte=now).prefetch_related(
        "exercises"
    )


def upcoming_or_recent_contests(limit: int = 5):
    return Contest.objects.filter(is_published=True).order_by("-starts_at")[:limit]


def sync_student_contests_on_solve(student, exercise: Exercise):
    now = timezone.now()
    contests = Contest.objects.filter(
        is_published=True,
        starts_at__lte=now,
        ends_at__gte=now,
        exercises=exercise,
    )
    for contest in contests:
        refresh_contest_score(contest, student)
