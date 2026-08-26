"""
PythonAnywhere deployment settings.

Designed for:
- Free / Beginner accounts (SQLite for Django + SQLite SQL sandbox)
- Easy re-deploy when you add courses/features later
- Optional MySQL later via .env (PYTHONANYWHERE_USE_MYSQL=1)

Local development stays on config.settings.local — do not use this file for day-to-day coding.
"""

from pathlib import Path

from .base import *  # noqa: F403
from .base import BASE_DIR, env

DEBUG = env.bool("DEBUG", default=False)

# https://www.pythonanywhere.com/user/<username>/ → <username>.pythonanywhere.com
ALLOWED_HOSTS = env.list(
    "ALLOWED_HOSTS",
    default=[".pythonanywhere.com", "localhost", "127.0.0.1"],
)
CSRF_TRUSTED_ORIGINS = env.list(
    "CSRF_TRUSTED_ORIGINS",
    default=[],
)

# Prefer HTTPS on PythonAnywhere (force via env when custom domain is ready)
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
SECURE_SSL_REDIRECT = env.bool("SECURE_SSL_REDIRECT", default=True)
SESSION_COOKIE_SECURE = env.bool("SESSION_COOKIE_SECURE", default=True)
CSRF_COOKIE_SECURE = env.bool("CSRF_COOKIE_SECURE", default=True)
SECURE_HSTS_SECONDS = env.int("SECURE_HSTS_SECONDS", default=0)
SECURE_HSTS_INCLUDE_SUBDOMAINS = False
SECURE_HSTS_PRELOAD = False

if not SECRET_KEY or str(SECRET_KEY).startswith("insecure"):  # noqa: F405
    raise ValueError("Set a strong SECRET_KEY in the PythonAnywhere .env file.")

# --- Databases: SQLite by default (simple + free-tier friendly) ---
USE_MYSQL = env.bool("PYTHONANYWHERE_USE_MYSQL", default=False)

if USE_MYSQL:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.mysql",
            "NAME": env("MYSQL_DATABASE"),
            "USER": env("MYSQL_USER"),
            "PASSWORD": env("MYSQL_PASSWORD"),
            "HOST": env("MYSQL_HOST", default="USERNAME.mysql.pythonanywhere-services.com"),
            "PORT": env("MYSQL_PORT", default="3306"),
            "OPTIONS": {"charset": "utf8mb4"},
        }
    }
else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "pa_platform.sqlite3",
        }
    }

# SQL exercise sandbox — always a separate SQLite file (never the main DB)
SANDBOX_DATABASE = {
    "NAME": str(BASE_DIR / "pa_sandbox.sqlite3"),
    "USER": "",
    "PASSWORD": "",
    "HOST": "",
    "PORT": "",
    "ADMIN_USER": "",
    "ADMIN_PASSWORD": "",
    "ENGINE": "sqlite",
}

# Redis is optional on PA; fall back to local memory cache
REDIS_URL = env("REDIS_URL", default="")
if not REDIS_URL:
    CACHES = {
        "default": {
            "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
            "LOCATION": "pa-cache",
        }
    }

# Manifest storage is brittle while you iterate on CSS/JS; CompressedStaticFilesStorage is safer on PA
STORAGES = {
    "default": {"BACKEND": "django.contrib.files.storage.FileSystemStorage"},
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedStaticFilesStorage",
    },
}

# Serve /media/ from Django when PA Static Files mapping is not used (ok for homework .txt)
SERVE_MEDIA = env.bool("SERVE_MEDIA", default=True)

EMAIL_BACKEND = env(
    "EMAIL_BACKEND",
    default="django.core.mail.backends.console.EmailBackend",
)

# Keep logs readable in the PA error log
LOGGING["handlers"]["console"]["formatter"] = "console"  # noqa: F405
LOGGING["root"]["level"] = env("LOG_LEVEL", default="INFO")  # noqa: F405

# Data dir helpers (created at import time if missing)
Path(MEDIA_ROOT).mkdir(parents=True, exist_ok=True)  # noqa: F405
Path(STATIC_ROOT).mkdir(parents=True, exist_ok=True)  # noqa: F405
