"""Badge definitions and earned achievements."""

from __future__ import annotations

from django.conf import settings
from django.db import models
from django.utils import timezone

from apps.core.models import TimeStampedModel


class Badge(TimeStampedModel):
    class Category(models.TextChoices):
        PROBLEM = "problem", "Problem Solving"
        CONSISTENCY = "consistency", "Consistency"
        LEARNING = "learning", "Learning"
        COMPETITION = "competition", "Competition"
        MASTERY = "mastery", "Mastery"
        PLATFORM = "platform", "Platform"

    class RequirementType(models.TextChoices):
        PROBLEMS_SOLVED = "problems_solved", "Problems solved"
        TOPIC_PROBLEMS = "topic_problems", "Topic problems"
        DISTINCT_SQL_TOPICS = "distinct_sql_topics", "Distinct SQL topics"
        STREAK = "streak", "Streak days"
        LESSONS_COMPLETED = "lessons_completed", "Lessons completed"
        COURSE_COMPLETED = "course_completed", "Course completed"
        TOP_RANK = "top_rank", "Best leaderboard rank"
        PERFECT_WEEK = "perfect_week", "Perfect calendar week"
        NIGHT_ACTIVITY = "night_activity", "Night learning activities"
        BADGES_EARNED = "badges_earned", "Other badges earned"

    slug = models.SlugField(max_length=64, unique=True)
    name = models.CharField(max_length=120)
    description = models.TextField()
    category = models.CharField(max_length=20, choices=Category.choices, db_index=True)
    icon_path = models.CharField(
        max_length=255,
        blank=True,
        help_text="Static path, e.g. badges/first-step.svg",
    )
    rarity = models.CharField(
        max_length=20,
        blank=True,
        default="common",
        help_text="common | rare | epic | legendary (visual weight)",
    )
    requirement_type = models.CharField(max_length=40, choices=RequirementType.choices)
    requirement_value = models.PositiveIntegerField(default=1)
    requirement_meta = models.JSONField(default=dict, blank=True)
    sort_order = models.PositiveSmallIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["sort_order", "id"]
        verbose_name = "Badge"
        verbose_name_plural = "Badges"

    def __str__(self):
        return self.name

    @property
    def icon_url(self) -> str:
        if self.icon_path:
            return f"/static/{self.icon_path.lstrip('/')}"
        return "/static/badges/first-step.svg"


class UserBadge(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="earned_badges",
    )
    badge = models.ForeignKey(Badge, on_delete=models.CASCADE, related_name="holders")
    earned_at = models.DateTimeField(default=timezone.now, db_index=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["user", "badge"], name="uniq_user_badge"),
        ]
        indexes = [
            models.Index(fields=["user", "-earned_at"]),
            models.Index(fields=["badge"]),
        ]
        verbose_name = "User badge"
        verbose_name_plural = "User badges"

    def __str__(self):
        return f"{self.user_id}:{self.badge.slug}"


class UserRankPeak(models.Model):
    """Historical best leaderboard rank (1 = first place)."""

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="rank_peak",
    )
    best_rank = models.PositiveIntegerField()
    achieved_at = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = "Rank peak"
        verbose_name_plural = "Rank peaks"

    def __str__(self):
        return f"{self.user_id} best=#{self.best_rank}"
