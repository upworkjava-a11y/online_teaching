from django.db import models
from django.utils.text import slugify

from apps.core.models import TimeStampedModel


class PublishableQuerySet(models.QuerySet):
    def published(self):
        return self.filter(is_published=True)


class Course(TimeStampedModel):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=220, unique=True)
    description = models.TextField(blank=True)
    order = models.PositiveIntegerField(default=0)
    is_published = models.BooleanField(default=False)
    is_visible = models.BooleanField(default=False, help_text="Talabalar ro‘yxatida ko‘rinsinmi")

    objects = PublishableQuerySet.as_manager()

    class Meta:
        ordering = ["order", "id"]
        verbose_name = "Kurs"
        verbose_name_plural = "Kurslar"
        indexes = [models.Index(fields=["is_published", "is_visible", "order"])]

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title) or f"course-{self.pk or 'new'}"
        super().save(*args, **kwargs)


class Module(TimeStampedModel):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="modules")
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=220)
    description = models.TextField(blank=True)
    order = models.PositiveIntegerField(default=0)
    is_published = models.BooleanField(default=False)

    objects = PublishableQuerySet.as_manager()

    class Meta:
        ordering = ["order", "id"]
        verbose_name = "Modul"
        verbose_name_plural = "Modullar"
        unique_together = [("course", "slug")]
        indexes = [models.Index(fields=["course", "is_published", "order"])]

    def __str__(self):
        return f"{self.course.title} — {self.title}"


class Lecture(TimeStampedModel):
    module = models.ForeignKey(Module, on_delete=models.CASCADE, related_name="lectures")
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=220)
    content = models.TextField(help_text="Uzbek tilidagi boy matn (HTML)")
    sql_examples = models.JSONField(default=list, blank=True)
    order = models.PositiveIntegerField(default=0)
    is_published = models.BooleanField(default=False)

    objects = PublishableQuerySet.as_manager()

    class Meta:
        ordering = ["order", "id"]
        verbose_name = "Ma’ruza"
        verbose_name_plural = "Ma’ruzalar"
        unique_together = [("module", "slug")]
        indexes = [models.Index(fields=["module", "is_published", "order"])]

    def __str__(self):
        return self.title

    @property
    def course(self):
        return self.module.course

    def get_previous(self):
        return (
            Lecture.objects.filter(module=self.module, is_published=True, order__lt=self.order)
            .order_by("-order")
            .first()
        )

    def get_next(self):
        nxt = (
            Lecture.objects.filter(module=self.module, is_published=True, order__gt=self.order)
            .order_by("order")
            .first()
        )
        if nxt:
            return nxt
        next_module = (
            Module.objects.filter(course=self.module.course, is_published=True, order__gt=self.module.order)
            .order_by("order")
            .first()
        )
        if next_module:
            return next_module.lectures.filter(is_published=True).order_by("order").first()
        return None


class CourseEnrollment(TimeStampedModel):
    student = models.ForeignKey("accounts.User", on_delete=models.CASCADE, related_name="enrollments")
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="enrollments")

    class Meta:
        verbose_name = "Kursga yozilish"
        verbose_name_plural = "Kursga yozilishlar"
        constraints = [models.UniqueConstraint(fields=["student", "course"], name="uniq_student_course_enrollment")]
        indexes = [models.Index(fields=["course", "student"])]

    def __str__(self):
        return f"{self.student} → {self.course}"
