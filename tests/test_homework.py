from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase
from django.urls import reverse

from apps.accounts.models import User
from apps.homework.models import HomeworkReview, HomeworkSubmission
from apps.homework.services import homework_service
from apps.homework.validation import validate_homework_file
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


class HomeworkTests(TestCase):
    def setUp(self):
        self.student = make_user("student@test.com", User.Role.STUDENT, first_name="Ali")
        self.other = make_user("other@test.com", User.Role.STUDENT, first_name="Bek")
        self.teacher = make_user("teacher@test.com", User.Role.TEACHER)
        self.course = make_course()
        self.module = make_module(self.course)
        self.lecture = make_lecture(self.module)
        self.assignment = make_homework(self.lecture)
        enroll(self.student, self.course)
        assign_teacher(self.teacher, self.course)

    def test_student_can_submit_txt(self):
        self.client.force_login(self.student)
        response = self.client.post(
            reverse("homework:submit", args=[self.assignment.pk]),
            {"file": txt_file("Javobim")},
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(HomeworkSubmission.objects.filter(student=self.student).count(), 1)

    def test_invalid_files_rejected(self):
        self.client.force_login(self.student)
        bad = SimpleUploadedFile("virus.exe", b"MZ", content_type="application/octet-stream")
        response = self.client.post(reverse("homework:submit", args=[self.assignment.pk]), {"file": bad})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(HomeworkSubmission.objects.count(), 0)

    def test_file_size_restriction(self):
        from django.core.exceptions import ValidationError

        huge = SimpleUploadedFile("big.txt", b"a" * (2 * 1024 * 1024), content_type="text/plain")
        with self.assertRaises(ValidationError):
            validate_homework_file(huge)

    def test_resubmit_replaces_single_file(self):
        first = homework_service.submit(self.student, self.assignment, txt_file("birinchi", "one.txt"))
        second = homework_service.submit(self.student, self.assignment, txt_file("ikkinchi", "two.txt"))
        self.assertEqual(first.pk, second.pk)
        self.assertEqual(HomeworkSubmission.objects.filter(student=self.student).count(), 1)
        second.refresh_from_db()
        self.assertEqual(second.original_filename, "two.txt")

    def test_student_can_download_own_file(self):
        submission = homework_service.submit(self.student, self.assignment, txt_file("javob", "javob.txt"))
        self.client.force_login(self.student)
        response = self.client.get(reverse("homework:download", args=[submission.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertIn("javob.txt", response.get("Content-Disposition", ""))

    def test_teacher_can_download_and_delete(self):
        submission = homework_service.submit(self.student, self.assignment, txt_file("javob", "javob.txt"))
        self.client.force_login(self.teacher)
        download = self.client.get(reverse("homework:download", args=[submission.pk]))
        self.assertEqual(download.status_code, 200)
        # Windows may keep the streamed file open briefly; close before delete.
        if hasattr(download, "close"):
            download.close()
        delete = self.client.post(reverse("homework:delete", args=[submission.pk]))
        self.assertEqual(delete.status_code, 302)
        self.assertFalse(HomeworkSubmission.objects.filter(pk=submission.pk).exists())

    def test_student_can_delete_own_submission(self):
        submission = homework_service.submit(self.student, self.assignment, txt_file("javob"))
        self.client.force_login(self.student)
        response = self.client.post(reverse("homework:delete", args=[submission.pk]))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(HomeworkSubmission.objects.filter(student=self.student).count(), 0)

    def test_review_score_feedback_revision(self):
        submission = homework_service.submit(self.student, self.assignment, txt_file("javob"))
        review = homework_service.review(
            self.teacher,
            submission,
            score=75,
            feedback="Yaxshi, lekin JOIN ni tushuntiring.",
            status=HomeworkReview.Status.NEEDS_REVISION,
            additional_instructions="Qayta yuboring",
        )
        submission.refresh_from_db()
        self.assertEqual(review.score, 75)
        self.assertIn("JOIN", review.feedback)
        self.assertEqual(submission.status, HomeworkSubmission.Status.NEEDS_REVISION)

    def test_student_sees_own_feedback(self):
        submission = homework_service.submit(self.student, self.assignment, txt_file("javob"))
        homework_service.review(self.teacher, submission, 85, "Alo ishlandi", HomeworkReview.Status.REVIEWED)
        self.client.force_login(self.student)
        response = self.client.get(reverse("homework:submit", args=[self.assignment.pk]))
        self.assertContains(response, "Alo ishlandi")
        self.assertContains(response, "85/100")

    def test_student_cannot_see_another_homework_file(self):
        submission = homework_service.submit(self.student, self.assignment, txt_file("maxfiy"))
        self.client.force_login(self.other)
        response = self.client.get(reverse("homework:download", args=[submission.pk]))
        self.assertEqual(response.status_code, 404)
