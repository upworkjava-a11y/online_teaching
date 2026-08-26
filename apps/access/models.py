from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models

from apps.core.models import TimeStampedModel


class UserContentAccess(TimeStampedModel):
    class Status(models.TextChoices):
        ALLOWED = "allowed", "Ruxsat berilgan"
        BLOCKED = "blocked", "Bloklangan"

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="content_access_rules",
    )
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey("content_type", "object_id")
    status = models.CharField(max_length=20, choices=Status.choices)
    reason = models.TextField(blank=True)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="created_access_rules",
    )

    class Meta:
        verbose_name = "Foydalanuvchi kontent ruxsati"
        verbose_name_plural = "Foydalanuvchi kontent ruxsatlari"
        constraints = [
            models.UniqueConstraint(
                fields=["user", "content_type", "object_id"],
                name="uniq_user_content_access",
            )
        ]
        indexes = [
            models.Index(fields=["user", "content_type", "object_id"]),
            models.Index(fields=["status"]),
        ]

    def __str__(self):
        return f"{self.user} — {self.status} — {self.content_object}"
