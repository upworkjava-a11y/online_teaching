from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.views import View

from apps.access.services import access_service
from apps.core.views import RoleRequiredMixin
from apps.exercises.models import ExerciseAttempt
from apps.progress.models import LectureProgress
from apps.progress.services import progress_service

from .models import Course


class CourseListView(RoleRequiredMixin, View):
    allowed_roles = ("student",)

    def get(self, request):
        courses = Course.objects.all().order_by("order")
        visible = []
        for course in courses:
            decision = access_service.evaluate(request.user, course)
            coming_soon = (
                course.is_published
                and course.is_visible
                and not access_service.is_course_open(course)
                and not (request.user.is_admin or request.user.is_teacher)
            )
            visible.append(
                {
                    "course": course,
                    "decision": decision,
                    "coming_soon": coming_soon or decision.code == "coming_soon",
                    "stats": progress_service.course_stats(request.user, course),
                    "full_access": access_service.has_full_course_access(request.user, course)
                    if decision.allowed and not coming_soon
                    else False,
                }
            )
        return render(request, "courses/list.html", {"courses": visible})


class CourseDetailView(RoleRequiredMixin, View):
    allowed_roles = ("student",)

    def get(self, request, slug):
        course = get_object_or_404(
            Course.objects.prefetch_related("modules__lectures__practice_exercises", "modules__exercises"),
            slug=slug,
        )
        decision = access_service.evaluate(request.user, course)
        if not decision.allowed:
            return render(
                request,
                "courses/blocked.html",
                {"course": course, "decision": decision},
                status=403,
            )
        completed_ids = set(
            LectureProgress.objects.filter(student=request.user, completed=True).values_list("lecture_id", flat=True)
        )
        solved_ids = set(
            ExerciseAttempt.objects.filter(student=request.user, is_correct=True).values_list("exercise_id", flat=True)
        )
        full_access = access_service.has_full_course_access(request.user, course)
        preview_ids = access_service.preview_module_ids(course)
        modules = []
        for module in course.modules.all():
            module_decision = access_service.evaluate(request.user, module)
            lectures = []
            for lecture in module.lectures.all():
                lecture_decision = access_service.evaluate(request.user, lecture)
                practices = [ex for ex in lecture.practice_exercises.all() if ex.is_published]
                practice = practices[0] if practices else None
                lecture_done = lecture.pk in completed_ids
                solved_practice = sum(1 for ex in practices if ex.pk in solved_ids)
                all_practice_done = not practices or solved_practice == len(practices)
                if lecture_done and all_practice_done:
                    status = "done"
                elif lecture_done or solved_practice:
                    status = "partial"
                else:
                    status = "open"
                lectures.append(
                    {
                        "lecture": lecture,
                        "decision": lecture_decision,
                        "completed": lecture_done and all_practice_done,
                        "status": status,
                        "practice_left": bool(practices) and solved_practice < len(practices),
                        "practice": practice,
                        "practices": practices,
                    }
                )
            exercises = []
            for exercise in module.exercises.all():
                if exercise.lecture_id:
                    continue
                exercises.append(
                    {
                        "exercise": exercise,
                        "allowed": access_service.can_access(request.user, exercise),
                        "solved": exercise.pk in solved_ids,
                    }
                )
            modules.append(
                {
                    "module": module,
                    "decision": module_decision,
                    "percent": progress_service.module_percent(request.user, module) if module_decision.allowed else 0,
                    "lectures": lectures,
                    "exercises": exercises,
                    "premium_locked": (
                        module_decision.allowed
                        and not full_access
                        and module.is_published
                        and module.pk not in preview_ids
                    ),
                }
            )
        if not decision.allowed:
            raise Http404()
        return render(
            request,
            "courses/detail.html",
            {
                "course": course,
                "modules": modules,
                "stats": progress_service.course_stats(request.user, course),
                "full_access": full_access,
            },
        )
