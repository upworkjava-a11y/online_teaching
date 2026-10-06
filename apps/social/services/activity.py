"""Learning activity aggregation for contribution calendar."""

from __future__ import annotations

import calendar
from datetime import date, timedelta

from django.db.models import F, Sum
from django.db.models.functions import Coalesce
from django.utils import timezone

from apps.social.models import UserActivity


def record_activity(user, activity_type: str, amount: int = 1, on_date: date | None = None) -> UserActivity:
    on_date = on_date or timezone.localdate()
    row, _ = UserActivity.objects.get_or_create(
        user=user,
        date=on_date,
        activity_type=activity_type,
        defaults={"count": 0},
    )
    UserActivity.objects.filter(pk=row.pk).update(count=F("count") + amount)
    row.refresh_from_db(fields=["count"])
    return row


def record_lesson(user) -> UserActivity:
    return record_activity(user, UserActivity.ActivityType.LESSON)


def record_exercise(user, *, is_quiz: bool = False) -> UserActivity:
    kind = UserActivity.ActivityType.QUIZ if is_quiz else UserActivity.ActivityType.EXERCISE
    return record_activity(user, kind)


def day_totals(user, start: date, end: date) -> dict[date, int]:
    rows = (
        UserActivity.objects.filter(user=user, date__gte=start, date__lte=end)
        .values("date")
        .annotate(total=Coalesce(Sum("count"), 0))
    )
    return {row["date"]: int(row["total"]) for row in rows}


def intensity(count: int) -> int:
    """0..4 levels for calendar cells."""
    if count <= 0:
        return 0
    if count == 1:
        return 1
    if count <= 3:
        return 2
    if count <= 6:
        return 3
    return 4


def year_calendar(user, year: int | None = None) -> dict:
    year = year or timezone.localdate().year
    start = date(year, 1, 1)
    end = date(year, 12, 31)
    totals = day_totals(user, start, end)
    cursor = start - timedelta(days=start.weekday())
    weeks: list[list[dict | None]] = []
    while cursor <= end:
        week: list[dict | None] = []
        for _ in range(7):
            if cursor.year != year:
                week.append(None)
            else:
                c = totals.get(cursor, 0)
                week.append(
                    {
                        "date": cursor.isoformat(),
                        "count": c,
                        "level": intensity(c),
                        "label": cursor.strftime("%d.%m.%Y"),
                    }
                )
            cursor += timedelta(days=1)
        weeks.append(week)
    months = [
        {"num": m, "name": calendar.month_abbr[m], "key": f"{year}-{m:02d}"}
        for m in range(1, 13)
    ]
    return {"year": year, "weeks": weeks, "months": months, "totals": totals}


def month_calendar(user, year: int, month: int) -> dict:
    start = date(year, month, 1)
    last_day = calendar.monthrange(year, month)[1]
    end = date(year, month, last_day)
    totals = day_totals(user, start, end)
    cursor = start - timedelta(days=start.weekday())
    weeks: list[list[dict]] = []
    for _ in range(6):
        week: list[dict] = []
        for _dow in range(7):
            if cursor.month != month or cursor.year != year:
                week.append({"date": None, "count": 0, "level": 0, "day": None})
            else:
                c = totals.get(cursor, 0)
                week.append(
                    {
                        "date": cursor.isoformat(),
                        "count": c,
                        "level": intensity(c),
                        "day": cursor.day,
                        "label": cursor.strftime("%d.%m.%Y"),
                    }
                )
            cursor += timedelta(days=1)
        weeks.append(week)
        if cursor > end:
            break
    return {
        "year": year,
        "month": month,
        "name": calendar.month_name[month],
        "weeks": weeks,
    }


def day_breakdown(user, day: date) -> dict:
    rows = UserActivity.objects.filter(user=user, date=day)
    by_type = {r.activity_type: r.count for r in rows}
    lesson = by_type.get(UserActivity.ActivityType.LESSON, 0)
    exercise = by_type.get(UserActivity.ActivityType.EXERCISE, 0)
    quiz = by_type.get(UserActivity.ActivityType.QUIZ, 0)
    return {
        "date": day.isoformat(),
        "label": day.strftime("%d.%m.%Y"),
        "lesson": lesson,
        "exercise": exercise,
        "quiz": quiz,
        "total": lesson + exercise + quiz,
    }
