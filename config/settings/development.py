from .base import *  # noqa: F403
from .base import BASE_DIR, DATABASES, SANDBOX_DATABASE
import socket

DEBUG = True
ALLOWED_HOSTS = ["localhost", "127.0.0.1", "web", "0.0.0.0"]
CSRF_TRUSTED_ORIGINS = [
    "http://localhost",
    "http://127.0.0.1",
    "http://localhost:8000",
    "http://127.0.0.1:8000",
]

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

STORAGES["staticfiles"] = {  # noqa: F405
    "BACKEND": "django.contrib.staticfiles.storage.StaticFilesStorage",
}

SECURE_SSL_REDIRECT = False
SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False


def _host_resolves(host: str) -> bool:
    if not host:
        return False
    try:
        socket.getaddrinfo(host, None)
        return True
    except OSError:
        return False


if not _host_resolves(DATABASES["default"].get("HOST", "")):
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "local_platform.sqlite3",
        }
    }
    SANDBOX_DATABASE = {
        "NAME": str(BASE_DIR / "local_sandbox.sqlite3"),
        "USER": "",
        "PASSWORD": "",
        "HOST": "",
        "PORT": "",
        "ADMIN_USER": "",
        "ADMIN_PASSWORD": "",
        "ENGINE": "sqlite",
    }
    CACHES = {
        "default": {
            "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
            "LOCATION": "dev-cache",
        }
    }
    REDIS_URL = ""
