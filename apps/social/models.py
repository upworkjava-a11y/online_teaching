"""Social / messaging models: profile extras, chat, follow, block, activity."""

from __future__ import annotations

from django.conf import settings
from django.db import models
from django.db.models import F, Q
from django.utils import timezone

from apps.accounts.avatars import DEFAULT_AVATAR_KEY
from apps.core.models import TimeStampedModel


def conversation_pair_key(user_a_id: int, user_b_id: int) -> str:
    low, high = sorted((int(user_a_id), int(user_b_id)))
    return f"{low}:{high}"


class SocialProfile(TimeStampedModel):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="social_profile",
    )
    avatar_preset = models.CharField(max_length=32, default=DEFAULT_AVATAR_KEY, blank=True)
    avatar_image = models.ImageField(upload_to="avatars/%Y/%m/", blank=True, null=True)
    bio = models.CharField(max_length=280, blank=True)

    class Meta:
        verbose_name = "Profil"
        verbose_name_plural = "Profillar"

    def __str__(self):
        return f"SocialProfile<{self.user_id}>"

    @property
    def uses_upload(self) -> bool:
        return bool(self.avatar_image)


class Conversation(TimeStampedModel):
    """1-to-1 conversation identified by sorted participant pair_key."""

    pair_key = models.CharField(max_length=64, unique=True, db_index=True)
    participants = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        through="ConversationParticipant",
        related_name="conversations",
    )

    class Meta:
        ordering = ["-updated_at"]
        verbose_name = "Suhbat"
        verbose_name_plural = "Suhbatlar"
        indexes = [models.Index(fields=["-updated_at"])]

    def __str__(self):
        return f"Conversation {self.pair_key}"


class ConversationParticipant(models.Model):
    conversation = models.ForeignKey(
        Conversation,
        on_delete=models.CASCADE,
        related_name="memberships",
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="conversation_memberships",
    )
    last_read_at = models.DateTimeField(null=True, blank=True)
    joined_at = models.DateTimeField(default=timezone.now)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["conversation", "user"],
                name="uniq_conversation_participant",
            )
        ]
        indexes = [models.Index(fields=["user", "conversation"])]

    def __str__(self):
        return f"{self.user_id} in {self.conversation_id}"


class Message(models.Model):
    conversation = models.ForeignKey(
        Conversation,
        on_delete=models.CASCADE,
        related_name="messages",
    )
    sender = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="social_messages",
    )
    text = models.TextField(max_length=2000)
    created_at = models.DateTimeField(default=timezone.now, db_index=True)
    read_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ["created_at"]
        verbose_name = "Xabar"
        verbose_name_plural = "Xabarlar"
        indexes = [
            models.Index(fields=["conversation", "created_at"]),
            models.Index(fields=["sender", "created_at"]),
            models.Index(fields=["conversation", "read_at"]),
        ]

    def __str__(self):
        return f"Msg {self.pk} by {self.sender_id}"


class Follow(models.Model):
    follower = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="following_set",
    )
    following = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="followers_set",
    )
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["follower", "following"], name="uniq_follow_pair"),
            models.CheckConstraint(
                condition=~Q(follower=F("following")),
                name="prevent_self_follow",
            ),
        ]
        indexes = [
            models.Index(fields=["follower", "-created_at"]),
            models.Index(fields=["following", "-created_at"]),
        ]
        verbose_name = "Obuna"
        verbose_name_plural = "Obunalar"

    def __str__(self):
        return f"{self.follower_id} → {self.following_id}"


class Block(models.Model):
    blocker = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="blocks_made",
    )
    blocked = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="blocks_received",
    )
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["blocker", "blocked"], name="uniq_block_pair"),
            models.CheckConstraint(
                condition=~Q(blocker=F("blocked")),
                name="prevent_self_block",
            ),
        ]
        indexes = [
            models.Index(fields=["blocker"]),
            models.Index(fields=["blocked"]),
        ]
        verbose_name = "Blok"
        verbose_name_plural = "Bloklar"

    def __str__(self):
        return f"{self.blocker_id} blocks {self.blocked_id}"


class UserActivity(models.Model):
    class ActivityType(models.TextChoices):
        LESSON = "lesson", "Dars tugallandi"
        EXERCISE = "exercise", "Mashq yechildi"
        QUIZ = "quiz", "Quiz / bilim testi"

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="learning_activities",
    )
    date = models.DateField(db_index=True)
    activity_type = models.CharField(max_length=20, choices=ActivityType.choices)
    count = models.PositiveIntegerField(default=0)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["user", "date", "activity_type"],
                name="uniq_user_day_activity_type",
            )
        ]
        indexes = [
            models.Index(fields=["user", "date"]),
            models.Index(fields=["date"]),
        ]
        verbose_name = "Faoliyat"
        verbose_name_plural = "Faoliyatlar"

    def __str__(self):
        return f"{self.user_id} {self.date} {self.activity_type}={self.count}"
