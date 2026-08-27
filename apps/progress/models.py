from django.conf import settings
from django.db import models

from apps.core.models import TimeStampedModel


class LectureProgress(TimeStampedModel):
    student = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="lecture_progress",
    )
    lecture = models.ForeignKey("courses.Lecture", on_delete=models.CASCADE, related_name="progress_rows")
    completed = models.BooleanField(default=False)
    completed_at = models.DateTimeField(null=True, blank=True)
    last_viewed_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        verbose_name = "Ma’ruza progressi"
        verbose_name_plural = "Ma’ruza progresslari"
        constraints = [
            models.UniqueConstraint(fields=["student", "lecture"], name="uniq_student_lecture_progress")
        ]
        indexes = [
            models.Index(fields=["student", "completed"]),
            models.Index(fields=["lecture"]),
        ]

    def __str__(self):
        return f"{self.student} — {self.lecture}"


class CourseProgress(TimeStampedModel):
    student = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="course_progress",
    )
    course = models.ForeignKey("courses.Course", on_delete=models.CASCADE, related_name="progress_rows")
    last_lecture = models.ForeignKey(
        "courses.Lecture",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="+",
    )
    last_activity_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        verbose_name = "Kurs progressi"
        verbose_name_plural = "Kurs progresslari"
        constraints = [
            models.UniqueConstraint(fields=["student", "course"], name="uniq_student_course_progress")
        ]
        indexes = [models.Index(fields=["student", "course"])]

    def __str__(self):
        return f"{self.student} — {self.course}"


class StudentStreak(TimeStampedModel):
    """Kunlik masala yechish zanjiri."""

    student = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="streak",
    )
    current_streak = models.PositiveIntegerField(default=0)
    longest_streak = models.PositiveIntegerField(default=0)
    last_solved_date = models.DateField(null=True, blank=True)

    class Meta:
        verbose_name = "Kunlik zanjir"
        verbose_name_plural = "Kunlik zanjirlar"

    def __str__(self):
        return f"{self.student} — {self.current_streak} kun"


class Certificate(TimeStampedModel):
    class Kind(models.TextChoices):
        MODULE = "module", "Modul"
        COURSE = "course", "Kurs"

    student = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="certificates",
    )
    kind = models.CharField(max_length=20, choices=Kind.choices)
    module = models.ForeignKey(
        "courses.Module",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="certificates",
    )
    course = models.ForeignKey(
        "courses.Course",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="certificates",
    )
    title = models.CharField(max_length=255)
    code = models.CharField(max_length=32, unique=True)
    issued_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Sertifikat"
        verbose_name_plural = "Sertifikatlar"
        ordering = ["-issued_at"]
        indexes = [models.Index(fields=["student", "-issued_at"])]

    def __str__(self):
        return f"{self.title} — {self.student}"
