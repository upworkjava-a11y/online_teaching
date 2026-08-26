from django.test import TestCase
from django.urls import reverse

from apps.accounts.models import User
from apps.progress.models import LectureProgress
from tests.helpers import make_course, make_exercise, make_lecture, make_module, make_user


class CourseAccessTests(TestCase):
    def setUp(self):
        self.student = make_user("student@test.com", User.Role.STUDENT)
        self.published = make_course("sql", published=True, visible=True, title="SQL")
        self.hidden = make_course("excel", published=False, visible=False, title="Excel")
        self.module = make_module(self.published)
        self.lecture = make_lecture(self.module)

    def test_published_course_visible(self):
        self.client.force_login(self.student)
        response = self.client.get(reverse("courses:detail", args=["sql"]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "SQL")

    def test_unpublished_course_blocked(self):
        self.client.force_login(self.student)
        response = self.client.get(reverse("courses:detail", args=["excel"]))
        self.assertEqual(response.status_code, 403)

    def test_hidden_course_not_openable(self):
        self.client.force_login(self.student)
        response = self.client.get(reverse("courses:list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "yashirin")

    def test_lecture_partial_when_read_but_practice_unsolved(self):
        make_exercise(self.module, slug="practice", lecture=self.lecture)
        LectureProgress.objects.create(student=self.student, lecture=self.lecture, completed=True)
        self.client.force_login(self.student)
        response = self.client.get(reverse("courses:detail", args=["sql"]))
        self.assertContains(response, "is-partial")
        self.assertContains(response, "Amaliyot qoldi")
        self.assertNotContains(response, "is-done")

    def test_course_ordering(self):
        later = make_course("python", published=True, visible=True, title="Python")
        later.order = 5
        later.save()
        self.published.order = 1
        self.published.save()
        courses = list(type(self.published).objects.filter(is_published=True).order_by("order"))
        self.assertEqual(courses[0].slug, "sql")

    def test_non_sql_course_shows_coming_soon(self):
        make_course("python", published=True, visible=True, title="Python")
        self.client.force_login(self.student)
        detail = self.client.get(reverse("courses:detail", args=["python"]))
        self.assertEqual(detail.status_code, 403)
        self.assertContains(detail, "Hozir jarayonda", status_code=403)
        dashboard = self.client.get(reverse("dashboard:home"))
        self.assertEqual(dashboard.status_code, 200)
        self.assertContains(dashboard, "Hozir jarayonda")
        self.assertContains(dashboard, "course-card-locked")
        self.assertContains(dashboard, "Mening panelim")
        courses_list = self.client.get(reverse("courses:list"))
        self.assertEqual(courses_list.status_code, 200)
        self.assertContains(courses_list, "Hozir jarayonda")
        self.assertContains(courses_list, "course-card-locked")
        # Non-SQL cards must not show the free-module preview line
        self.assertEqual(courses_list.content.decode().count("Dastlabki 3 modul ochiq"), 1)
