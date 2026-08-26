from .base import *  # noqa: F403
from .base import BASE_DIR

DEBUG = True
ALLOWED_HOSTS = ["localhost", "127.0.0.1", "testserver"]
CSRF_TRUSTED_ORIGINS = [
    "http://localhost",
    "http://127.0.0.1",
    "http://localhost:8000",
    "http://127.0.0.1:8000",
]

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
        "LOCATION": "local-cache",
    }
}

REDIS_URL = ""
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
STORAGES["staticfiles"] = {  # noqa: F405
    "BACKEND": "django.contrib.staticfiles.storage.StaticFilesStorage",
}
SECURE_SSL_REDIRECT = False
SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False
