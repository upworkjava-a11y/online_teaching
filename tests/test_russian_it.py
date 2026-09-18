"""Русский для IT — structure, i18n, bootstrap, and freemium access tests."""

from django.test import TestCase
from django.urls import reverse

from apps.access.services import OPEN_COURSE_SLUGS, access_service
from apps.accounts.models import User
from apps.core.i18n.languages import LANG_UZ
from apps.core.i18n.service import localize_html, set_language
from apps.core.russian_it_content import build_russian_it_modules
from apps.core.russian_it_skill_tests import MODULE_SKILL_TESTS, skill_tests_for_module
from apps.courses.models import Course
from apps.exercises.models import Exercise
from tests.helpers import make_user


class RussianITContentTests(TestCase):
    def test_module_shape(self):
        modules = build_russian_it_modules()
        self.assertEqual(len(modules), 17)
        self.assertEqual([m["order"] for m in modules], list(range(1, 18)))
        for m in modules:
            self.assertTrue(m["slug"].startswith("rit-"))
            self.assertEqual(len(m["lectures"]), 3)
            self.assertTrue(m["homework"])
            self.assertTrue(m["practice"])
            self.assertTrue(m["exercises"])
            for lec in m["lectures"]:
                self.assertTrue(lec["slug"].startswith("rit-"))
                self.assertIn("Lesson goal", lec["content"])
                self.assertIn("Key vocabulary", lec["content"])
                self.assertTrue(
                    "Academic / study tip" in lec["content"]
                    or "Collocations & useful chunks" in lec["content"]
                    or m["slug"] in {"rit-academic", "rit-interview"}
                )

    def test_academic_and_interview_modules(self):
        modules = {m["slug"]: m for m in build_russian_it_modules()}
        self.assertIn("rit-academic", modules)
        self.assertIn("rit-interview", modules)
        self.assertEqual(modules["rit-academic"]["order"], 16)
        self.assertEqual(modules["rit-interview"]["order"], 17)

    def test_skill_tests_complete(self):
        modules = build_russian_it_modules()
        for m in modules:
            quizzes = skill_tests_for_module(m["slug"])
            self.assertGreaterEqual(len(quizzes), 8, m["slug"])
            self.assertEqual(len(MODULE_SKILL_TESTS[m["slug"]]), 8)
        self.assertEqual(sum(len(v) for v in MODULE_SKILL_TESTS.values()), 136)

    def test_open_course_slug(self):
        self.assertIn("russian-it", OPEN_COURSE_SLUGS)

    def test_localize_html_rit_wrapper(self):
        set_language(LANG_UZ)
        html = "<h2>Lesson goal</h2><p>Изучите IT-русский.</p><h2>Key vocabulary</h2>"
        out = localize_html(html, slug="rit-welcome-it")
        self.assertIn("rit-lesson", out)
        self.assertIn("rit-banner", out)
        self.assertIn("rit-h", out)
        self.assertIn("rit-explain", out)
        self.assertIn("IT ruschasini", out)

    def test_module1_has_visuals(self):
        modules = {m["slug"]: m for m in build_russian_it_modules()}
        first = modules["rit-it-basics"]
        joined = "\n".join(lec["content"] for lec in first["lectures"])
        self.assertIn("/static/course_media/russian-it/", joined)
        self.assertIn("lang-fig", joined)
        self.assertIn("esp-timeline", joined)
        self.assertIn("esp-cards", joined)


class RussianITBootstrapTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        from django.core.management import call_command

        call_command("bootstrap_platform")

    def test_course_seeded(self):
        course = Course.objects.get(slug="russian-it")
        self.assertTrue(course.is_published)
        self.assertTrue(course.is_visible)
        self.assertEqual(course.modules.filter(is_published=True).count(), 17)
        skill = Exercise.objects.filter(
            module__course=course, is_skill_test=True, is_published=True
        ).count()
        self.assertGreaterEqual(skill, 136)

    def test_free_preview_first_module_only(self):
        course = Course.objects.get(slug="russian-it")
        student = make_user("rit-free@example.com", User.Role.STUDENT)
        modules = list(course.modules.filter(is_published=True).order_by("order"))
        self.assertEqual(len(modules), 17)
        self.assertEqual(access_service.free_preview_count(course), 1)
        self.assertTrue(access_service.can_access(student, modules[0]), modules[0].slug)
        for mod in modules[1:]:
            self.assertFalse(access_service.can_access(student, mod), mod.slug)
            self.assertEqual(access_service.evaluate(student, mod).code, "premium")

    def test_premium_redirect(self):
        course = Course.objects.get(slug="russian-it")
        student = make_user("rit-lock@example.com", User.Role.STUDENT)
        locked = course.modules.filter(is_published=True).order_by("order")[1]
        lecture = locked.lectures.filter(is_published=True).first()
        self.client.force_login(student)
        response = self.client.get(reverse("learning:lecture", args=[lecture.pk]))
        self.assertEqual(response.status_code, 302)
        self.assertIn("/courses/russian-it/premium/", response.url)
