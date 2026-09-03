from django.test import TestCase
from django.urls import reverse

from apps.access.premium import DEFAULT_PREMIUM_PRICE, format_sum, price_for_course
from apps.accounts.models import User
from tests.helpers import make_course, make_user


class PremiumOfferTests(TestCase):
    def setUp(self):
        self.student = make_user("prem@test.com", User.Role.STUDENT)
        self.course = make_course("sql", published=True, visible=True, title="SQL")

    def test_default_price(self):
        self.assertEqual(price_for_course("sql", course=self.course), 50_000)
        self.assertEqual(price_for_course("python"), DEFAULT_PREMIUM_PRICE)
        self.assertIn("50 000", format_sum(50_000))

    def test_admin_price_change_shows_on_page(self):
        self.course.premium_price = 75_000
        self.course.save(update_fields=["premium_price"])
        self.client.force_login(self.student)
        response = self.client.get(reverse("courses:premium", args=["sql"]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "75 000 so‘m")
        self.assertNotContains(response, "50 000 so‘m")

    def test_premium_page_content(self):
        self.client.force_login(self.student)
        response = self.client.get(reverse("courses:premium", args=["sql"]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "50 000 so‘m")
        self.assertContains(response, "9860 1201 4053 1134")
        self.assertContains(response, "Orzikulov Javokhir")
        self.assertContains(response, "@just_585")
        self.assertContains(response, "Uy vazifalari tekshirib boriladi")
        self.assertContains(response, "mentor izohlari")
        self.assertNotContains(response, "Kurslar narxi")
        self.assertNotContains(response, "Amaliy loyihalar")

    def test_premium_page_translates_to_russian(self):
        self.client.post(reverse("set_language"), {"language": "ru", "next": "/"})
        self.client.force_login(self.student)
        response = self.client.get(reverse("courses:premium", args=["sql"]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Почему Premium?")
        self.assertContains(response, "Инструкция по оплате")
        self.assertContains(response, "Номер карты")
        self.assertContains(response, "сум")
        self.assertNotContains(response, "Nima uchun Premium?")
        self.assertNotContains(response, "To‘lov yo‘riqnomasi")
