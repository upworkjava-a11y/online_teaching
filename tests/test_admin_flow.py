from django.contrib.contenttypes.models import ContentType
from django.test import TestCase
from django.urls import reverse

from apps.access.models import UserContentAccess
from apps.accounts.models import User
from apps.homework.models import HomeworkReview
from apps.homework.services import homework_service
from tests.helpers import make_course, make_homework, make_lecture, make_module, make_user, txt_file


class AdminFlowTests(TestCase):
    def setUp(self):
        self.admin = make_user("admin@test.com", User.Role.ADMIN, is_staff=True, is_superuser=True)
        self.student = make_user("student@test.com", User.Role.STUDENT)
        self.course = make_course()
        self.module = make_module(self.course)
        self.lecture = make_lecture(self.module)
        self.assignment = make_homework(self.lecture)

    def test_admin_can_open_admin_and_content(self):
        self.client.force_login(self.admin)
        self.assertEqual(self.client.get("/admin/").status_code, 200)
        self.assertEqual(self.client.get("/admin/courses/course/").status_code, 200)
        self.assertEqual(self.client.get("/admin/homework/homeworksubmission/").status_code, 200)

    def test_admin_can_publish_unpublish(self):
        self.course.is_published = False
        self.course.save()
        self.course.is_published = True
        self.course.save()
        self.course.refresh_from_db()
        self.assertTrue(self.course.is_published)

    def test_admin_can_block_and_review(self):
        UserContentAccess.objects.create(
            user=self.student,
            content_type=ContentType.objects.get_for_model(self.module),
            object_id=self.module.pk,
            status=UserContentAccess.Status.BLOCKED,
            created_by=self.admin,
        )
        submission = homework_service.submit(self.student, self.assignment, txt_file("javob"))
        homework_service.review(self.admin, submission, 80, "Yaxshi", HomeworkReview.Status.REVIEWED)
        self.assertEqual(UserContentAccess.objects.count(), 1)
        submission.refresh_from_db()
        self.assertEqual(submission.status, "reviewed")
