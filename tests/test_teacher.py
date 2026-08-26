from django.test import TestCase
from django.urls import reverse

from apps.accounts.models import User
from apps.homework.models import HomeworkReview
from apps.homework.services import homework_service
from tests.helpers import (
    assign_teacher,
    enroll,
    make_course,
    make_homework,
    make_lecture,
    make_module,
    make_user,
    txt_file,
)


class TeacherAccessTests(TestCase):
    def setUp(self):
        self.teacher = make_user("teacher@test.com", User.Role.TEACHER)
        self.other_teacher = make_user("other-teacher@test.com", User.Role.TEACHER)
        self.student = make_user("student@test.com", User.Role.STUDENT, first_name="Ali")
        self.other_student = make_user("other-student@test.com", User.Role.STUDENT, first_name="Gulnora")
        self.course = make_course("sql")
        self.other_course = make_course("excel", published=False, visible=False, title="Excel")
        self.module = make_module(self.course)
        self.lecture = make_lecture(self.module)
        self.assignment = make_homework(self.lecture)
        enroll(self.student, self.course)
        enroll(self.other_student, self.other_course)
        assign_teacher(self.teacher, self.course)
        assign_teacher(self.other_teacher, self.other_course)

    def test_teacher_sees_assigned_students(self):
        self.client.force_login(self.teacher)
        response = self.client.get(reverse("analytics:students"))
        self.assertContains(response, "Ali")
        self.assertNotContains(response, "Gulnora")

    def test_teacher_cannot_open_other_teacher_student(self):
        self.client.force_login(self.teacher)
        response = self.client.get(reverse("analytics:student_detail", args=[self.other_student.pk]))
        self.assertEqual(response.status_code, 404)

    def test_teacher_can_see_student_progress(self):
        self.client.force_login(self.teacher)
        response = self.client.get(reverse("analytics:student_detail", args=[self.student.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Ali")

    def test_teacher_can_review_assigned_homework(self):
        submission = homework_service.submit(self.student, self.assignment, txt_file("javob"))
        self.client.force_login(self.teacher)
        page = self.client.get(reverse("analytics:homework_review", args=[submission.pk]))
        self.assertEqual(page.status_code, 200)
        self.assertContains(page, "Baholash va fikr-mulohaza")
        self.assertContains(page, "Fikr-mulohaza")
        response = self.client.post(
            reverse("analytics:homework_review", args=[submission.pk]),
            {
                "score": "90",
                "feedback": "Yaxshi ish",
                "status": HomeworkReview.Status.REVIEWED,
                "additional_instructions": "",
            },
        )
        self.assertEqual(response.status_code, 302)
        submission.refresh_from_db()
        self.assertEqual(submission.status, "reviewed")
        self.assertEqual(submission.latest_review.score, 90)
        self.assertIn("Yaxshi", submission.latest_review.feedback)

    def test_teacher_can_open_reyting_page(self):
        self.client.force_login(self.teacher)
        response = self.client.get(reverse("dashboard:leaderboard"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Reyting jadvali")

    def test_teacher_dashboard_shows_reyting(self):
        self.client.force_login(self.teacher)
        response = self.client.get(reverse("analytics:dashboard"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Reyting")
        self.assertContains(response, "Reytingni ochish")
