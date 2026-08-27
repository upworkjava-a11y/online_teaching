import os
from pathlib import Path

import environ

BASE_DIR = Path(__file__).resolve().parent.parent.parent

env = environ.Env(
    DEBUG=(bool, False),
    ALLOWED_HOSTS=(list, ["localhost", "127.0.0.1"]),
    CSRF_TRUSTED_ORIGINS=(list, []),
    SECURE_SSL_REDIRECT=(bool, False),
    SESSION_COOKIE_SECURE=(bool, False),
    CSRF_COOKIE_SECURE=(bool, False),
    SANDBOX_QUERY_TIMEOUT_SECONDS=(int, 5),
    SANDBOX_MAX_ROWS=(int, 200),
    SANDBOX_MAX_QUERY_CHARS=(int, 8000),
    MAX_HOMEWORK_UPLOAD_MB=(int, 1),
    SQL_RATE_LIMIT_PER_MINUTE=(int, 20),
)

_settings_module = os.environ.get("DJANGO_SETTINGS_MODULE")
environ.Env.read_env(BASE_DIR / ".env", overwrite=True)
if _settings_module:
    os.environ["DJANGO_SETTINGS_MODULE"] = _settings_module

SECRET_KEY = env("SECRET_KEY", default="insecure-dev-key-change-me")
DEBUG = env("DEBUG")
ALLOWED_HOSTS = env("ALLOWED_HOSTS")
CSRF_TRUSTED_ORIGINS = env("CSRF_TRUSTED_ORIGINS")

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django_htmx",
    "apps.core.apps.CoreConfig",
    "apps.accounts.apps.AccountsConfig",
    "apps.courses.apps.CoursesConfig",
    "apps.access.apps.AccessConfig",
    "apps.progress.apps.ProgressConfig",
    "apps.sandbox.apps.SandboxConfig",
    "apps.exercises.apps.ExercisesConfig",
    "apps.homework.apps.HomeworkConfig",
    "apps.learning.apps.LearningConfig",
    "apps.dashboard.apps.DashboardConfig",
    "apps.analytics.apps.AnalyticsConfig",
    "apps.contests.apps.ContestsConfig",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django_htmx.middleware.HtmxMiddleware",
    "apps.core.middleware.RequestLoggingMiddleware",
    "apps.accounts.middleware.LastActivityMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "config.urls"
WSGI_APPLICATION = "config.wsgi.application"
ASGI_APPLICATION = "config.asgi.application"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "apps.core.context_processors.platform",
            ],
        },
    }
]

AUTH_USER_MODEL = "accounts.User"
AUTHENTICATION_BACKENDS = ["django.contrib.auth.backends.ModelBackend"]
LOGIN_URL = "accounts:login"
LOGIN_REDIRECT_URL = "root"
LOGOUT_REDIRECT_URL = "courses:list"

AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator", "OPTIONS": {"min_length": 10}},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

PASSWORD_HASHERS = [
    "django.contrib.auth.hashers.Argon2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2PasswordHasher",
]

LANGUAGE_CODE = "uz"
TIME_ZONE = "Asia/Tashkent"
USE_I18N = True
USE_TZ = True

STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_DIRS = [BASE_DIR / "static"]
STORAGES = {
    "default": {"BACKEND": "django.core.files.storage.FileSystemStorage"},
    "staticfiles": {"BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage"},
}

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": env("POSTGRES_DB", default="analytics_edu"),
        "USER": env("POSTGRES_USER", default="analytics_user"),
        "PASSWORD": env("POSTGRES_PASSWORD", default="change-me-db-password"),
        "HOST": env("POSTGRES_HOST", default="db"),
        "PORT": env("POSTGRES_PORT", default="5432"),
        "CONN_MAX_AGE": 60,
        "OPTIONS": {"connect_timeout": 10},
    }
}

SANDBOX_DATABASE = {
    "NAME": env("SANDBOX_DB", default="sql_sandbox"),
    "USER": env("SANDBOX_USER", default="sandbox_reader"),
    "PASSWORD": env("SANDBOX_PASSWORD", default="change-me-sandbox-password"),
    "HOST": env("SANDBOX_HOST", default="sandbox-db"),
    "PORT": env("SANDBOX_PORT", default="5432"),
    "ADMIN_USER": env("SANDBOX_ADMIN_USER", default="sandbox_admin"),
    "ADMIN_PASSWORD": env("SANDBOX_ADMIN_PASSWORD", default="change-me-sandbox-admin-password"),
}

SANDBOX_QUERY_TIMEOUT_SECONDS = env("SANDBOX_QUERY_TIMEOUT_SECONDS")
SANDBOX_MAX_ROWS = env("SANDBOX_MAX_ROWS")
SANDBOX_MAX_QUERY_CHARS = env("SANDBOX_MAX_QUERY_CHARS")
SQL_RATE_LIMIT_PER_MINUTE = env("SQL_RATE_LIMIT_PER_MINUTE")
MAX_HOMEWORK_UPLOAD_MB = env("MAX_HOMEWORK_UPLOAD_MB")

REDIS_URL = env("REDIS_URL", default="")

CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
        "LOCATION": "analytics-edu",
    }
}

if REDIS_URL:
    CACHES["default"] = {
        "BACKEND": "django.core.cache.backends.redis.RedisCache",
        "LOCATION": REDIS_URL,
    }

SESSION_ENGINE = "django.contrib.sessions.backends.cached_db"
SESSION_COOKIE_HTTPONLY = True
SESSION_COOKIE_SAMESITE = "Lax"
CSRF_COOKIE_HTTPONLY = True
CSRF_COOKIE_SAMESITE = "Lax"
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_REFERRER_POLICY = "strict-origin-when-cross-origin"
X_FRAME_OPTIONS = "DENY"

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "json": {
            "()": "pythonjsonlogger.json.JsonFormatter",
            "fmt": "%(asctime)s %(levelname)s %(name)s %(message)s %(pathname)s %(lineno)d",
        },
        "console": {
            "format": "[{asctime}] {levelname} {name}: {message}",
            "style": "{",
        },
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "console",
        }
    },
    "root": {"handlers": ["console"], "level": "INFO"},
    "loggers": {
        "django.security": {"handlers": ["console"], "level": "WARNING", "propagate": False},
        "apps": {"handlers": ["console"], "level": "INFO", "propagate": False},
    },
}

PLATFORM_NAME = "Code with me"
PLATFORM_MOTTO = "Data analitikani biz bilan o‘rganing"
PLATFORM_TAGLINE = "Code with me o‘quv platformasi"
TELEGRAM_CHANNEL_URL = "https://t.me/code_with_javohir"
TELEGRAM_CHANNEL_LABEL = "Kanalga o‘tish"

GOOGLE_CLIENT_ID = env("GOOGLE_CLIENT_ID", default="")
GOOGLE_CLIENT_SECRET = env("GOOGLE_CLIENT_SECRET", default="")
GOOGLE_OAUTH_REDIRECT_URI = env("GOOGLE_OAUTH_REDIRECT_URI", default="")
