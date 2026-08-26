from unittest.mock import patch

from django.test import TestCase, override_settings
from django.urls import reverse

from apps.accounts.google import GoogleProfile, login_or_register_google
from apps.accounts.models import GoogleAccount, User


GOOGLE_SETTINGS = {
    "GOOGLE_CLIENT_ID": "test-google-client-id",
    "GOOGLE_CLIENT_SECRET": "test-google-client-secret",
    "GOOGLE_OAUTH_REDIRECT_URI": "http://testserver/accounts/google/callback/",
}


def google_profile(**kwargs):
    data = {
        "sub": "google-sub-1",
        "email": "ali.google@example.com",
        "email_verified": True,
        "given_name": "Ali",
        "family_name": "Valiyev",
    }
    data.update(kwargs)
    return GoogleProfile(**data)


@override_settings(**GOOGLE_SETTINGS)
class GoogleOAuthTests(TestCase):
    def test_login_page_hides_google_button(self):
        response = self.client.get(reverse("accounts:login"))
        self.assertNotContains(response, "Google orqali kirish")
        self.assertNotContains(response, reverse("accounts:google_login"))

    def test_register_page_hides_google_button(self):
        response = self.client.get(reverse("accounts:register"))
        self.assertNotContains(response, "Google orqali ro‘yxatdan o‘tish")
        self.assertNotContains(response, reverse("accounts:google_login"))

    @patch("apps.accounts.views.verify_google_id_token")
    def test_token_registers_student_from_account_picker(self, mocked):
        mocked.return_value = google_profile()
        response = self.client.post(reverse("accounts:google_token"), {"credential": "fake.google.jwt"})
        self.assertEqual(response.status_code, 302)
        user = User.objects.get(email="ali.google@example.com")
        self.assertEqual(user.role, User.Role.STUDENT)
        self.assertEqual(int(self.client.session["_auth_user_id"]), user.pk)

    @patch("apps.accounts.views.verify_google_id_token")
    def test_token_logs_in_existing_account(self, mocked):
        existing = User.objects.create_user(
            email="ali.google@example.com",
            password="StrongPass123!",
            username="aligoogle",
        )
        mocked.return_value = google_profile()
        response = self.client.post(reverse("accounts:google_token"), {"credential": "fake.google.jwt"})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(User.objects.filter(email="ali.google@example.com").count(), 1)
        self.assertEqual(GoogleAccount.objects.get(user=existing).google_sub, "google-sub-1")

    def test_start_redirects_to_google(self):
        response = self.client.get(reverse("accounts:google_login"))
        self.assertEqual(response.status_code, 302)
        self.assertIn("accounts.google.com", response["Location"])
        self.assertIn("client_id=test-google-client-id", response["Location"])
        self.assertTrue(self.client.session.get("google_oauth_state"))

    def test_callback_rejects_invalid_state(self):
        session = self.client.session
        session["google_oauth_state"] = "expected-state"
        session.save()
        response = self.client.get(reverse("accounts:google_callback"), {"code": "abc", "state": "wrong"})
        self.assertEqual(response.status_code, 302)
        self.assertFalse(User.objects.filter(email="ali.google@example.com").exists())

    @patch("apps.accounts.views.fetch_google_profile")
    def test_callback_registers_student(self, mocked):
        mocked.return_value = google_profile()
        session = self.client.session
        session["google_oauth_state"] = "state-1"
        session.save()
        response = self.client.get(reverse("accounts:google_callback"), {"code": "valid-code", "state": "state-1"})
        self.assertEqual(response.status_code, 302)
        user = User.objects.get(email="ali.google@example.com")
        self.assertEqual(user.role, User.Role.STUDENT)
        self.assertFalse(user.has_usable_password())
        self.assertEqual(user.google_account.google_sub, "google-sub-1")
        self.assertEqual(int(self.client.session["_auth_user_id"]), user.pk)

    @patch("apps.accounts.views.fetch_google_profile")
    def test_callback_logs_in_existing_email(self, mocked):
        existing = User.objects.create_user(
            email="ali.google@example.com",
            password="StrongPass123!",
            username="aligoogle",
            first_name="Ali",
        )
        mocked.return_value = google_profile()
        session = self.client.session
        session["google_oauth_state"] = "state-2"
        session.save()
        response = self.client.get(reverse("accounts:google_callback"), {"code": "valid-code", "state": "state-2"})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(User.objects.filter(email="ali.google@example.com").count(), 1)
        self.assertEqual(GoogleAccount.objects.get(user=existing).google_sub, "google-sub-1")

    def test_unverified_email_rejected(self):
        from apps.accounts.google import GoogleOAuthError
        from django.test import RequestFactory

        request = RequestFactory().get("/")
        with self.assertRaises(GoogleOAuthError):
            login_or_register_google(request, google_profile(email_verified=False))
        self.assertFalse(User.objects.filter(email="ali.google@example.com").exists())

    def test_blocked_user_cannot_use_google(self):
        from apps.accounts.google import GoogleOAuthError
        from django.test import RequestFactory

        user = User.objects.create_user(
            email="ali.google@example.com",
            password="StrongPass123!",
            username="blocked",
            is_blocked=True,
        )
        GoogleAccount.objects.create(user=user, google_sub="google-sub-1", email=user.email)
        request = RequestFactory().get("/")
        with self.assertRaises(GoogleOAuthError):
            login_or_register_google(request, google_profile())


@override_settings(GOOGLE_CLIENT_ID="", GOOGLE_CLIENT_SECRET="", GOOGLE_OAUTH_REDIRECT_URI="")
class GoogleOAuthDisabledTests(TestCase):
    def test_buttons_hidden_without_credentials(self):
        login_page = self.client.get(reverse("accounts:login"))
        register_page = self.client.get(reverse("accounts:register"))
        self.assertNotContains(login_page, "Google orqali kirish")
        self.assertNotContains(register_page, "Google orqali ro‘yxatdan o‘tish")

    def test_start_without_credentials(self):
        response = self.client.get(reverse("accounts:google_login") + "?from=register", follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Google Cloud")
