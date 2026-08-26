from dataclasses import dataclass

from django.contrib.contenttypes.models import ContentType

from apps.courses.models import Course, Lecture, Module

from .models import UserContentAccess

FREE_PREVIEW_MODULES = 3
PREMIUM_GROUP_NAME = "Premium"
# Talabalar uchun hozircha ochiq kurs(lar). Qolganlari “Hozir jarayonda”.
OPEN_COURSE_SLUGS = frozenset({"sql"})
COMING_SOON_REASON = "Hozir jarayonda"


@dataclass
class AccessDecision:
    allowed: bool
    reason: str
    code: str

    @property
    def is_blocked_for_user(self):
        return self.code == "blocked"

    @property
    def is_unpublished(self):
        return self.code == "unpublished"

    @property
    def is_premium_locked(self):
        return self.code == "premium"

    @property
    def is_coming_soon(self):
        return self.code == "coming_soon"


class AccessService:
    """
    Policy:
    1. BLOCKED rule always denies, even if content is published.
    2. ALLOWED rule can grant access to unpublished content for that user.
    3. Admins/teachers bypass student publication rules.
    4. Premium users (or ALLOWED on the course) get every published lesson.
    5. Other registered students get the first 3 published modules per course.
    """

    PREMIUM_REASON = "Bu modul premium. To‘liq kurs uchun admin Premium belgilashi kerak."

    def is_course_open(self, course: Course) -> bool:
        return course.slug in OPEN_COURSE_SLUGS

    def _rule(self, user, obj):
        ct = ContentType.objects.get_for_model(obj.__class__)
        return UserContentAccess.objects.filter(user=user, content_type=ct, object_id=obj.pk).first()

    def _parent_blocked(self, user, obj) -> UserContentAccess | None:
        if isinstance(obj, Lecture):
            return self._rule(user, obj.module) or self._rule(user, obj.module.course)
        if isinstance(obj, Module):
            return self._rule(user, obj.course)
        from apps.exercises.models import Exercise

        if isinstance(obj, Exercise):
            lecture_rule = self._rule(user, obj.lecture) if obj.lecture_id else None
            return lecture_rule or self._rule(user, obj.module) or self._rule(user, obj.module.course)
        return None

    def preview_module_ids(self, course: Course) -> set[int]:
        return set(
            Module.objects.filter(course=course, is_published=True)
            .order_by("order", "id")
            .values_list("id", flat=True)[:FREE_PREVIEW_MODULES]
        )

    def is_preview_module(self, module: Module) -> bool:
        return module.pk in self.preview_module_ids(module.course)

    def is_premium_user(self, user) -> bool:
        if getattr(user, "is_premium", False):
            return True
        if not getattr(user, "pk", None):
            return False
        return user.groups.filter(name__iexact=PREMIUM_GROUP_NAME).exists()

    def has_full_course_access(self, user, course: Course) -> bool:
        if not user.is_authenticated:
            return False
        if getattr(user, "is_blocked", False):
            return False
        if user.is_admin or user.is_teacher:
            return True
        if self.is_premium_user(user):
            return True
        rule = self._rule(user, course)
        return bool(rule and rule.status == UserContentAccess.Status.ALLOWED)

    def evaluate(self, user, obj) -> AccessDecision:
        if not user.is_authenticated:
            return AccessDecision(False, "Avval tizimga kiring.", "unauthenticated")
        if getattr(user, "is_blocked", False):
            return AccessDecision(False, "Hisobingiz bloklangan.", "account_blocked")
        if user.is_admin:
            return AccessDecision(True, "", "admin")
        if user.is_teacher:
            return AccessDecision(True, "", "teacher")

        from apps.exercises.models import Exercise

        # “Hozir jarayonda” kurslar — ALLOWED ham ochmaydi (faqat admin/teacher yuqorida o‘tdi)
        course_for_gate = None
        if isinstance(obj, Course):
            course_for_gate = obj
        elif isinstance(obj, Module):
            course_for_gate = obj.course
        elif isinstance(obj, Lecture):
            course_for_gate = obj.module.course
        elif isinstance(obj, Exercise):
            course_for_gate = obj.module.course
        if course_for_gate is not None and not self.is_course_open(course_for_gate):
            if course_for_gate.is_published and course_for_gate.is_visible:
                return AccessDecision(False, COMING_SOON_REASON, "coming_soon")
            return AccessDecision(False, "Bu kurs hozircha mavjud emas.", "unpublished")

        rule = self._rule(user, obj)
        if rule and rule.status == UserContentAccess.Status.BLOCKED:
            return AccessDecision(False, "Bu bo‘lim siz uchun hozircha yopilgan.", "blocked")

        parent_rule = self._parent_blocked(user, obj)
        if parent_rule and parent_rule.status == UserContentAccess.Status.BLOCKED:
            return AccessDecision(False, "Bu bo‘lim siz uchun hozircha yopilgan.", "blocked")

        if rule and rule.status == UserContentAccess.Status.ALLOWED:
            return AccessDecision(True, "", "explicit_allow")

        if isinstance(obj, Course):
            if obj.is_published and obj.is_visible:
                return AccessDecision(True, "", "published")
            return AccessDecision(False, "Bu kurs hozircha mavjud emas.", "unpublished")

        if isinstance(obj, Module):
            course_decision = self.evaluate(user, obj.course)
            if not course_decision.allowed:
                return course_decision
            if obj.is_published:
                return AccessDecision(True, "", "published")
            return AccessDecision(False, "Bu modul hozircha mavjud emas.", "unpublished")

        if isinstance(obj, Lecture):
            module_decision = self.evaluate(user, obj.module)
            if not module_decision.allowed:
                return module_decision
            if not obj.is_published:
                return AccessDecision(False, "Bu ma’ruza hozircha mavjud emas.", "unpublished")
            if self.has_full_course_access(user, obj.course):
                return AccessDecision(True, "", "full")
            module_rule = self._rule(user, obj.module)
            if module_rule and module_rule.status == UserContentAccess.Status.ALLOWED:
                return AccessDecision(True, "", "explicit_allow")
            if self.is_preview_module(obj.module):
                return AccessDecision(True, "", "preview")
            return AccessDecision(False, self.PREMIUM_REASON, "premium")

        if isinstance(obj, Exercise):
            if obj.lecture_id:
                return self.evaluate(user, obj.lecture)
            module_decision = self.evaluate(user, obj.module)
            if not module_decision.allowed:
                return module_decision
            if not obj.is_published:
                return AccessDecision(False, "Bu mashq hozircha mavjud emas.", "unpublished")
            if self.has_full_course_access(user, obj.module.course):
                return AccessDecision(True, "", "full")
            module_rule = self._rule(user, obj.module)
            if module_rule and module_rule.status == UserContentAccess.Status.ALLOWED:
                return AccessDecision(True, "", "explicit_allow")
            if self.is_preview_module(obj.module):
                return AccessDecision(True, "", "preview")
            return AccessDecision(False, self.PREMIUM_REASON, "premium")

        if getattr(obj, "is_published", False):
            return AccessDecision(True, "", "published")
        return AccessDecision(False, "Bu kontent hozircha mavjud emas.", "unpublished")

    def can_access(self, user, obj) -> bool:
        return self.evaluate(user, obj).allowed


access_service = AccessService()
