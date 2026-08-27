from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.utils import timezone

from apps.core.models import TimeStampedModel


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("Email manzili majburiy.")
        email = self.normalize_email(email)
        extra_fields.setdefault("username", email.split("@")[0])
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        extra_fields.setdefault("role", User.Role.STUDENT)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("role", User.Role.ADMIN)
        extra_fields.setdefault("is_active", True)
        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser is_staff=True bo‘lishi kerak.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser is_superuser=True bo‘lishi kerak.")
        return self._create_user(email, password, **extra_fields)


class User(AbstractUser):
    class Role(models.TextChoices):
        STUDENT = "student", "Talaba"
        TEACHER = "teacher", "O‘qituvchi"
        ADMIN = "admin", "Administrator"

    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField("Email", unique=True)
    role = models.CharField(max_length=20, choices=Role.choices, default=Role.STUDENT)
    is_blocked = models.BooleanField(default=False)
    is_premium = models.BooleanField(
        default=False,
        verbose_name="Premium",
        help_text="Belgilansa, foydalanuvchi har bir kursning barcha modullarini ochadi. Belgilanmasa — faqat dastlabki 5 modul.",
    )
    last_activity_at = models.DateTimeField(null=True, blank=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    objects = UserManager()

    class Meta:
        verbose_name = "Foydalanuvchi"
        verbose_name_plural = "Foydalanuvchilar"
        indexes = [
            models.Index(fields=["role"]),
            models.Index(fields=["email"]),
            models.Index(fields=["last_activity_at"]),
        ]

    def __str__(self):
        return self.get_full_name() or self.email

    def get_full_name(self):
        name = f"{self.first_name} {self.last_name}".strip()
        return name or self.email

    @property
    def is_student(self):
        return self.role == self.Role.STUDENT

    @property
    def is_teacher(self):
        return self.role == self.Role.TEACHER

    @property
    def is_admin(self):
        return self.role == self.Role.ADMIN or self.is_superuser

    def mark_activity(self):
        self.last_activity_at = timezone.now()
        self.save(update_fields=["last_activity_at"])


class StudentProfile(TimeStampedModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="student_profile")
    bio = models.TextField(blank=True)

    class Meta:
        verbose_name = "Talaba profili"
        verbose_name_plural = "Talaba profillari"

    def __str__(self):
        return f"Talaba: {self.user}"


class TeacherProfile(TimeStampedModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="teacher_profile")
    bio = models.TextField(blank=True)
    assigned_courses = models.ManyToManyField(
        "courses.Course",
        blank=True,
        related_name="teachers",
    )

    class Meta:
        verbose_name = "O‘qituvchi profili"
        verbose_name_plural = "O‘qituvchi profillari"

    def __str__(self):
        return f"O‘qituvchi: {self.user}"


class GoogleAccount(TimeStampedModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="google_account")
    google_sub = models.CharField(max_length=255, unique=True)
    email = models.EmailField()

    class Meta:
        verbose_name = "Google hisobi"
        verbose_name_plural = "Google hisoblari"

    def __str__(self):
        return f"{self.email} ({self.google_sub})"


class TelegramAccount(TimeStampedModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="telegram_account")
    telegram_id = models.BigIntegerField(unique=True)
    telegram_username = models.CharField(max_length=255, blank=True)
    notify_enabled = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Telegram hisobi"
        verbose_name_plural = "Telegram hisoblari"
        indexes = [models.Index(fields=["telegram_id"], name="accounts_te_telegra_idx")]

    def __str__(self):
        return f"{self.user} ({self.telegram_id})"


class Announcement(TimeStampedModel):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="announcements")
    title = models.CharField(max_length=200)
    body = models.TextField()
    is_published = models.BooleanField(default=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "E’lon"
        verbose_name_plural = "E’lonlar"

    def __str__(self):
        return self.title


class DirectMessage(TimeStampedModel):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="sent_messages")
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name="received_messages")
    body = models.TextField()
    read_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Xabar"
        verbose_name_plural = "Xabarlar"

    def __str__(self):
        return f"{self.sender} → {self.recipient}"


class SupportTicket(TimeStampedModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="support_tickets")
    message = models.TextField()
    reply = models.TextField(blank=True)
    is_resolved = models.BooleanField(default=False)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Yordam so‘rovi"
        verbose_name_plural = "Yordam so‘rovlari"

    def __str__(self):
        return f"Ticket #{self.pk} {self.user}"
