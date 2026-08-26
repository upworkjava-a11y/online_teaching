from django.test import TestCase
from django.urls import reverse

from apps.accounts.models import User
from apps.progress.models import LectureProgress
from tests.helpers import make_course, make_exercise, make_lecture, make_module, make_user


class LectureTests(TestCase):
    def setUp(self):
        self.student = make_user("student@test.com", User.Role.STUDENT)
        self.course = make_course()
        self.module = make_module(self.course)
        self.lecture = make_lecture(self.module, slug="one", title="Birinchi")
        self.lecture2 = make_lecture(self.module, slug="two", title="Ikkinchi")
        self.lecture2.order = 2
        self.lecture2.save()

    def test_lecture_access(self):
        self.client.force_login(self.student)
        response = self.client.get(reverse("learning:lecture", args=[self.lecture.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Birinchi")

    def test_lecture_completion_and_progress(self):
        self.client.force_login(self.student)
        response = self.client.post(reverse("learning:complete", args=[self.lecture.pk]))
        self.assertEqual(response.status_code, 302)
        progress = LectureProgress.objects.get(student=self.student, lecture=self.lecture)
        self.assertTrue(progress.completed)

    def test_complete_with_unsolved_practice_stays_on_lecture(self):
        make_exercise(self.module, slug="practice", lecture=self.lecture)
        self.client.force_login(self.student)
        response = self.client.post(reverse("learning:complete", args=[self.lecture.pk]))
        self.assertRedirects(response, reverse("learning:lecture", args=[self.lecture.pk]))
        follow = self.client.get(reverse("learning:lecture", args=[self.lecture.pk]))
        self.assertContains(follow, "amaliyot hali yechilmagan")

    def test_previous_next_navigation(self):
        self.assertEqual(self.lecture.get_next(), self.lecture2)
        self.assertEqual(self.lecture2.get_previous(), self.lecture)

    def test_lecture_shows_practice_link(self):
        exercise = make_exercise(self.module, slug="practice", lecture=self.lecture)
        self.client.force_login(self.student)
        response = self.client.get(reverse("learning:lecture", args=[self.lecture.pk]))
        self.assertContains(response, "Tavsiya etilgan mashqlar")
        self.assertContains(response, reverse("exercises:detail", args=[exercise.pk]))
