from .models import User


def unique_username_from_email(email: str) -> str:
    base = (email.split("@")[0] or "user")[:120]
    username = base
    suffix = 1
    while User.objects.filter(username=username).exists():
        suffix += 1
        username = f"{base}{suffix}"
    return username
