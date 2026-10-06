"""Badge / achievement system tests."""

from __future__ import annotations

from datetime import timedelta

from django.contrib.auth import get_user_model
from django.core.cache import cache
from django.test import Client, TestCase, override_settings
from django.urls import reverse
from django.utils import timezone

from apps.badges.catalog import BADGE_DEFINITIONS, ensure_badges
from apps.badges.models import Badge, UserBadge, UserRankPeak
from apps.badges.services import service as badge_service
from apps.badges.topics import TOPIC_JOIN, TOPIC_SELECT, TOPIC_WINDOW
from apps.courses.models import Course, Lecture, Module
from apps.exercises.models import Exercise, ExerciseAttempt
from apps.progress.models import LectureProgress, StudentStreak
from apps.progress.streak import record_learning_day

User = get_user_model()


class BadgeBase(TestCase):
    @classmethod
    def setUpTestData(cls):
        ensure_badges()
        cls.course = Course.objects.create(title="SQL", slug="sql-test", is_published=True, is_visible=True)
        cls.mod_select = Module.objects.create(course=cls.course, title="Select", slug="sql-asoslari", order=1, is_published=True)
        cls.mod_join = Module.objects.create(course=cls.course, title="Joins", slug="joins", order=2, is_published=True)
        cls.mod_win = Module.objects.create(course=cls.course, title="Window", slug="window-functions", order=3, is_published=True)
        cls.py_course = Course.objects.create(title="Python", slug="python", is_published=True, is_visible=True)
        cls.py_mod = Module.objects.create(course=cls.py_course, title="Py", slug="py-noldan", order=1, is_published=True)

    def setUp(self):
        cache.clear()
        self.user = User.objects.create_user(
            email="badgeuser@example.com",
            password="Pass123!",
            username="badgeuser",
            role=User.Role.STUDENT,
        )

    def _ex(self, module, slug, order=1):
        return Exercise.objects.create(
            module=module,
            title=slug,
            slug=slug,
            description="d",
            task="t",
            kind=Exercise.Kind.SQL,
            order=order,
            is_published=True,
        )

    def _solve(self, exercise):
        ExerciseAttempt.objects.create(
            student=self.user,
            exercise=exercise,
            sql_query="SELECT 1",
            is_correct=True,
            score=100,
        )


class ProblemBadgeTests(BadgeBase):
    def test_first_and_ten_problems(self):
        for i in range(10):
            ex = self._ex(self.mod_select, f"p-{i}", order=i)
            self._solve(ex)
            record_learning_day(self.user)
        newly = badge_service.evaluate(self.user, trigger="solve")
        slugs = {ub.badge.slug for ub in UserBadge.objects.filter(user=self.user)}
        self.assertIn("first-step", slugs)
        self.assertIn("problem-solver", slugs)
        # permanent + no duplicates
        badge_service.evaluate(self.user, trigger="solve")
        self.assertEqual(UserBadge.objects.filter(user=self.user, badge__slug="first-step").count(), 1)

    def test_topic_join_and_sql_explorer(self):
        for i in range(5):
            self._solve(self._ex(self.mod_join, f"j-{i}", order=i))
        self._solve(self._ex(self.mod_select, "s-1", order=1))
        self._solve(self._ex(self.mod_win, "w-1", order=1))
        badge_service.evaluate(self.user, trigger="solve")
        slugs = set(UserBadge.objects.filter(user=self.user).values_list("badge__slug", flat=True))
        self.assertIn("join-master", slugs)
        self.assertIn("sql-explorer", slugs)

    def test_python_starter(self):
        for i in range(5):
            self._solve(self._ex(self.py_mod, f"py-{i}", order=i))
        badge_service.evaluate(self.user, trigger="solve")
        self.assertTrue(UserBadge.objects.filter(user=self.user, badge__slug="python-starter").exists())


