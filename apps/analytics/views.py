from django.contrib import messages
from django.core.exceptions import ValidationError
from django.core.paginator import Paginator
from django.http import Http404
from django.shortcuts import get_object_or_404, redirect, render
from django.views import View
import json

from apps.accounts.models import User
from apps.core.views import RoleRequiredMixin
from apps.courses.models import Course, Module
from apps.dashboard.leaderboard import build_leaderboard, recent_correct_solves
from apps.exercises.models import ExerciseAttempt
from apps.homework.models import HomeworkReview, HomeworkSubmission
from apps.homework.services import homework_service
from apps.progress.models import LectureProgress
from apps.progress.services import progress_service

from .services import (
    activity_series,
    dashboard_overview,
    difficult_exercises,
    homework_status_series,
    module_progress_series,
    progress_distribution,
    score_series,
    student_belongs_to_teacher,
    student_rows,
    teacher_courses,
    teacher_students,
)


class TeacherRequiredMixin(RoleRequiredMixin):
    allowed_roles = ("teacher", "admin")


class TeacherDashboardView(TeacherRequiredMixin, View):
    def get(self, request):
        board = build_leaderboard(limit=10)
        return render(
            request,
            "analytics/dashboard.html",
            {
                "overview": dashboard_overview(request.user),
                "students": student_rows(request.user, {})[:12],
                "difficult": difficult_exercises(request.user),
                "activity_json": json.dumps(activity_series(request.user)),
                "distribution_json": json.dumps(progress_distribution(request.user)),
                "module_json": json.dumps(module_progress_series(request.user)),
                "scores_json": json.dumps(score_series(request.user)),
                "leaderboard_top": board[:3],
                "leaderboard_preview": board,
                "recent_solves": recent_correct_solves(limit=6),
            },
        )


class TeacherStudentListView(TeacherRequiredMixin, View):
    def get(self, request):
        course_id = request.GET.get("course")
        course = teacher_courses(request.user).filter(pk=course_id).first() if course_id else None
        filters = {
            "course": course,
            "active": request.GET.get("active"),
            "progress_min": request.GET.get("progress_min"),
            "progress_max": request.GET.get("progress_max"),
            "score_min": request.GET.get("score_min"),
            "score_max": request.GET.get("score_max"),
        }
        rows = student_rows(request.user, filters)
        paginator = Paginator(rows, 25)
        page = paginator.get_page(request.GET.get("page"))
        return render(
            request,
            "analytics/students.html",
            {"page": page, "courses": teacher_courses(request.user), "filters": filters},
        )


class TeacherStudentDetailView(TeacherRequiredMixin, View):
    def get(self, request, pk):
        student = get_object_or_404(User, pk=pk, role=User.Role.STUDENT)
        if not request.user.is_admin and not student_belongs_to_teacher(request.user, student):
            raise Http404()
        course = teacher_courses(request.user).filter(is_published=True).first()
        stats = progress_service.course_stats(student, course) if course else {}
        modules = []
        if course:
            for module in course.modules.filter(is_published=True):
                modules.append({"module": module, "percent": progress_service.module_percent(student, module)})
        attempts = (
            ExerciseAttempt.objects.filter(student=student)
            .select_related("exercise", "exercise__module")[:20]
        )
        lectures = LectureProgress.objects.filter(student=student).select_related("lecture", "lecture__module")
        submissions = student.homework_submissions.select_related("assignment", "assignment__lecture").prefetch_related("reviews")[:20]
        failed = ExerciseAttempt.objects.filter(student=student, is_correct=False).count()
        return render(
            request,
            "analytics/student_detail.html",
            {
                "student": student,
                "course": course,
                "stats": stats,
                "modules": modules,
                "attempts": attempts,
                "completed_lectures": lectures.filter(completed=True),
                "uncompleted_count": (course.modules.filter(is_published=True).count() if course else 0),
                "submissions": submissions,
                "failed_attempts": failed,
            },
        )


