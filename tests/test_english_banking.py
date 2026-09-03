from django.test import TestCase
from django.urls import reverse

from apps.access.services import OPEN_COURSE_SLUGS, access_service
from apps.accounts.models import User
from apps.core.i18n.service import localize, localize_html, set_language
from apps.core.english_banking_content import build_english_banking_modules
from apps.core.english_banking_skill_tests import MODULE_SKILL_TESTS, skill_tests_for_module
from apps.courses.models import Course
from apps.exercises.models import Exercise
from tests.helpers import make_user


class EnglishBankingContentTests(TestCase):
    def test_modules_structure(self):
        modules = build_english_banking_modules()
        self.assertEqual(len(modules), 11)
        slugs = [m["slug"] for m in modules]
        self.assertTrue(all(s.startswith("eb-") for s in slugs))
        self.assertEqual(
            slugs,
            [
                "eb-bank-basics",
                "eb-accounts",
                "eb-cards-payments",
                "eb-loans-credit",
                "eb-fx-remittance",
                "eb-trade-sme",
                "eb-digital-fraud",
                "eb-hr-banking",
                "eb-customer-service",
                "eb-compliance-kyc",
                "eb-emails-meetings",
            ],
        )
        for module in modules:
            self.assertGreaterEqual(len(module["lectures"]), 2)
            self.assertTrue(module.get("exercises"))
            self.assertTrue(module.get("homework"))
            for lecture in module["lectures"]:
                self.assertTrue(lecture["slug"].startswith("eb-"))
                self.assertIn("<h2>", lecture["content"])
                self.assertRegex(lecture["content"], r"[A-Za-z]{4,}")

    def test_skill_tests_cover_all_modules(self):
        modules = build_english_banking_modules()
        for module in modules:
            quizzes = skill_tests_for_module(module["slug"])
            self.assertGreaterEqual(len(quizzes), 8, module["slug"])
            self.assertIn(module["slug"], MODULE_SKILL_TESTS)
            for q in quizzes:
                self.assertTrue(q["is_skill_test"])
                self.assertEqual(q["kind"], "quiz")
                self.assertEqual(len(q["quiz_options"]), 4)

    def test_course_is_open(self):
        self.assertIn("english-banking", OPEN_COURSE_SLUGS)
        self.assertIn("sql", OPEN_COURSE_SLUGS)

    def test_english_vocab_not_cyrillicized(self):
        set_language("uz-cyrl")
        option = "A) Know Your Customer"
        self.assertEqual(localize(option), option)
        title = "Welcome to the bank"
        self.assertEqual(localize(title), title)
        # Ellipsis / curly punctuation must not trigger fake Cyrillic transliteration.
        task = "A savings account is mainly for…"
        self.assertEqual(localize(task), task)
        self.assertNotIn("савингс", localize(task))
        self.assertEqual(localize("Branch = local office."), "Branch = local office.")
        self.assertEqual(localize("Client borrows."), "Client borrows.")
        self.assertEqual(localize("KYC"), "KYC")
        self.assertEqual(localize("Spread"), "Spread")

    def test_lecture_html_adds_ui_language_explain(self):
        html = "<h2>Lesson goal</h2><p>Learn KYC and AML words.</p><table><tr><th>Word</th><th>Meaning</th></tr><tr><td><strong>KYC (Know Your Customer)</strong></td><td>identifying and verifying the client</td></tr></table>"
        set_language("ru")
        out = localize_html(html, slug="eb-kyc")
        self.assertIn("Пояснение", out)
        self.assertIn("eb-lesson", out)
        self.assertIn("знай своего клиента", out.lower())
        self.assertIn("KYC", out)
        set_language("uz-cyrl")
        out_c = localize_html(html, slug="eb-kyc")
        self.assertIn("Тушунтириш", out_c)
        set_language("uz")
        out_uz = localize_html(html, slug="eb-kyc")
        self.assertIn("eb-lesson", out_uz)
        self.assertIn("Tushuntirish", out_uz)
        self.assertIn("mijozni bilish", out_uz.lower())

    def test_dialogue_translation_injected(self):
        html = (
            "<h2>Dialogue — Missing document</h2>"
            "<p><strong>Officer:</strong> Thank you for your application. "
            "I’m afraid we still need proof of address.<br>"
            "<strong>Customer:</strong> I don’t have it with me today.</p>"
            "<h2>Grammar focus</h2><p>Could you…?</p>"
        )
        set_language("ru")
        out = localize_html(html, slug="eb-polite-talk")
        self.assertIn("Перевод диалога", out)
        self.assertIn("eb-dialogue-tr", out)
        self.assertIn("подтверждение адреса", out)
        self.assertIn("Thank you for your application", out)
        set_language("uz")
        out_uz = localize_html(html, slug="eb-polite-talk")
        self.assertIn("Dialog tarjimasi", out_uz)
        self.assertIn("yashash manzili", out_uz.lower())


class EnglishBankingBootstrapTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        from django.core.management import call_command

        call_command("bootstrap_platform")

    def test_course_seeded_and_accessible(self):
        course = Course.objects.get(slug="english-banking")
        self.assertTrue(course.is_published)
        self.assertTrue(course.is_visible)
        self.assertEqual(course.modules.filter(is_published=True).count(), 11)
        student = make_user("eb-student@test.com", User.Role.STUDENT)
        first = course.modules.filter(is_published=True).order_by("order").first()
        self.assertTrue(access_service.can_access(student, first))

    def test_skill_tests_seeded(self):
        course = Course.objects.get(slug="english-banking")
        skill = Exercise.objects.filter(
            module__course=course,
            is_skill_test=True,
            is_published=True,
        )
        self.assertGreaterEqual(skill.count(), 88)

    def test_free_user_premium_modules_locked(self):
        free = make_user("qa-eb-lock@test.com", User.Role.STUDENT)
        course = Course.objects.get(slug="english-banking")
        mods = list(course.modules.filter(is_published=True).order_by("order"))
        self.assertEqual(len(mods), 11)
        for m in mods[:5]:
            self.assertTrue(access_service.can_access(free, m), m.slug)
            lec = m.lectures.filter(is_published=True).first()
            self.assertTrue(access_service.can_access(free, lec), lec.slug)
        for m in mods[5:]:
            self.assertFalse(access_service.can_access(free, m), m.slug)
            self.assertEqual(access_service.evaluate(free, m).code, "premium")
            lec = m.lectures.filter(is_published=True).first()
            self.assertFalse(access_service.can_access(free, lec), lec.slug)
            self.client.force_login(free)
            response = self.client.get(reverse("learning:lecture", args=[lec.pk]))
            self.assertEqual(response.status_code, 302)
            self.assertIn("/courses/english-banking/premium/", response.url)

    def test_course_detail_shows_premium_locks(self):
        free = make_user("qa-eb-detail@test.com", User.Role.STUDENT)
        self.client.force_login(free)
        response = self.client.get(reverse("courses:detail", args=["english-banking"]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "English for Banking")
        self.assertContains(response, "🔒")
        self.assertContains(response, "Dastlabki 5 modul ochiq")
