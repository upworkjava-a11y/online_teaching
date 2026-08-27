from django.contrib import messages
from django.core.exceptions import ValidationError
from django.http import FileResponse, Http404
from django.shortcuts import get_object_or_404, redirect, render
from django.views import View

from apps.access.services import access_service
from apps.core.views import RoleRequiredMixin

from .models import HomeworkAssignment, HomeworkSubmission
from .services import homework_service


def _can_manage_submission(user, submission: HomeworkSubmission) -> bool:
    if user.is_admin:
        return True
    if user.is_student and submission.student_id == user.pk:
        return True
    if user.is_teacher:
        profile = getattr(user, "teacher_profile", None)
        if not profile:
            return False
        return profile.assigned_courses.filter(
            pk=submission.assignment.lecture.module.course_id
        ).exists()
    return False


class HomeworkListView(RoleRequiredMixin, View):
    allowed_roles = ("student",)
    auth_gate_title = "Uy vazifasi uchun hisob kerak"
    auth_gate_message = (
        "Uy vazifasini ko‘rish va yuborish uchun tizimga kiring yoki ro‘yxatdan o‘ting."
    )

    def get(self, request):
        assignments = (
            HomeworkAssignment.objects.filter(
                is_published=True,
                lecture__is_published=True,
                lecture__module__course__is_published=True,
                lecture__module__course__is_visible=True,
            )
            .select_related("lecture", "lecture__module", "lecture__module__course")
            .order_by(
                "lecture__module__course__order",
                "lecture__module__order",
                "lecture__order",
            )
        )
        rows = []
        for assignment in assignments:
            course = assignment.lecture.module.course
            coming_soon = (
                not access_service.is_course_open(course)
                and not (request.user.is_admin or request.user.is_teacher)
            )
            if coming_soon:
                rows.append(
                    {
                        "assignment": assignment,
                        "latest": None,
                        "status": "coming_soon",
                        "coming_soon": True,
                    }
                )
                continue
            if not access_service.can_access(request.user, assignment.lecture):
                continue
            latest = homework_service.latest_for_student(request.user, assignment)
            rows.append(
                {
                    "assignment": assignment,
                    "latest": latest,
                    "status": latest.status if latest else "not_submitted",
                    "coming_soon": False,
                }
            )
        return render(request, "homework/list.html", {"rows": rows})


class HomeworkSubmitView(RoleRequiredMixin, View):
    allowed_roles = ("student",)
    auth_gate_title = "Uy vazifasi uchun hisob kerak"
    auth_gate_message = (
        "Uy vazifasini yuborish uchun tizimga kiring yoki ro‘yxatdan o‘ting."
    )

    def get_assignment(self, request, pk):
        assignment = get_object_or_404(
            HomeworkAssignment.objects.select_related(
                "lecture", "lecture__module", "lecture__module__course"
            ),
            pk=pk,
            is_published=True,
        )
        if not access_service.can_access(request.user, assignment.lecture):
            raise Http404("Bu bo‘lim siz uchun hozircha yopilgan.")
        return assignment

    def get(self, request, pk):
        assignment = self.get_assignment(request, pk)
        latest = homework_service.latest_for_student(request.user, assignment)
        history = []
        if latest:
            history = (
                assignment.submissions.filter(pk=latest.pk)
                .prefetch_related("reviews")
            )
        return render(
            request,
            "homework/submit.html",
            {"assignment": assignment, "history": history, "latest": latest},
        )

    def post(self, request, pk):
        assignment = self.get_assignment(request, pk)
        uploaded = request.FILES.get("file")
        if len(request.FILES.getlist("file")) > 1:
            messages.error(request, "Faqat 1 ta .txt fayl yuborish mumkin.")
            return redirect("homework:submit", pk=assignment.pk)
        try:
            homework_service.submit(request.user, assignment, uploaded)
        except ValidationError as exc:
            messages.error(request, " ".join(exc.messages))
            return redirect("homework:submit", pk=assignment.pk)
        messages.success(request, "Uy vazifasi saqlandi.")
        return redirect("homework:submit", pk=assignment.pk)


class HomeworkDownloadView(RoleRequiredMixin, View):
    allowed_roles = ("student", "teacher", "admin")

    def get(self, request, pk):
        submission = get_object_or_404(
            HomeworkSubmission.objects.select_related(
                "assignment", "assignment__lecture", "assignment__lecture__module"
            ),
            pk=pk,
        )
        if not _can_manage_submission(request.user, submission):
            raise Http404()
        return FileResponse(
            submission.file.open("rb"),
            as_attachment=True,
            filename=submission.original_filename,
        )


class HomeworkDeleteView(RoleRequiredMixin, View):
    allowed_roles = ("student", "teacher", "admin")
    http_method_names = ["post"]

    def post(self, request, pk):
        submission = get_object_or_404(
            HomeworkSubmission.objects.select_related(
                "assignment", "assignment__lecture", "assignment__lecture__module"
            ),
            pk=pk,
        )
        if not _can_manage_submission(request.user, submission):
            raise Http404()
        assignment_pk = submission.assignment_id
        was_student = request.user.is_student and submission.student_id == request.user.pk
        homework_service.delete_submission(submission)
        messages.success(request, "Topshiriq o‘chirildi.")
        if was_student:
            return redirect("homework:submit", pk=assignment_pk)
        return redirect("analytics:homework")
