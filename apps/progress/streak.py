from datetime import timedelta

from django.utils import timezone

from .models import StudentStreak


def record_correct_solve(student) -> StudentStreak:
    """To‘g‘ri yechimdan keyin kunlik zanjirni yangilaydi."""
    today = timezone.localdate()
    streak, _ = StudentStreak.objects.get_or_create(student=student)
    if streak.last_solved_date == today:
        return streak
    if streak.last_solved_date == today - timedelta(days=1):
        streak.current_streak += 1
    else:
        streak.current_streak = 1
    streak.longest_streak = max(streak.longest_streak, streak.current_streak)
    streak.last_solved_date = today
    streak.save(update_fields=["current_streak", "longest_streak", "last_solved_date", "updated_at"])
    return streak


def get_streak(student) -> StudentStreak | None:
    streak = getattr(student, "streak", None)
    if streak is not None:
        return streak
    return StudentStreak.objects.filter(student=student).first()