class StreakBadgeTests(BadgeBase):
    def test_streak_badges_and_break(self):
        streak, _ = StudentStreak.objects.get_or_create(student=self.user)
        streak.current_streak = 3
        streak.longest_streak = 3
        streak.last_solved_date = timezone.localdate()
        streak.save()
        badge_service.evaluate(self.user, trigger="solve")
        self.assertTrue(UserBadge.objects.filter(user=self.user, badge__slug="streak-3").exists())
        # broken streak does not remove badge
        streak.current_streak = 0
        streak.save(update_fields=["current_streak"])
        self.assertTrue(UserBadge.objects.filter(user=self.user, badge__slug="streak-3").exists())

    def test_seven_and_thirty(self):
        streak, _ = StudentStreak.objects.get_or_create(student=self.user)
        streak.longest_streak = 30
        streak.current_streak = 30
        streak.save()
        badge_service.evaluate(self.user, trigger="solve")
        slugs = set(UserBadge.objects.filter(user=self.user).values_list("badge__slug", flat=True))
        self.assertIn("streak-7", slugs)
        self.assertIn("streak-30", slugs)


class RankBadgeTests(BadgeBase):
    def test_historical_top_ranks(self):
        badge_service.check_after_rank_update(self.user, 10)
        self.assertTrue(UserBadge.objects.filter(user=self.user, badge__slug="top-10").exists())
        badge_service.check_after_rank_update(self.user, 2)
        self.assertTrue(UserBadge.objects.filter(user=self.user, badge__slug="top-3").exists())
        badge_service.check_after_rank_update(self.user, 1)
        self.assertTrue(UserBadge.objects.filter(user=self.user, badge__slug="number-one").exists())
        # historical: later worse rank does not revoke
        badge_service.check_after_rank_update(self.user, 50)
        peak = UserRankPeak.objects.get(user=self.user)
        self.assertEqual(peak.best_rank, 1)
        self.assertTrue(UserBadge.objects.filter(user=self.user, badge__slug="number-one").exists())


class LearningBadgeTests(BadgeBase):
    def test_lesson_and_course(self):
        lectures = []
        for i in range(2):
            lec = Lecture.objects.create(
                module=self.mod_select,
                title=f"L{i}",
                slug=f"lec-{i}",
                content="<p>x</p>",
                order=i + 1,
                is_published=True,
            )
            lectures.append(lec)
            LectureProgress.objects.create(
                student=self.user, lecture=lec, completed=True, completed_at=timezone.now()
            )
        # only one module with 2 lectures — need all course lectures
        badge_service.evaluate(self.user, trigger="lesson")
        self.assertTrue(UserBadge.objects.filter(user=self.user, badge__slug="first-lesson").exists())
        # Complete remaining published lectures in course modules
        for mod in (self.mod_join, self.mod_win):
            lec = Lecture.objects.create(
                module=mod, title=mod.slug, slug=f"lec-{mod.slug}", content="x", order=1, is_published=True
            )
            LectureProgress.objects.create(
                student=self.user, lecture=lec, completed=True, completed_at=timezone.now()
            )
        badge_service.evaluate(self.user, trigger="lesson")
        self.assertTrue(UserBadge.objects.filter(user=self.user, badge__slug="course-finisher").exists())


