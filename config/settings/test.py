from .base import *  # noqa: F403

DEBUG = True
SECRET_KEY = "test-secret-key-not-for-production"
ALLOWED_HOSTS = ["testserver", "localhost", "127.0.0.1"]

DATABASES = {  # noqa: F405
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "test_platform.sqlite3",  # noqa: F405
    }
}

SANDBOX_DATABASE = {  # noqa: F405
    "NAME": str(BASE_DIR / "test_sandbox.sqlite3"),  # noqa: F405
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
        "LOCATION": "test-cache",
    }
}

PASSWORD_HASHERS = ["django.contrib.auth.hashers.MD5PasswordHasher"]
EMAIL_BACKEND = "django.core.mail.backends.locmem.EmailBackend"

# Ignore real .env Google credentials so disabled-OAuth tests stay deterministic.
GOOGLE_CLIENT_ID = ""
GOOGLE_CLIENT_SECRET = ""
GOOGLE_OAUTH_REDIRECT_URI = ""
STORAGES["staticfiles"] = {  # noqa: F405
    "BACKEND": "django.contrib.staticfiles.storage.StaticFilesStorage",
}
MEDIA_ROOT = BASE_DIR / "test_media"  # noqa: F405
SANDBOX_QUERY_TIMEOUT_SECONDS = 2
SQL_RATE_LIMIT_PER_MINUTE = 1000
