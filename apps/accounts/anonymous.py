"""Mehmon (AnonymousUser) uchun User bilan mos xavfsiz atributlar."""

from django.contrib.auth.models import AnonymousUser


def patch_anonymous_user() -> None:
    if getattr(AnonymousUser, "_platform_role_patched", False):
        return

    AnonymousUser.role = ""
    AnonymousUser.is_blocked = False
    AnonymousUser.is_premium = False

    @property
    def is_student(self):
        return False

    @property
    def is_teacher(self):
        return False

    @property
    def is_admin(self):
        return False

    AnonymousUser.is_student = is_student
    AnonymousUser.is_teacher = is_teacher
    AnonymousUser.is_admin = is_admin
    AnonymousUser._platform_role_patched = True
