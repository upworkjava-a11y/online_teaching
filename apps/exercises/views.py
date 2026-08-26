from django.contrib import messages
from django.http import Http404
from django.shortcuts import get_object_or_404, redirect, render
from django.views import View

from apps.access.services import access_service
from apps.core.views import RoleRequiredMixin
from apps.progress.models import CourseProgress

from .models import Exercise, ExerciseAttempt
from .services import RateLimited, exercise_service


class ExerciseDetailView(RoleRequiredMixin, View):
    allowed_roles = ("student",)
    template_name = "exercises/detail.html"

    def get_exercise(self, request, pk):
        exercise = get_object_or_404(
            Exercise.objects.select_related("module", "module__course", "lecture", "expected_result"),
            pk=pk,
        )
        decision = access_service.evaluate(request.user, exercise)
        if not decision.allowed:
            return None, decision
        if not exercise.is_published and decision.code != "explicit_allow":
            return None, decision
        return exercise, decision

    def get(self, request, pk):
        exercise, decision = self.get_exercise(request, pk)
        if exercise is None:
            return render(request, "core/blocked.html", {"reason": decision.reason}, status=403)
        attempts = ExerciseAttempt.objects.filter(student=request.user, exercise=exercise)[:10]
        if exercise.kind == Exercise.Kind.QUIZ:
            last_sql = attempts[0].sql_query if attempts else ""
        else:
            last_sql = attempts[0].sql_query if attempts else "SELECT "
        CourseProgress.objects.update_or_create(
            student=request.user,
            course=exercise.course,
            defaults={},
        )
        return render(
            request,
            self.template_name,
            {
                "exercise": exercise,
                "attempts": attempts,
                "last_sql": last_sql,
                "datasets": exercise.datasets.all(),
                "latest_attempt": attempts[0] if attempts else None,
            },
        )

    def post(self, request, pk):
        exercise, decision = self.get_exercise(request, pk)
        if exercise is None:
            return render(request, "core/blocked.html", {"reason": decision.reason}, status=403)
        if exercise.kind == Exercise.Kind.QUIZ:
            submission = request.POST.get("answer", "")
        else:
            submission = request.POST.get("sql", "")
        try:
            attempt = exercise_service.run(request.user, exercise, submission)
        except RateLimited as exc:
            messages.error(request, exc.message)
            return redirect("exercises:detail", pk=exercise.pk)

        attempts = ExerciseAttempt.objects.filter(student=request.user, exercise=exercise)[:10]
        context = {
            "exercise": exercise,
            "attempts": attempts,
            "last_sql": submission,
            "datasets": exercise.datasets.all(),
            "latest_attempt": attempt,
        }
        if request.htmx:
            return render(request, "exercises/partials/result.html", context)
        return render(request, self.template_name, context)
