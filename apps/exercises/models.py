from django.conf import settings
from django.db import models

from apps.core.models import TimeStampedModel


class Dataset(TimeStampedModel):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    schema_sql = models.TextField()
    seed_sql = models.TextField()
    preview = models.JSONField(default=dict, blank=True)

    class Meta:
        verbose_name = "Dataset"
        verbose_name_plural = "Datasetlar"

    def __str__(self):
        return self.name


class Exercise(TimeStampedModel):
    class Kind(models.TextChoices):
        SQL = "sql", "SQL"
        QUIZ = "quiz", "Test"

    class Difficulty(models.TextChoices):
        EASY = "easy", "Oson"
        MEDIUM = "medium", "O‘rta"
        HARD = "hard", "Qiyin"

    module = models.ForeignKey("courses.Module", on_delete=models.CASCADE, related_name="exercises")
    lecture = models.ForeignKey(
        "courses.Lecture",
        on_delete=models.SET_NULL,
        related_name="practice_exercises",
        null=True,
        blank=True,
        help_text="Darsga biriktirilgan amaliy mashq",
    )
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=220)
    description = models.TextField()
    task = models.TextField()
    hints = models.JSONField(default=list, blank=True)
    editorial = models.TextField(
        blank=True,
        help_text="To‘g‘ri yechgandan keyin ko‘rsatiladigan yechim yo‘riqnomasi (o‘zbekcha)",
    )
    kind = models.CharField(max_length=20, choices=Kind.choices, default=Kind.SQL)
    difficulty = models.CharField(
        max_length=10,
        choices=Difficulty.choices,
        default=Difficulty.EASY,
        db_index=True,
    )
    quiz_options = models.JSONField(
        default=list,
        blank=True,
        help_text='Test variantlari, masalan: ["A) ...", "B) ..."]',
    )
    is_skill_test = models.BooleanField(
        default=False,
        db_index=True,
        help_text="Modul oxiridagi bilimsini tekshirish testi",
    )
    order = models.PositiveIntegerField(default=0)
    is_published = models.BooleanField(default=False)
    require_row_order = models.BooleanField(default=False)
    require_column_order = models.BooleanField(default=False)
    max_score = models.PositiveIntegerField(default=100)
    datasets = models.ManyToManyField(Dataset, through="ExerciseDataset", related_name="exercises", blank=True)

    class Meta:
        ordering = ["order", "id"]
        verbose_name = "Mashq"
        verbose_name_plural = "Mashqlar"
        unique_together = [("module", "slug")]
        indexes = [models.Index(fields=["module", "is_published", "order"])]

    def __str__(self):
        return self.title

    @property
    def course(self):
        return self.module.course

    @property
    def difficulty_label(self) -> str:
        return {
            self.Difficulty.EASY: "Oson",
            self.Difficulty.MEDIUM: "O‘rta",
            self.Difficulty.HARD: "Qiyin",
        }.get(self.difficulty, self.difficulty)


class ExerciseDataset(models.Model):
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    dataset = models.ForeignKey(Dataset, on_delete=models.CASCADE)

    class Meta:
        unique_together = [("exercise", "dataset")]
        verbose_name = "Mashq dataseti"
        verbose_name_plural = "Mashq datasetlari"


class ExerciseExpectedResult(TimeStampedModel):
    exercise = models.OneToOneField(Exercise, on_delete=models.CASCADE, related_name="expected_result")
    columns = models.JSONField(default=list)
    rows = models.JSONField(default=list)

    class Meta:
        verbose_name = "Kutilgan natija"
        verbose_name_plural = "Kutilgan natijalar"

    def __str__(self):
        return f"Expected: {self.exercise}"


class ExerciseAttempt(TimeStampedModel):
    student = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="exercise_attempts",
    )
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE, related_name="attempts")
    sql_query = models.TextField()
    is_correct = models.BooleanField(default=False)
    score = models.PositiveIntegerField(default=0)
    result_preview = models.JSONField(default=dict, blank=True)
    error_message = models.TextField(blank=True)
    execution_ms = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Mashq urinishi"
        verbose_name_plural = "Mashq urinishlari"
        indexes = [
            models.Index(fields=["student", "exercise", "-created_at"]),
            models.Index(fields=["exercise", "is_correct"]),
        ]

    def __str__(self):
        return f"{self.student} — {self.exercise} — {self.created_at}"


class ExerciseComment(TimeStampedModel):
    """Masala ostidagi muhokama."""

    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="exercise_comments",
    )
    body = models.TextField(max_length=2000)
    is_hidden = models.BooleanField(default=False)

    class Meta:
        ordering = ["created_at"]
        verbose_name = "Masala izohi"
        verbose_name_plural = "Masala izohlari"
        indexes = [models.Index(fields=["exercise", "created_at"])]

    def __str__(self):
        return f"{self.author} — {self.exercise_id}"
