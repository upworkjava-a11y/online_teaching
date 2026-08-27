from datetime import timedelta

from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from apps.access.services import access_service
from apps.contests.models import Contest
from tests.helpers import make_course, make_exercise, make_lecture, make_module, make_user


class GuestAccessTests(TestCase):
    def setUp(self):
        self.course = make_course("sql")
        self.module = make_module(self.course, slug="sql-asoslari")
        self.lecture = make_lecture(self.module)
        self.exercise = make_exercise(self.module, lecture=self.lecture)

    def test_anonymous_user_has_role_helpers(self):
        from django.contrib.auth.models import AnonymousUser

        guest = AnonymousUser()
        self.assertFalse(guest.is_student)
        self.assertFalse(guest.is_teacher)
        self.assertFalse(guest.is_admin)
        self.assertFalse(guest.is_premium)
        self.assertFalse(guest.is_blocked)
        self.assertEqual(guest.role, "")

    def test_guest_can_open_courses(self):
        response = self.client.get(reverse("courses:list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Mehmon")
        self.assertContains(response, "Kirish")

    def test_guest_can_open_course_and_lecture(self):
        response = self.client.get(reverse("courses:detail", args=[self.course.slug]))
        self.assertEqual(response.status_code, 200)
        lecture = self.client.get(reverse("learning:lecture", args=[self.lecture.pk]))
        self.assertEqual(lecture.status_code, 200)
        self.assertContains(lecture, self.lecture.title)

    def test_guest_blocked_from_puzzle_with_gate(self):
        response = self.client.get(reverse("exercises:detail", args=[self.exercise.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Masalani yechish uchun hisob kerak")
        self.assertContains(response, "Tizimga kirish")
        self.assertContains(response, "Ro‘yxatdan o‘tish")

    def test_guest_blocked_from_homework(self):
        response = self.client.get(reverse("homework:list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Uy vazifasi uchun hisob kerak")

    def test_guest_can_browse_catalog(self):
        response = self.client.get(reverse("exercises:catalog"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Mashqlar katalogi")

    def test_guest_can_open_leaderboard(self):
        response = self.client.get(reverse("dashboard:leaderboard"))
        self.assertEqual(response.status_code, 200)

    def test_guest_can_open_contests(self):
        now = timezone.now()
        Contest.objects.create(
            title="Haftalik",
            slug="haftalik-test",
            starts_at=now - timedelta(days=1),
            ends_at=now + timedelta(days=6),
            is_published=True,
        )
        list_resp = self.client.get(reverse("contests:list"))
        self.assertEqual(list_resp.status_code, 200)
        detail = self.client.get(reverse("contests:detail", args=["haftalik-test"]))
        self.assertEqual(detail.status_code, 200)

    def test_guest_skill_test_requires_auth(self):
        response = self.client.get(reverse("exercises:skill_tests", args=[self.module.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Bilim testi uchun hisob kerak")

    def test_root_redirects_guest_to_courses(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 302)
        self.assertIn("/courses/", response.url)

    def test_guest_smoke_browse_paths_do_not_500(self):
        paths = [
            "/",
            reverse("courses:list"),
            reverse("courses:detail", args=[self.course.slug]),
            reverse("learning:lecture", args=[self.lecture.pk]),
            reverse("exercises:catalog"),
            reverse("dashboard:leaderboard"),
            reverse("contests:list"),
            reverse("accounts:login"),
            reverse("accounts:register"),
        ]
        for path in paths:
            with self.subTest(path=path):
                response = self.client.get(path, follow=True)
                self.assertLess(response.status_code, 500, msg=f"{path} returned {response.status_code}")

    def test_register_rejects_open_redirect(self):
        student = make_user("newstudent@example.com", password="StudentPass123!")
        # Ensure email is free — make_user already created; use unique
        from apps.accounts.models import User

        User.objects.filter(email="openredirect@example.com").delete()
        response = self.client.post(
            reverse("accounts:register") + "?next=//evil.example/phish",
            {
                "email": "openredirect@example.com",
                "first_name": "Test",
                "last_name": "User",
                "password1": "StudentPass123!",
                "password2": "StudentPass123!",
            },
        )
        self.assertEqual(response.status_code, 302)
        self.assertNotIn("evil.example", response.url)

    def test_premium_skill_test_blocked_for_free_student(self):
        student = make_user("free@example.com", password="StudentPass123!")
        # Create 6 published modules; skill test on 6th should be premium-locked
        modules = [self.module]
        for i in range(2, 7):
            modules.append(make_module(self.course, slug=f"sql-m{i}", order=i))
        premium_module = modules[-1]
        self.client.login(email="free@example.com", password="StudentPass123!")
        self.assertFalse(access_service.can_take_skill_test(student, premium_module))
        response = self.client.get(reverse("exercises:skill_tests", args=[premium_module.pk]))
        self.assertEqual(response.status_code, 403)

    def test_guest_post_exercise_shows_gate_not_500(self):
        response = self.client.post(reverse("exercises:detail", args=[self.exercise.pk]), {"sql": "SELECT 1"})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Masalani yechish uchun hisob kerak")
