from django.core import mail
from django.test import TestCase, override_settings
from django.urls import reverse

from apps.accounts.models import User
from tests.helpers import make_user


@override_settings(
    EMAIL_BACKEND="django.core.mail.backends.locmem.EmailBackend",
    DEFAULT_FROM_EMAIL="noreply@test.local",
)
class PasswordResetTests(TestCase):
    def setUp(self):
        self.user = make_user("resetme@test.com", User.Role.STUDENT, password="OldPass123!")

    def test_reset_link_on_login(self):
        response = self.client.get(reverse("accounts:login"))
        self.assertContains(response, reverse("accounts:password_reset"))

    def test_password_reset_sends_email(self):
        response = self.client.post(
            reverse("accounts:password_reset"),
            {"email": "resetme@test.com"},
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(len(mail.outbox), 1)
        self.assertIn("parol", mail.outbox[0].subject.lower())
        self.assertIn("parolni-tiklash", mail.outbox[0].body)

    def test_unknown_email_still_shows_done(self):
        response = self.client.post(
            reverse("accounts:password_reset"),
            {"email": "nobody@test.com"},
            follow=True,
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(mail.outbox), 0)
        self.assertContains(response, "Tekshirib ko‘ring")
