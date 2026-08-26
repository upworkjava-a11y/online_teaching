from django.test import TestCase
from django.urls import reverse

from apps.accounts.models import User
from apps.dashboard.leaderboard import build_leaderboard
from apps.exercises.models import Exercise, ExerciseAttempt
from tests.helpers import make_course, make_exercise, make_lecture, make_module, make_user


class LeaderboardTests(TestCase):
    def setUp(self):
        self.course = make_course()
        self.module = make_module(self.course)
        self.lecture = make_lecture(self.module)
        self.easy = make_exercise(
            self.module, slug="easy1", lecture=self.lecture, difficulty=Exercise.Difficulty.EASY, title="Easy", order=1
        )
        self.medium = make_exercise(
            self.module,
            slug="med1",
            lecture=self.lecture,
            difficulty=Exercise.Difficulty.MEDIUM,
            title="Medium",
            order=2,
        )
        self.hard = make_exercise(
            self.module, slug="hard1", lecture=self.lecture, difficulty=Exercise.Difficulty.HARD, title="Hard", order=3
        )
        self.a = make_user("a@test.com", User.Role.STUDENT, first_name="Ali", last_name="A")
        self.b = make_user("b@test.com", User.Role.STUDENT, first_name="Bobur", last_name="B")
        self.c = make_user("c@test.com", User.Role.STUDENT, first_name="Carol", last_name="C")

    def _solve(self, student, exercise):
        ExerciseAttempt.objects.create(
            student=student,
            exercise=exercise,
            sql_query="SELECT 1",
            is_correct=True,
            score=100,
        )

    def test_scoring_easy_medium_hard(self):
        self._solve(self.a, self.easy)
        self._solve(self.a, self.medium)
        self._solve(self.a, self.hard)
        board = build_leaderboard()
        self.assertEqual(board[0]["student_id"], self.a.pk)
        self.assertEqual(board[0]["points"], 1 + 2 + 3)
        self.assertEqual(board[0]["easy_count"], 1)
        self.assertEqual(board[0]["medium_count"], 1)
        self.assertEqual(board[0]["hard_count"], 1)

    def test_duplicate_correct_attempts_count_once(self):
        self._solve(self.a, self.hard)
        self._solve(self.a, self.hard)
        board = build_leaderboard()
        self.assertEqual(board[0]["points"], 3)
        self.assertEqual(board[0]["solved_count"], 1)

    def test_rank_order_by_points(self):
        self._solve(self.a, self.easy)
        self._solve(self.b, self.medium)
        self._solve(self.c, self.hard)
        board = build_leaderboard()
        self.assertEqual([row["student_id"] for row in board], [self.c.pk, self.b.pk, self.a.pk])
        self.assertEqual([row["rank"] for row in board], [1, 2, 3])

    def test_leaderboard_page_uzbek(self):
        self._solve(self.a, self.hard)
        self.client.force_login(self.a)
        response = self.client.get(reverse("dashboard:leaderboard"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Reyting jadvali")
        self.assertContains(response, "Reyting")
        self.assertContains(response, "1-o‘rin")
        self.assertContains(response, "Ali A")