class DataDrivenBadgeTests(BadgeBase):
    def test_difficulty_and_sql_course_solves(self):
        # Use real sql course slug for COURSE_SOLVES badges
        self.course.slug = "sql"
        self.course.save(update_fields=["slug"])
        for i in range(25):
            ex = self._ex(self.mod_select, f"ez-{i}", order=i)
            ex.difficulty = Exercise.Difficulty.EASY
            ex.save(update_fields=["difficulty"])
            self._solve(ex)
        for i in range(15):
            ex = self._ex(self.mod_join, f"md-{i}", order=i)
            ex.difficulty = Exercise.Difficulty.MEDIUM
            ex.save(update_fields=["difficulty"])
            self._solve(ex)
        for i in range(3):
            ex = self._ex(self.mod_win, f"hd-{i}", order=i)
            ex.difficulty = Exercise.Difficulty.HARD
            ex.save(update_fields=["difficulty"])
            self._solve(ex)
        badge_service.evaluate(self.user, trigger="solve")
        slugs = set(UserBadge.objects.filter(user=self.user).values_list("badge__slug", flat=True))
        self.assertIn("easy-starter", slugs)
        self.assertIn("medium-solver", slugs)
        self.assertIn("hard-crusher", slugs)
        self.assertIn("sql-solver", slugs)
        # duplicate evaluate is idempotent
        before = UserBadge.objects.filter(user=self.user).count()
        badge_service.evaluate(self.user, trigger="solve")
        self.assertEqual(UserBadge.objects.filter(user=self.user).count(), before)

    def test_cross_course_multi_skilled(self):
        bank = Course.objects.create(
            title="Banking", slug="english-banking", is_published=True, is_visible=True
        )
        bmod = Module.objects.create(course=bank, title="B", slug="eb-bank-basics", order=1, is_published=True)
        for i in range(5):
            self._solve(self._ex(self.mod_select, f"sqlx-{i}", order=i))
            ex = self._ex(bmod, f"bx-{i}", order=i)
            ex.kind = Exercise.Kind.QUIZ
            ex.is_skill_test = True
            ex.save(update_fields=["kind", "is_skill_test"])
            self._solve(ex)
        badge_service.evaluate(self.user, trigger="solve")
        self.assertTrue(UserBadge.objects.filter(user=self.user, badge__slug="multi-skilled").exists())
        self.assertTrue(UserBadge.objects.filter(user=self.user, badge__slug="banking-starter").exists() is False)
        # banking starter needs 10
        for i in range(5, 10):
            ex = self._ex(bmod, f"bx-{i}", order=i)
            ex.kind = Exercise.Kind.QUIZ
            ex.is_skill_test = True
            ex.save(update_fields=["kind", "is_skill_test"])
            self._solve(ex)
        badge_service.evaluate(self.user, trigger="solve")
        self.assertTrue(UserBadge.objects.filter(user=self.user, badge__slug="banking-starter").exists())


class IntegrityTests(BadgeBase):
    def test_catalog_size(self):
        self.assertEqual(Badge.objects.filter(is_active=True).count(), len(BADGE_DEFINITIONS))

    def test_achievements_page_awards_eligible_on_view(self):
        """Progress can be complete before UserBadge exists (e.g. after data import)."""
        self._solve(self._ex(self.mod_select, "import-solve", 1))
        self.assertEqual(UserBadge.objects.filter(user=self.user).count(), 0)
        client = Client()
        client.force_login(self.user)
        resp = client.get(reverse("badges:achievements", args=[self.user.username]))
        self.assertEqual(resp.status_code, 200)
        self.assertTrue(UserBadge.objects.filter(user=self.user, badge__slug="first-step").exists())
        self.assertContains(resp, "is-earned")

    def test_no_manual_award_endpoint(self):
        client = Client()
        client.force_login(self.user)
        # toast endpoint cannot award
        resp = client.get(reverse("badges:toasts"))
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(UserBadge.objects.filter(user=self.user).count(), 0)

    def test_progress_and_page(self):
        self._solve(self._ex(self.mod_select, "one", 1))
        rows = badge_service.all_progress(self.user)
        first = next(r for r in rows if r.badge.slug == "first-step")
        self.assertEqual(first.current, 1)
        client = Client()
        client.force_login(self.user)
        resp = client.get(reverse("badges:achievements", args=[self.user.username]))
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, "First Step")

    def test_toast_queued_once(self):
        self._solve(self._ex(self.mod_select, "toast-ex", 1))
        badge_service.evaluate(self.user, trigger="solve")
        toasts = badge_service.pop_toasts(self.user.pk)
        self.assertTrue(any(t["slug"] == "first-step" for t in toasts))
        self.assertEqual(badge_service.pop_toasts(self.user.pk), [])
