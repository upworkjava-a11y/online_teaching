"""Badge evaluation, awarding, and progress (server-side only)."""

from __future__ import annotations

from dataclasses import dataclass

from django.core.cache import cache
from django.db import transaction
from django.utils import timezone

from apps.badges.models import Badge, UserBadge, UserRankPeak
from apps.badges.services import metrics


TOAST_CACHE_KEY = "badges:toasts:{user_id}"


@dataclass
class BadgeProgress:
    badge: Badge
    current: int
    target: int
    earned: bool
    earned_at: object | None = None

    @property
    def ratio(self) -> float:
        if self.target <= 0:
            return 1.0 if self.earned else 0.0
        return min(1.0, self.current / self.target)

    @property
    def percent(self) -> int:
        return int(round(self.ratio * 100))

    @property
    def remaining(self) -> int:
        return max(0, self.target - self.current)


def queue_toast(user_id: int, badges: list[Badge]) -> None:
    if not badges:
        return
    key = TOAST_CACHE_KEY.format(user_id=user_id)
    existing = cache.get(key) or []
    slugs = {item.get("slug") for item in existing}
    for b in badges:
        if b.slug in slugs:
            continue
        existing.append(
            {
                "slug": b.slug,
                "name": b.name,
                "icon_url": b.icon_url,
                "rarity": b.rarity,
                "description": b.description,
            }
        )
    cache.set(key, existing, timeout=600)


def pop_toasts(user_id: int) -> list[dict]:
    key = TOAST_CACHE_KEY.format(user_id=user_id)
    items = cache.get(key) or []
    cache.delete(key)
    return items


def record_rank(user, rank: int) -> UserRankPeak | None:
    """Update historical best rank (lower is better)."""
    if rank is None or rank < 1:
        return None
    peak, created = UserRankPeak.objects.get_or_create(
        user=user,
        defaults={"best_rank": rank, "achieved_at": timezone.now()},
    )
    if not created and rank < peak.best_rank:
        peak.best_rank = rank
        peak.achieved_at = timezone.now()
        peak.save(update_fields=["best_rank", "achieved_at"])
    return peak


def best_rank(user) -> int | None:
    peak = UserRankPeak.objects.filter(user=user).first()
    return peak.best_rank if peak else None


def progress_value(user, badge: Badge) -> int:
    rt = badge.requirement_type
    meta = badge.requirement_meta or {}
    if rt == Badge.RequirementType.PROBLEMS_SOLVED:
        return metrics.problems_solved(user)
    if rt == Badge.RequirementType.TOPIC_PROBLEMS:
        topic = meta.get("topic") or ""
        return metrics.topic_problem_counts(user).get(topic, 0)
    if rt == Badge.RequirementType.DISTINCT_SQL_TOPICS:
        return metrics.distinct_sql_topics(user)
    if rt == Badge.RequirementType.STREAK:
        return metrics.longest_streak(user)
    if rt == Badge.RequirementType.LESSONS_COMPLETED:
        return metrics.lessons_completed(user)
    if rt == Badge.RequirementType.COURSE_COMPLETED:
        return metrics.courses_fully_completed(user)
    if rt == Badge.RequirementType.DIFFICULTY_SOLVED:
        return metrics.difficulty_solved(user, meta.get("difficulty") or "easy")
    if rt == Badge.RequirementType.COURSE_SOLVES:
        return metrics.course_solves(
            user,
            meta.get("course_slug") or "",
            include_skill_tests=bool(meta.get("include_skill_tests")),
        )
    if rt == Badge.RequirementType.COURSES_ACTIVE:
        return metrics.courses_active(
            user,
            min_solves=int(meta.get("min_solves") or 5),
            include_skill_tests=bool(meta.get("include_skill_tests", True)),
        )
    if rt == Badge.RequirementType.TOP_RANK:
        rank = best_rank(user)
        if rank is None:
            return 0
        # Progress: closer to 1 is better. Show as (target - rank + 1) capped.
        # For display: if best_rank <= target, current=target else current=0-ish.
        # Better UX: current = max(0, target - rank + 1) when rank known? 
        # Spec wants progress like 5/10 meaning need top 10. Use:
        # earned if rank <= value; progress current = value if earned else max(0, value - rank + 1) weird.
        # Simple: current = target if rank <= target else 0, OR show rank as inverse.
        # Use: current = target if (rank and rank <= target) else 0 for binary,
        # For partial: if rank is 15 and target 10, current=0; if rank 8, current=10.
        return badge.requirement_value if rank <= badge.requirement_value else 0
    if rt == Badge.RequirementType.PERFECT_WEEK:
        return metrics.perfect_week_progress(user)
    if rt == Badge.RequirementType.NIGHT_ACTIVITY:
        return metrics.night_activity_count(user)
    if rt == Badge.RequirementType.BADGES_EARNED:
        exclude = set(meta.get("exclude_slugs") or [])
        qs = UserBadge.objects.filter(user=user)
        if exclude:
            qs = qs.exclude(badge__slug__in=exclude)
        return qs.count()
    return 0


