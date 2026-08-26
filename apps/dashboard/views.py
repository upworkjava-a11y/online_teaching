from django.shortcuts import render
from django.views import View

from apps.access.services import access_service
from apps.core.views import RoleRequiredMixin
from apps.courses.models import Course
from apps.exercises.models import ExerciseAttempt
from apps.homework.models import HomeworkAssignment
from apps.homework.services import homework_service
from apps.progress.models import LectureProgress
from apps.progress.services import progress_service


class StudentDashboardView(RoleRequiredMixin, View):
    allowed_roles = ("student",)

    def get(self, request):
        courses = Course.objects.filter(is_published=True, is_visible=True).order_by("order")
        course_cards = []
        for course in courses:
            decision = access_service.evaluate(request.user, course)
            course_cards.append(
                {
                    "course": course,
                    "stats": progress_service.course_stats(request.user, course),
                    "decision": decision,
                    "coming_soon": (
                        not access_service.is_course_open(course)
                        and not (request.user.is_admin or request.user.is_teacher)
                    )
                    or decision.code == "coming_soon",
                }
            )
        continue_lecture = progress_service.last_position(request.user)
        if continue_lecture and not access_service.can_access(request.user, continue_lecture):
            continue_lecture = None
        recent_attempts = (
            ExerciseAttempt.objects.filter(student=request.user)
            .select_related("exercise", "exercise__module")[:8]
        )
        recent_lectures = (
            LectureProgress.objects.filter(student=request.user)
            .select_related("lecture", "lecture__module")
            .order_by("-updated_at")[:5]
        )
        homework_rows = []
        for assignment in HomeworkAssignment.objects.filter(is_published=True).select_related("lecture"):
            if not access_service.can_access(request.user, assignment.lecture):
                continue
            latest = homework_service.latest_for_student(request.user, assignment)
            if latest and latest.status in ("submitted", "under_review", "needs_revision", "reviewed"):
                homework_rows.append({"assignment": assignment, "latest": latest})
        return render(
            request,
            "dashboard/student.html",
            {
                "course_cards": course_cards,
                "continue_lecture": continue_lecture,
                "recent_attempts": recent_attempts,
                "recent_lectures": recent_lectures,
                "homework_rows": homework_rows,
            },
        )


class StudentProgressView(RoleRequiredMixin, View):
    allowed_roles = ("student",)

    def get(self, request):
        courses = Course.objects.filter(is_published=True, is_visible=True).order_by("order")
        rows = []
        for course in courses:
            coming_soon = (
                not access_service.is_course_open(course)
                and not (request.user.is_admin or request.user.is_teacher)
            )
            modules = []
            if not coming_soon:
                for module in course.modules.filter(is_published=True):
                    if access_service.can_access(request.user, module):
                        modules.append(
                            {
                                "module": module,
                                "percent": progress_service.module_percent(request.user, module),
                            }
                        )
            rows.append(
                {
                    "course": course,
                    "stats": progress_service.course_stats(request.user, course),
                    "modules": modules,
                    "coming_soon": coming_soon,
                }
            )
        return render(request, "dashboard/progress.html", {"rows": rows})
