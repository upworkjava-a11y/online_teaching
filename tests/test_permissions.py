from django.test import TestCase
from django.urls import reverse

from apps.accounts.models import User
from tests.helpers import make_user


class PermissionTests(TestCase):
    def setUp(self):
        self.student = make_user("student@test.com", User.Role.STUDENT)
        self.teacher = make_user("teacher@test.com", User.Role.TEACHER)
        self.admin = make_user("admin@test.com", User.Role.ADMIN, is_staff=True, is_superuser=True)

    def test_student_reaches_dashboard(self):
        self.client.force_login(self.student)
        response = self.client.get(reverse("dashboard:home"))
        self.assertEqual(response.status_code, 200)

    def test_student_cannot_open_teacher_dashboard(self):
        self.client.force_login(self.student)
        response = self.client.get(reverse("analytics:dashboard"))
        self.assertEqual(response.status_code, 302)

    def test_teacher_reaches_teacher_dashboard(self):
        self.client.force_login(self.teacher)
        response = self.client.get(reverse("analytics:dashboard"))
        self.assertEqual(response.status_code, 200)

    def test_teacher_cannot_open_student_dashboard(self):
        self.client.force_login(self.teacher)
        response = self.client.get(reverse("dashboard:home"))
        self.assertEqual(response.status_code, 302)

    def test_admin_can_open_admin(self):
        self.client.force_login(self.admin)
        response = self.client.get("/admin/")
        self.assertEqual(response.status_code, 200)
