from django.test import TestCase
from django.urls import reverse

from apps.accounts.models import User
from apps.exercises.models import ExerciseAttempt
from apps.exercises.navigation import next_exercise_for, next_lecture_for
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

    def test_next_nav_after_correct(self):
        next_ex = make_exercise(
            self.module, slug="ex2", lecture=self.lecture, title="Ikkinchi mashq", order=2
        )
        next_lec = make_lecture(self.module, slug="select-2", title="Keyingi dars", order=2)
        self.assertEqual(next_exercise_for(self.student, self.exercise).pk, next_ex.pk)
        self.assertEqual(next_lecture_for(self.student, self.exercise).pk, next_lec.pk)

        exercise_service.run(self.student, self.exercise, "SELECT name FROM customers")
        self.client.force_login(self.student)
        response = self.client.get(reverse("exercises:detail", args=[self.exercise.pk]))
        self.assertContains(response, "Keyingi masala")
        self.assertContains(response, "Keyingi dars")
        self.assertContains(response, reverse("exercises:detail", args=[next_ex.pk]))
        self.assertContains(response, reverse("learning:lecture", args=[next_lec.pk]))

    def test_next_nav_hidden_when_incorrect(self):
        make_exercise(self.module, slug="ex2", lecture=self.lecture, title="Ikkinchi", order=2)
        exercise_service.run(self.student, self.exercise, "SELECT city FROM customers")
        self.client.force_login(self.student)
        response = self.client.get(reverse("exercises:detail", args=[self.exercise.pk]))
        self.assertNotContains(response, "Keyingi masala")
        self.assertNotContains(response, "Keyingi dars →")
