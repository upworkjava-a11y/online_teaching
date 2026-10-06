from django.apps import AppConfig


class BadgesConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.badges"
    verbose_name = "Yutuqlar (badges)"

    def ready(self):
        from . import signals  # noqa: F401
