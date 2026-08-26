from django.test import TestCase
from django.urls import reverse

from apps.accounts.models import User
from apps.exercises.models import ExerciseAttempt
from apps.exercises.services import exercise_service
from apps.sandbox.datasets import seed_sandbox_database
from tests.helpers import make_course, make_exercise, make_lecture, make_module, make_user


class ExerciseTests(TestCase):
    def setUp(self):
        seed_sandbox_database()
        self.student = make_user("student@test.com", User.Role.STUDENT)
        self.course = make_course()
        self.module = make_module(self.course)
        self.lecture = make_lecture(self.module)
        self.exercise = make_exercise(self.module, lecture=self.lecture)

    def test_exercise_access(self):
        self.client.force_login(self.student)
        response = self.client.get(reverse("exercises:detail", args=[self.exercise.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.exercise.title)

    def test_correct_and_incorrect_sql(self):
        correct = exercise_service.run(self.student, self.exercise, "SELECT name FROM customers")
        self.assertTrue(correct.is_correct)
        self.assertEqual(correct.score, 100)
        alt = exercise_service.run(self.student, self.exercise, "SELECT name FROM customers WHERE name IS NOT NULL")
        self.assertTrue(alt.is_correct)
        wrong = exercise_service.run(self.student, self.exercise, "SELECT city FROM customers")
        self.assertFalse(wrong.is_correct)
        self.assertEqual(wrong.score, 0)

    def test_attempt_history_saved(self):
        exercise_service.run(self.student, self.exercise, "SELECT name FROM customers")
        exercise_service.run(self.student, self.exercise, "SELECT 1")
        self.assertEqual(ExerciseAttempt.objects.filter(student=self.student, exercise=self.exercise).count(), 2)

    def test_score_calculation(self):
        attempt = exercise_service.run(self.student, self.exercise, "SELECT name FROM customers")
        self.assertEqual(attempt.score, self.exercise.max_score)
