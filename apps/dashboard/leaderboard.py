"""
Reyting — to‘g‘ri yechilgan masalalar bo‘yicha.

Ball: Easy=1, Medium=2, Hard=3 (har bir mashq bir marta hisoblanadi).
"""

from django.db.models import Count, Max, Q
from django.utils import timezone

from apps.accounts.models import User
from apps.exercises.models import Exercise, ExerciseAttempt

DIFFICULTY_POINTS = {
    Exercise.Difficulty.EASY: 1,
    Exercise.Difficulty.MEDIUM: 2,
    Exercise.Difficulty.HARD: 3,
}

DIFFICULTY_LABELS = {
    "easy": "Oson",
    "medium": "O‘rta",
    "hard": "Qiyin",
}


def build_leaderboard(limit: int = 50) -> list[dict]:
    rows = (
        ExerciseAttempt.objects.filter(
            is_correct=True,
            student__role=User.Role.STUDENT,
            student__is_active=True,
            exercise__is_published=True,
        )
        .values(
            "student_id",
            "student__first_name",
            "student__last_name",
            "student__email",
        )
        .annotate(
            easy_count=Count(
                "exercise",
                filter=Q(exercise__difficulty=Exercise.Difficulty.EASY),
                distinct=True,
            ),
            medium_count=Count(
                "exercise",
                filter=Q(exercise__difficulty=Exercise.Difficulty.MEDIUM),
                distinct=True,
            ),
            hard_count=Count(
                "exercise",
                filter=Q(exercise__difficulty=Exercise.Difficulty.HARD),
                distinct=True,
            ),
            solved_count=Count("exercise", distinct=True),
            last_solved_at=Max("created_at"),
        )
    )

    board = []
    for row in rows:
        easy = row["easy_count"] or 0
        medium = row["medium_count"] or 0
        hard = row["hard_count"] or 0
        points = (
            easy * DIFFICULTY_POINTS[Exercise.Difficulty.EASY]
            + medium * DIFFICULTY_POINTS[Exercise.Difficulty.MEDIUM]
            + hard * DIFFICULTY_POINTS[Exercise.Difficulty.HARD]
        )
        name = f"{row['student__first_name']} {row['student__last_name']}".strip()
        if not name:
            name = row["student__email"]
        board.append(
            {
                "student_id": row["student_id"],
                "name": name,
                "points": points,
                "solved_count": row["solved_count"] or 0,
                "easy_count": easy,
                "medium_count": medium,
                "hard_count": hard,
                "last_solved_at": row["last_solved_at"],
            }
        )

    board.sort(
        key=lambda item: (
            -item["points"],
            -item["solved_count"],
            item["last_solved_at"] or timezone.now(),
        )
    )
    for index, item in enumerate(board[:limit], start=1):
        item["rank"] = index
    return board[:limit]


def recent_correct_solves(limit: int = 12) -> list:
    return list(
        ExerciseAttempt.objects.filter(
            is_correct=True,
            student__role=User.Role.STUDENT,
            exercise__is_published=True,
        )
        .select_related("student", "exercise")
        .order_by("-created_at")[:limit]
    )


def my_rank(board: list[dict], student_id: int) -> dict | None:
    for item in board:
        if item["student_id"] == student_id:
            return item
    return None
