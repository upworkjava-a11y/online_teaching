import logging

from django.core.exceptions import ValidationError
from django.db import transaction

from .models import HomeworkAssignment, HomeworkReview, HomeworkSubmission, NotificationHook
from .validation import validate_homework_file

logger = logging.getLogger("apps.homework")


class HomeworkService:
    @transaction.atomic
    def submit(self, student, assignment: HomeworkAssignment, uploaded) -> HomeworkSubmission:
        """Bir talaba + bir topshiriq = bitta fayl. Qayta yuborsa — almashtiriladi."""
        filename = validate_homework_file(uploaded)
        existing = self.latest_for_student(student, assignment)
        if existing:
            old_name = existing.file.name if existing.file else ""
            if existing.file:
                try:
                    existing.file.close()
                except Exception:
                    pass
            existing.file = uploaded
            existing.original_filename = filename
            existing.status = HomeworkSubmission.Status.SUBMITTED
            existing.save()
            if old_name:
                from django.core.files.storage import default_storage

                try:
                    default_storage.delete(old_name)
                except OSError:
                    pass
            submission = existing
            logger.info(
                "homework_replaced",
                extra={"submission_id": submission.pk, "student_id": student.pk},
            )
        else:
            submission = HomeworkSubmission(
                assignment=assignment,
                student=student,
                file=uploaded,
                original_filename=filename,
                status=HomeworkSubmission.Status.SUBMITTED,
            )
            submission.save()
            logger.info(
                "homework_submitted",
                extra={"submission_id": submission.pk, "student_id": student.pk},
            )
        NotificationHook.objects.create(
            event=NotificationHook.Event.HOMEWORK_SUBMITTED,
            payload={"submission_id": submission.pk, "student_id": student.pk},
        )
        return submission

    def latest_for_student(self, student, assignment: HomeworkAssignment):
        return assignment.submissions.filter(student=student).order_by("-created_at").first()

    def student_status(self, student, assignment: HomeworkAssignment) -> str:
        latest = self.latest_for_student(student, assignment)
        if not latest:
            return "not_submitted"
        return latest.status

    @transaction.atomic
    def delete_submission(self, submission: HomeworkSubmission) -> None:
        submission_id = submission.pk
        file_name = submission.file.name if submission.file else ""
        if submission.file:
            try:
                submission.file.close()
            except Exception:
                pass
        submission.delete()
        if file_name:
            from django.core.files.storage import default_storage

            try:
                default_storage.delete(file_name)
            except OSError:
                logger.warning(
                    "homework_file_delete_failed",
                    extra={"submission_id": submission_id, "file": file_name},
                )
        logger.info("homework_deleted", extra={"submission_id": submission_id})

    @transaction.atomic
    def review(
        self,
        reviewer,
        submission: HomeworkSubmission,
        score: int,
        feedback: str,
        status: str,
        additional_instructions: str = "",
    ) -> HomeworkReview:
        if score < 0 or score > submission.assignment.max_score:
            raise ValidationError("Ball oralig‘i noto‘g‘ri.")
        review = HomeworkReview.objects.create(
            submission=submission,
            reviewer=reviewer,
            score=score,
            feedback=feedback,
            additional_instructions=additional_instructions,
            status=status,
        )
        submission.status = status
        submission.save(update_fields=["status", "updated_at"])
        event = (
            NotificationHook.Event.HOMEWORK_REVISION
            if status == HomeworkReview.Status.NEEDS_REVISION
            else NotificationHook.Event.HOMEWORK_REVIEWED
        )
        NotificationHook.objects.create(
            event=event,
            payload={"submission_id": submission.pk, "review_id": review.pk},
        )
        logger.info("homework_reviewed", extra={"submission_id": submission.pk, "reviewer_id": reviewer.pk})
        return review


homework_service = HomeworkService()
