from django.conf import settings
from django.core.validators import FileExtensionValidator
from django.db import models

from apps.core.models import TimeStampedModel


class HomeworkAssignment(TimeStampedModel):
    lecture = models.OneToOneField(
        "courses.Lecture",
        on_delete=models.CASCADE,
        related_name="homework_assignment",
    )
    title = models.CharField(max_length=200)
    instructions = models.TextField()
    max_score = models.PositiveIntegerField(default=100)
    is_published = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Uy vazifasi"
        verbose_name_plural = "Uy vazifalari"

    def __str__(self):
        return self.title


class HomeworkSubmission(TimeStampedModel):
    class Status(models.TextChoices):
        SUBMITTED = "submitted", "Yuborilgan"
        UNDER_REVIEW = "under_review", "Ko‘rib chiqilmoqda"
        REVIEWED = "reviewed", "Tekshirilgan"
        NEEDS_REVISION = "needs_revision", "Qayta topshirish kerak"

    assignment = models.ForeignKey(
        HomeworkAssignment,
        on_delete=models.CASCADE,
        related_name="submissions",
    )
    student = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="homework_submissions",
    )
    file = models.FileField(
        upload_to="homework/%Y/%m/",
        validators=[FileExtensionValidator(allowed_extensions=["txt"])],
    )
    original_filename = models.CharField(max_length=255)
    status = models.CharField(max_length=30, choices=Status.choices, default=Status.SUBMITTED)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Topshiriq"
        verbose_name_plural = "Topshiriqlar"
        constraints = [
            models.UniqueConstraint(
                fields=["student", "assignment"],
                name="homework_one_submission_per_student_assignment",
            ),
        ]
        indexes = [
            models.Index(fields=["student", "assignment", "-created_at"]),
            models.Index(fields=["status"]),
        ]

    def __str__(self):
        return f"{self.student} — {self.assignment} #{self.pk}"

    @property
    def latest_review(self):
        return self.reviews.order_by("-created_at").first()


class HomeworkReview(TimeStampedModel):
    class Status(models.TextChoices):
        REVIEWED = "reviewed", "Tekshirilgan"
        NEEDS_REVISION = "needs_revision", "Qayta topshirish kerak"

    submission = models.ForeignKey(
        HomeworkSubmission,
        on_delete=models.CASCADE,
        related_name="reviews",
    )
    reviewer = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name="homework_reviews",
    )
    score = models.PositiveIntegerField()
    feedback = models.TextField()
    additional_instructions = models.TextField(blank=True)
    status = models.CharField(max_length=30, choices=Status.choices, default=Status.REVIEWED)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Tekshiruv"
        verbose_name_plural = "Tekshiruvlar"

    def __str__(self):
        return f"Review #{self.pk} for {self.submission}"


class NotificationHook(TimeStampedModel):
    """Placeholder so future notifications can be added without schema redesign."""

    class Event(models.TextChoices):
        HOMEWORK_SUBMITTED = "homework_submitted", "Uy vazifasi yuborildi"
        HOMEWORK_REVIEWED = "homework_reviewed", "Uy vazifasi tekshirildi"
        HOMEWORK_REVISION = "homework_revision", "Qayta topshirish so‘raldi"

    event = models.CharField(max_length=50, choices=Event.choices)
    payload = models.JSONField(default=dict)
    processed = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Bildirishnoma hodisasi"
        verbose_name_plural = "Bildirishnoma hodisalari"
