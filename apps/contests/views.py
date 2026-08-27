from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.views import View

from apps.access.services import access_service
from apps.core.views import GuestBrowseMixin, RoleRequiredMixin
from apps.exercises.models import ExerciseAttempt

from .models import Contest, ContestExercise, ContestScore
from .services import contest_leaderboard, refresh_contest_score, upcoming_or_recent_contests


class ContestListView(GuestBrowseMixin, View):
    allowed_roles = ("student", "teacher", "admin")

    def get(self, request):
        contests = upcoming_or_recent_contests(limit=20)
        return render(request, "contests/list.html", {"contests": contests})


class ContestDetailView(GuestBrowseMixin, View):
    allowed_roles = ("student", "teacher", "admin")

    def get(self, request, slug):
        contest = get_object_or_404(Contest.objects.prefetch_related("exercises"), slug=slug, is_published=True)
        raw_links = list(
            ContestExercise.objects.filter(contest=contest)
            .select_related("exercise", "exercise__module", "exercise__module__course")
            .order_by("order", "id")
        )
        links = []
        for link in raw_links:
            allowed = access_service.can_access(request.user, link.exercise)
            links.append({"link": link, "allowed": allowed})
        my_score = None
        solved_ids = set()
        if request.user.is_authenticated and getattr(request.user, "is_student", False):
            refresh_contest_score(contest, request.user)
            my_score = ContestScore.objects.filter(contest=contest, student=request.user).first()
            exercise_ids = [row["link"].exercise_id for row in links]
            solved_ids = set(
                ExerciseAttempt.objects.filter(
                    student=request.user,
                    exercise_id__in=exercise_ids,
                    is_correct=True,
                    created_at__gte=contest.starts_at,
                    created_at__lte=contest.ends_at,
                ).values_list("exercise_id", flat=True)
            )
        board = contest_leaderboard(contest, limit=30)
        return render(
            request,
            "contests/detail.html",
            {
                "contest": contest,
                "links": links,
                "board": board,
                "my_score": my_score,
                "solved_ids": solved_ids,
            },
        )
