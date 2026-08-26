from __future__ import annotations

from asgiref.sync import sync_to_async
from django.contrib.auth import authenticate
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError

from apps.accounts.models import TelegramAccount, User
from apps.courses.models import Course, CourseEnrollment


def _unique_username(email: str) -> str:
    base = (email.split("@")[0] or "user")[:120]
    username = base
    n = 1
    while User.objects.filter(username=username).exists():
        username = f"{base}{n}"
        n += 1
    return username


@sync_to_async
def get_user_by_telegram(telegram_id: int):
    acc = TelegramAccount.objects.select_related("user").filter(telegram_id=telegram_id).first()
    return acc.user if acc else None


@sync_to_async
def link_telegram(user: User, telegram_id: int, telegram_username: str = "") -> str:
    existing = TelegramAccount.objects.filter(telegram_id=telegram_id).select_related("user").first()
    if existing and existing.user_id != user.pk:
        return "bu_telegram_boshqa_akkaunt"
    other = TelegramAccount.objects.filter(user=user).exclude(telegram_id=telegram_id).first()
    if other:
        return "akkaunt_boshqa_telegram"
    TelegramAccount.objects.update_or_create(
        user=user,
        defaults={"telegram_id": telegram_id, "telegram_username": telegram_username or ""},
    )
    user.mark_activity()
    return "ok"


@sync_to_async
def unlink_telegram(telegram_id: int) -> None:
    TelegramAccount.objects.filter(telegram_id=telegram_id).delete()


@sync_to_async
def login_user(email: str, password: str, telegram_id: int, telegram_username: str) -> tuple[str, User | None]:
    user = authenticate(username=email.strip().lower(), password=password)
    if user is None:
        return "bad_password", None
    if not user.is_active or user.is_blocked:
        return "blocked", None
    code = _link(user, telegram_id, telegram_username)
    if code != "ok":
        return code, None
    return "ok", user


def _link(user, telegram_id, telegram_username) -> str:
    existing = TelegramAccount.objects.filter(telegram_id=telegram_id).select_related("user").first()
    if existing and existing.user_id != user.pk:
        return "bu_telegram_boshqa_akkaunt"
    other = TelegramAccount.objects.filter(user=user).exclude(telegram_id=telegram_id).first()
    if other:
        return "akkaunt_boshqa_telegram"
    TelegramAccount.objects.update_or_create(
        user=user,
        defaults={"telegram_id": telegram_id, "telegram_username": telegram_username or ""},
    )
    user.mark_activity()
    return "ok"


@sync_to_async
def register_user(
    first_name: str,
    last_name: str,
    email: str,
    password: str,
    telegram_id: int,
    telegram_username: str,
) -> tuple[str, User | None]:
    email = email.strip().lower()
    if User.objects.filter(email__iexact=email).exists():
        return "email_exists", None
    try:
        validate_password(password)
    except ValidationError as exc:
        return "weak_password:" + " ".join(exc.messages), None
    user = User.objects.create_user(
        email=email,
        password=password,
        first_name=first_name.strip(),
        last_name=last_name.strip(),
        username=_unique_username(email),
        role=User.Role.STUDENT,
    )
    _link(user, telegram_id, telegram_username)
    for course in Course.objects.filter(is_published=True, is_visible=True):
        CourseEnrollment.objects.get_or_create(student=user, course=course)
    return "ok", user