class TeacherHomeworkListView(TeacherRequiredMixin, View):
    def get(self, request):
        courses = teacher_courses(request.user)
        qs = HomeworkSubmission.objects.filter(assignment__lecture__module__course__in=courses).select_related(
            "student", "assignment", "assignment__lecture", "assignment__lecture__module"
        )
        if request.GET.get("status"):
            qs = qs.filter(status=request.GET["status"])
        if request.GET.get("student"):
            qs = qs.filter(student_id=request.GET["student"])
        if request.GET.get("course"):
            qs = qs.filter(assignment__lecture__module__course_id=request.GET["course"])
        if request.GET.get("module"):
            qs = qs.filter(assignment__lecture__module_id=request.GET["module"])
        page = Paginator(qs, 20).get_page(request.GET.get("page"))
        pending = qs.filter(status__in=["submitted", "under_review"]).count()
        reviewed = HomeworkSubmission.objects.filter(assignment__lecture__module__course__in=courses, status="reviewed").count()
        revision = HomeworkSubmission.objects.filter(assignment__lecture__module__course__in=courses, status="needs_revision").count()
        return render(
            request,
            "analytics/homework_list.html",
            {
                "page": page,
                "courses": courses,
                "modules": Module.objects.filter(course__in=courses),
                "students": teacher_students(request.user),
                "pending": pending,
                "reviewed": reviewed,
                "revision": revision,
                "total": HomeworkSubmission.objects.filter(assignment__lecture__module__course__in=courses).count(),
            },
        )


class TeacherHomeworkReviewView(TeacherRequiredMixin, View):
    def get_submission(self, request, pk):
        submission = get_object_or_404(
            HomeworkSubmission.objects.select_related("student", "assignment", "assignment__lecture"),
            pk=pk,
        )
        if not request.user.is_admin and not student_belongs_to_teacher(request.user, submission.student):
            raise Http404()
        return submission

    def get(self, request, pk):
        submission = self.get_submission(request, pk)
        content = ""
        try:
            content = submission.file.read().decode("utf-8")
            submission.file.seek(0)
        except Exception:
            content = "Faylni o‘qib bo‘lmadi."
        latest_review = submission.latest_review
        history = HomeworkSubmission.objects.filter(
            student=submission.student, assignment=submission.assignment
        ).prefetch_related("reviews")
        return render(
            request,
            "analytics/homework_review.html",
            {
                "submission": submission,
                "content": content,
                "history": history,
                "latest_review": latest_review,
            },
        )

    def post(self, request, pk):
        submission = self.get_submission(request, pk)
        try:
            homework_service.review(
                reviewer=request.user,
                submission=submission,
                score=int(request.POST.get("score") or 0),
                feedback=request.POST.get("feedback", ""),
                status=request.POST.get("status") or HomeworkReview.Status.REVIEWED,
                additional_instructions=request.POST.get("additional_instructions", ""),
            )
        except (ValidationError, ValueError) as exc:
            messages.error(request, getattr(exc, "messages", ["Tekshiruv saqlanmadi."])[0] if hasattr(exc, "messages") else str(exc))
            return redirect("analytics:homework_review", pk=submission.pk)
        messages.success(request, "Tekshiruv saqlandi.")
        return redirect("analytics:homework_review", pk=submission.pk)


class TeacherAnalyticsView(TeacherRequiredMixin, View):
    def get(self, request):
        overview = dashboard_overview(request.user)
        return render(
            request,
            "analytics/analytics.html",
            {
                "overview": overview,
                "difficult": difficult_exercises(request.user),
                "courses": teacher_courses(request.user),
                "activity_json": json.dumps(activity_series(request.user)),
                "distribution_json": json.dumps(progress_distribution(request.user)),
                "module_json": json.dumps(module_progress_series(request.user)),
                "homework_json": json.dumps(homework_status_series(request.user)),
                "scores_json": json.dumps(score_series(request.user)),
            },
        )
