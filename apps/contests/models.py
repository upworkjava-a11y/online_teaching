from django.conf import settings
from django.db import models
from django.utils import timezone

from apps.core.models import TimeStampedModel


class Contest(TimeStampedModel):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=220, unique=True)
    description = models.TextField(blank=True)
    starts_at = models.DateTimeField()
    ends_at = models.DateTimeField()
    is_published = models.BooleanField(default=False)
    exercises = models.ManyToManyField(
        "exercises.Exercise",
        through="ContestExercise",
        related_name="contests",
        blank=True,
    )

    class Meta:
        ordering = ["-starts_at"]
        verbose_name = "Musobaqa"
        verbose_name_plural = "Musobaqalar"

    def __str__(self):
        return self.title

    @property
    def is_active(self) -> bool:
        now = timezone.now()
        return self.is_published and self.starts_at <= now <= self.ends_at

    @property
    def status_label(self) -> str:
        now = timezone.now()
        if not self.is_published:
            return "Yashirin"
        if now < self.starts_at:
            return "Tez orada"
        if now > self.ends_at:
            return "Tugagan"
        return "Davom etmoqda"


class ContestExercise(models.Model):
    contest = models.ForeignKey(Contest, on_delete=models.CASCADE)
    exercise = models.ForeignKey("exercises.Exercise", on_delete=models.CASCADE)
    order = models.PositiveIntegerField(default=0)
    points = models.PositiveIntegerField(default=0, help_text="0 bo‘lsa mashq qiyinligiga qarab hisoblanadi")

    class Meta:
        ordering = ["order", "id"]
        unique_together = [("contest", "exercise")]
        verbose_name = "Musobaqa mashqi"
        verbose_name_plural = "Musobaqa mashqlari"


class ContestScore(TimeStampedModel):
    contest = models.ForeignKey(Contest, on_delete=models.CASCADE, related_name="scores")
    student = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="contest_scores",
    )
    points = models.PositiveIntegerField(default=0)
    solved_count = models.PositiveIntegerField(default=0)
    last_solved_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ["-points", "last_solved_at", "id"]
        verbose_name = "Musobaqa balli"
        verbose_name_plural = "Musobaqa ballari"
        constraints = [
            models.UniqueConstraint(fields=["contest", "student"], name="uniq_contest_student_score")
        ]

    def __str__(self):
        return f"{self.contest} — {self.student}: {self.points}"
