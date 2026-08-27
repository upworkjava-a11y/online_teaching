from django.apps import AppConfig


class AccountsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.accounts"
    verbose_name = "Foydalanuvchilar"

    def ready(self):
        from . import signals  # noqa: F401
        from .anonymous import patch_anonymous_user

        patch_anonymous_user()
