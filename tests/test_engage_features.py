from datetime import timedelta

from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from apps.accounts.models import User
from apps.contests.models import Contest, ContestExercise
from apps.contests.services import contest_leaderboard, refresh_contest_score
from apps.exercises.models import Exercise, ExerciseAttempt, ExerciseComment
from apps.exercises.services import exercise_service
from apps.progress.models import StudentStreak
from apps.progress.streak import record_correct_solve
from apps.sandbox.datasets import seed_sandbox_database
from tests.helpers import make_course, make_exercise, make_lecture, make_module, make_user


class EngageFeaturesTests(TestCase):
    def setUp(self):
        seed_sandbox_database()
        self.student = make_user("engage@test.com", User.Role.STUDENT, first_name="Dilshod")
        self.course = make_course()
        self.module = make_module(self.course)
        self.lecture = make_lecture(self.module)
        self.exercise = make_exercise(self.module, lecture=self.lecture)

    def test_catalog_uzbek(self):
        self.client.force_login(self.student)
        response = self.client.get(reverse("exercises:catalog"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Mashqlar katalogi")
        self.assertContains(response, "Oson")
        self.assertContains(response, "Kurs")

    def test_catalog_sql_only_for_release(self):
        py_course = make_course("python", published=True, visible=True, title="Python")
        py_module = make_module(py_course, slug="py-asoslari", title="Python asoslari")
        make_exercise(py_module, slug="py-puzzle-1", title="Puzzle: AOV", lecture=None)
        self.client.force_login(self.student)
        all_page = self.client.get(reverse("exercises:catalog"))
        self.assertNotContains(all_page, "Puzzle: AOV")
        filtered = self.client.get(reverse("exercises:catalog"), {"course": "python"})
        self.assertNotContains(filtered, "Puzzle: AOV")

    def test_streak_increments_on_correct(self):
        exercise_service.run(self.student, self.exercise, "SELECT name FROM customers")
        streak = StudentStreak.objects.get(student=self.student)
        self.assertEqual(streak.current_streak, 1)
        record_correct_solve(self.student)
        streak.refresh_from_db()
        self.assertEqual(streak.current_streak, 1)

    def test_comment_and_editorial(self):
        self.exercise.editorial = "Bu yerda yechim yo‘riqnomasi."
        self.exercise.save(update_fields=["editorial"])
        exercise_service.run(self.student, self.exercise, "SELECT name FROM customers")
        self.client.force_login(self.student)
        page = self.client.get(reverse("exercises:detail", args=[self.exercise.pk]))
        self.assertContains(page, "Yechim yo‘riqnomasi")
        self.assertContains(page, "Muhokama")
        self.assertNotContains(page, "Yordamchi so‘rash")
        self.client.post(
            reverse("exercises:detail", args=[self.exercise.pk]),
            {"action": "comment", "body": "WHERE qayerga yoziladi?"},
        )
        self.assertEqual(ExerciseComment.objects.filter(exercise=self.exercise).count(), 1)

    def test_contest_leaderboard(self):
        now = timezone.now()
        contest = Contest.objects.create(
            title="Haftalik SQL",
            slug="test-contest",
            description="Sinov",
            starts_at=now - timedelta(days=1),
            ends_at=now + timedelta(days=2),
            is_published=True,
        )
        ContestExercise.objects.create(contest=contest, exercise=self.exercise, order=1)
        exercise_service.run(self.student, self.exercise, "SELECT name FROM customers")
        refresh_contest_score(contest, self.student)
        board = contest_leaderboard(contest)
        self.assertEqual(board[0]["name"], "Dilshod User")
        self.client.force_login(self.student)
        response = self.client.get(reverse("contests:detail", args=[contest.slug]))
        self.assertContains(response, "Musobaqa reytingi")

    def test_certificates_page(self):
        self.client.force_login(self.student)
        response = self.client.get(reverse("progress:certificates"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Sertifikatlarim")
