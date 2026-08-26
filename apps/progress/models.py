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
