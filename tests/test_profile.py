from django.test import TestCase
from django.urls import reverse

from apps.accounts.models import User
from tests.helpers import make_user


class ProfileUpdateTests(TestCase):
    def setUp(self):
        self.user = make_user("student@test.com", User.Role.STUDENT, first_name="Ali", last_name="Valiyev")
        self.user.username = "ali_old"
        self.user.save(update_fields=["username"])

    def test_can_change_username_and_email(self):
        self.client.force_login(self.user)
        response = self.client.post(
            reverse("accounts:profile"),
            {
                "first_name": "Ali",
                "last_name": "Valiyev",
                "username": "ali_new",
                "email": "ali.new@test.com",
                "current_password": "",
                "new_password1": "",
                "new_password2": "",
            },
        )
        self.assertEqual(response.status_code, 302)
        self.user.refresh_from_db()
        self.assertEqual(self.user.username, "ali_new")
        self.assertEqual(self.user.email, "ali.new@test.com")

    def test_can_change_password(self):
        self.client.force_login(self.user)
        response = self.client.post(
            reverse("accounts:profile"),
            {
                "first_name": "Ali",
                "last_name": "Valiyev",
                "username": self.user.username,
                "email": self.user.email,
                "current_password": "StrongPass123!",
                "new_password1": "BrandNewPass99!",
                "new_password2": "BrandNewPass99!",
            },
        )
        self.assertEqual(response.status_code, 302)
        self.user.refresh_from_db()
        self.assertTrue(self.user.check_password("BrandNewPass99!"))

    def test_wrong_current_password_rejected(self):
        self.client.force_login(self.user)
        response = self.client.post(
            reverse("accounts:profile"),
            {
                "first_name": "Ali",
                "last_name": "Valiyev",
                "username": self.user.username,
                "email": self.user.email,
                "current_password": "WrongPass123!",
                "new_password1": "BrandNewPass99!",
                "new_password2": "BrandNewPass99!",
            },
        )
        self.assertEqual(response.status_code, 200)
        self.user.refresh_from_db()
        self.assertTrue(self.user.check_password("StrongPass123!"))
