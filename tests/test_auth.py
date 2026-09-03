from django.test import TestCase, override_settings
from django.urls import reverse

from apps.accounts.models import User


@override_settings(ROOT_URLCONF="config.urls")
class AuthenticationTests(TestCase):
    def test_register_creates_student(self):
        response = self.client.post(
            reverse("accounts:register"),
            {
                "first_name": "Ali",
                "last_name": "Valiyev",
                "email": "ali@example.com",
                "password1": "StrongPass123!",
                "password2": "StrongPass123!",
            },
        )
        self.assertEqual(response.status_code, 302)
        user = User.objects.get(email="ali@example.com")
        self.assertEqual(user.role, User.Role.STUDENT)
        self.assertTrue(user.check_password("StrongPass123!"))

    def test_register_shows_localized_password_errors_in_red(self):
        response = self.client.post(
            reverse("accounts:register"),
            {
                "first_name": "Ali",
                "last_name": "Valiyev",
                "email": "ali2@example.com",
                "password1": "123",
                "password2": "123",
            },
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'class="form-error')
        self.assertContains(response, "Parol juda qisqa")
        self.assertContains(response, "Bu parol juda oddiy")
        self.assertNotContains(response, "This password is too short")
        self.assertNotContains(response, "This password is too common")

    def test_register_password_errors_follow_language(self):
        self.client.post(reverse("set_language"), {"language": "ru", "next": "/"})
        response = self.client.post(
            reverse("accounts:register"),
            {
                "first_name": "Ali",
                "last_name": "Valiyev",
                "email": "ali3@example.com",
                "password1": "123",
                "password2": "123",
            },
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Пароль слишком короткий")
        self.assertContains(response, "Этот пароль слишком простой")
        self.assertNotContains(response, "This password is too short")
        self.assertNotContains(response, "This password is too common")

        self.client.post(reverse("set_language"), {"language": "en", "next": "/"})
        response = self.client.post(
            reverse("accounts:register"),
            {
                "first_name": "Ali",
                "last_name": "Valiyev",
                "email": "ali4@example.com",
                "password1": "123",
                "password2": "123",
            },
        )
        self.assertContains(response, "Password is too short")
        self.assertContains(response, "This password is too common")
        self.assertNotContains(response, "Parol juda qisqa")

    def test_login_success(self):
        User.objects.create_user(email="ali@example.com", password="StrongPass123!", username="ali")
        response = self.client.post(reverse("accounts:login"), {"username": "ali@example.com", "password": "StrongPass123!"})
        self.assertEqual(response.status_code, 302)

    def test_invalid_login(self):
        response = self.client.post(reverse("accounts:login"), {"username": "missing@example.com", "password": "wrong"})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Email yoki parol noto‘g‘ri")

    def test_logout(self):
        user = User.objects.create_user(email="ali@example.com", password="StrongPass123!", username="ali")
        self.client.force_login(user)
        response = self.client.post(reverse("accounts:logout"))
        self.assertEqual(response.status_code, 302)