def is_satisfied(user, badge: Badge, current: int | None = None) -> bool:
    cur = progress_value(user, badge) if current is None else current
    if badge.requirement_type == Badge.RequirementType.TOP_RANK:
        rank = best_rank(user)
        return rank is not None and rank <= badge.requirement_value
    if badge.requirement_type == Badge.RequirementType.PERFECT_WEEK:
        return cur >= 7
    return cur >= badge.requirement_value


# Trigger → relevant requirement types
TRIGGER_MAP = {
    "solve": {
        Badge.RequirementType.PROBLEMS_SOLVED,
        Badge.RequirementType.TOPIC_PROBLEMS,
        Badge.RequirementType.DISTINCT_SQL_TOPICS,
        Badge.RequirementType.STREAK,
        Badge.RequirementType.NIGHT_ACTIVITY,
        Badge.RequirementType.PERFECT_WEEK,
        Badge.RequirementType.TOP_RANK,
        Badge.RequirementType.BADGES_EARNED,
        Badge.RequirementType.DIFFICULTY_SOLVED,
        Badge.RequirementType.COURSE_SOLVES,
        Badge.RequirementType.COURSES_ACTIVE,
    },
    "lesson": {
        Badge.RequirementType.LESSONS_COMPLETED,
        Badge.RequirementType.COURSE_COMPLETED,
        Badge.RequirementType.STREAK,
        Badge.RequirementType.NIGHT_ACTIVITY,
        Badge.RequirementType.PERFECT_WEEK,
        Badge.RequirementType.BADGES_EARNED,
    },
    "rank": {
        Badge.RequirementType.TOP_RANK,
        Badge.RequirementType.BADGES_EARNED,
    },
    "all": set(Badge.RequirementType.values),
}


@transaction.atomic
def award_if_eligible(user, badge: Badge) -> UserBadge | None:
    if UserBadge.objects.filter(user=user, badge=badge).exists():
        return None
    if not is_satisfied(user, badge):
        return None
    ub, created = UserBadge.objects.get_or_create(user=user, badge=badge)
    return ub if created else None


def evaluate(user, *, trigger: str = "all") -> list[UserBadge]:
    """Check relevant badges and award newly earned ones."""
    types = TRIGGER_MAP.get(trigger) or TRIGGER_MAP["all"]
    badges = list(Badge.objects.filter(is_active=True, requirement_type__in=types))
    earned_ids = set(
        UserBadge.objects.filter(user=user, badge_id__in=[b.pk for b in badges]).values_list(
            "badge_id", flat=True
        )
    )
    newly: list[UserBadge] = []
    # Non-legend first, then legend (depends on others)
    ordered = sorted(badges, key=lambda b: (b.slug == "legend", b.sort_order))
    for badge in ordered:
        if badge.pk in earned_ids:
            continue
        ub = award_if_eligible(user, badge)
        if ub:
            newly.append(ub)
            earned_ids.add(badge.pk)
    # Legend may become available after batch awards
    legend = next((b for b in badges if b.slug == "legend"), None)
    if legend and legend.pk not in earned_ids:
        ub = award_if_eligible(user, legend)
        if ub:
            newly.append(ub)
    if newly:
        queue_toast(user.pk, [ub.badge for ub in newly])
    return newly


def check_after_solve(user, exercise=None) -> list[UserBadge]:
    # Streak already updated by caller; refresh rank peak via lightweight board position optional
    return evaluate(user, trigger="solve")


def check_after_lesson(user) -> list[UserBadge]:
    return evaluate(user, trigger="lesson")


def check_after_rank_update(user, rank: int) -> list[UserBadge]:
    record_rank(user, rank)
    return evaluate(user, trigger="rank")


def user_badge_map(user) -> dict[int, UserBadge]:
    return {
        ub.badge_id: ub
        for ub in UserBadge.objects.filter(user=user).select_related("badge")
    }


def all_progress(user) -> list[BadgeProgress]:
    earned = user_badge_map(user)
    rows: list[BadgeProgress] = []
    for badge in Badge.objects.filter(is_active=True):
        ub = earned.get(badge.pk)
        current = progress_value(user, badge)
        target = badge.requirement_value
        if badge.requirement_type == Badge.RequirementType.PERFECT_WEEK:
            target = 7
        rows.append(
            BadgeProgress(
                badge=badge,
                current=min(current, target) if target else current,
                target=target,
                earned=ub is not None,
                earned_at=ub.earned_at if ub else None,
            )
        )
    return rows


def badge_counts(user_ids: list[int]) -> dict[int, int]:
    if not user_ids:
        return {}
    from django.db.models import Count

    rows = (
        UserBadge.objects.filter(user_id__in=user_ids)
        .values("user_id")
        .annotate(c=Count("id"))
    )
    return {r["user_id"]: r["c"] for r in rows}
