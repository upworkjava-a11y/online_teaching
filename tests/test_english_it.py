"""English for IT — structure, i18n, bootstrap, and freemium access tests."""

from django.test import TestCase
from django.urls import reverse

from apps.access.services import OPEN_COURSE_SLUGS, access_service
from apps.accounts.models import User
from apps.core.english_it_content import build_english_it_modules
from apps.core.english_it_skill_tests import MODULE_SKILL_TESTS, skill_tests_for_module
from apps.core.i18n.languages import LANG_CYRL, LANG_UZ
from apps.core.i18n.service import localize, localize_html, set_language
from apps.courses.models import Course
from apps.exercises.models import Exercise
from tests.helpers import make_user


class EnglishITContentTests(TestCase):
    def test_module_shape(self):
        modules = build_english_it_modules()
        self.assertEqual(len(modules), 17)
        self.assertEqual([m["order"] for m in modules], list(range(1, 18)))
        for m in modules:
            self.assertTrue(m["slug"].startswith("eit-"))
            self.assertEqual(len(m["lectures"]), 3)
            self.assertTrue(m["homework"])
            self.assertTrue(m["practice"])
            self.assertTrue(m["exercises"])
            for lec in m["lectures"]:
                self.assertTrue(lec["slug"].startswith("eit-"))
                self.assertIn("Lesson goal", lec["content"])
                self.assertIn("Key vocabulary", lec["content"])
                # Enhanced workplace lessons (and academic/interview) include study support
                self.assertTrue(
                    "Academic / study tip" in lec["content"]
                    or "Collocations & useful chunks" in lec["content"]
                    or m["slug"] in {"eit-academic", "eit-interview"}
                )

    def test_academic_and_interview_modules(self):
        modules = {m["slug"]: m for m in build_english_it_modules()}
        self.assertIn("eit-academic", modules)
        self.assertIn("eit-interview", modules)
        self.assertEqual(modules["eit-academic"]["order"], 16)
        self.assertEqual(modules["eit-interview"]["order"], 17)
        academic = modules["eit-academic"]
        slugs = [l["slug"] for l in academic["lectures"]]
        self.assertEqual(
            slugs,
            ["eit-academic-abstracts", "eit-academic-writing", "eit-academic-presentations"],
        )

    def test_skill_tests_complete(self):
        modules = build_english_it_modules()
        for m in modules:
            quizzes = skill_tests_for_module(m["slug"])
            self.assertGreaterEqual(len(quizzes), 8, m["slug"])
            self.assertEqual(len(MODULE_SKILL_TESTS[m["slug"]]), 8)
        self.assertEqual(sum(len(v) for v in MODULE_SKILL_TESTS.values()), 136)

    def test_open_course_slug(self):
        self.assertIn("english-it", OPEN_COURSE_SLUGS)
        self.assertIn("english-banking", OPEN_COURSE_SLUGS)
        self.assertIn("russian-it", OPEN_COURSE_SLUGS)

    def test_english_stays_latin_under_cyrillic(self):
        set_language(LANG_CYRL)
        task = "A pull request is mainly for…"
        self.assertEqual(localize(task), task)
        self.assertNotIn("пулл", localize("Pull request"))
        self.assertEqual(localize("Bug"), "Bug")

    def test_localize_html_eit_wrapper(self):
        set_language(LANG_UZ)
        html = "<h2>Lesson goal</h2><p>Learn IT English.</p><h2>Key vocabulary</h2>"
        out = localize_html(html, slug="eit-welcome-it")
        self.assertIn("eit-lesson", out)
        self.assertIn("eit-banner", out)
        self.assertIn("eit-h", out)
        self.assertIn("eit-explain", out)
        self.assertIn("IT inglizchasini", out)

    def test_module1_has_visuals(self):
        modules = {m["slug"]: m for m in build_english_it_modules()}
        first = modules["eit-it-basics"]
        joined = "\n".join(lec["content"] for lec in first["lectures"])
        self.assertIn("/static/course_media/english-it/", joined)
        self.assertIn("lang-fig", joined)
        self.assertIn("esp-timeline", joined)
        self.assertIn("esp-cards", joined)


class EnglishITBootstrapTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        from django.core.management import call_command

        call_command("bootstrap_platform")

    def test_course_seeded(self):
        course = Course.objects.get(slug="english-it")
        self.assertTrue(course.is_published)
        self.assertTrue(course.is_visible)
        self.assertEqual(course.modules.filter(is_published=True).count(), 17)
        skill = Exercise.objects.filter(
            module__course=course, is_skill_test=True, is_published=True
        ).count()
        self.assertGreaterEqual(skill, 136)

    def test_free_preview_first_module_only(self):
        course = Course.objects.get(slug="english-it")
        student = make_user("eit-free@example.com", User.Role.STUDENT)
        modules = list(course.modules.filter(is_published=True).order_by("order"))
        self.assertEqual(len(modules), 17)
        self.assertEqual(access_service.free_preview_count(course), 1)
        self.assertTrue(access_service.can_access(student, modules[0]), modules[0].slug)
        for mod in modules[1:]:
            self.assertFalse(access_service.can_access(student, mod), mod.slug)
            self.assertEqual(access_service.evaluate(student, mod).code, "premium")

    def test_premium_redirect(self):
        course = Course.objects.get(slug="english-it")
        student = make_user("eit-lock@example.com", User.Role.STUDENT)
        locked = course.modules.filter(is_published=True).order_by("order")[1]
        lecture = locked.lectures.filter(is_published=True).first()
        self.client.force_login(student)
        response = self.client.get(reverse("learning:lecture", args=[lecture.pk]))
        self.assertEqual(response.status_code, 302)
        self.assertIn("/courses/english-it/premium/", response.url)
