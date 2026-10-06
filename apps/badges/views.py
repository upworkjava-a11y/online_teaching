"""Badge views: gallery, detail partial, toast pop."""

from __future__ import annotations

from django.contrib.auth import get_user_model
from django.http import Http404, JsonResponse
from django.shortcuts import get_object_or_404, render
from django.views import View

from apps.badges.models import Badge
from apps.badges.services import service as badge_service
from apps.core.views import GuestBrowseMixin, RoleRequiredMixin
from apps.social.services.relations import is_blocked_either

User = get_user_model()


class AchievementsView(GuestBrowseMixin, View):
    allowed_roles = ("student", "teacher", "admin")

    def get(self, request, username):
        profile_user = get_object_or_404(User.objects.filter(is_active=True), username=username)
        if (
            request.user.is_authenticated
            and request.user.pk != profile_user.pk
            and is_blocked_either(request.user.pk, profile_user.pk)
        ):
            raise Http404()
        # Historical solves (imports) create progress but not UserBadge rows.
        # Re-evaluate for the profile owner so 1/1 is never stuck locked.
        if request.user.is_authenticated and request.user.pk == profile_user.pk:
            badge_service.evaluate(profile_user, trigger="all")
        rows = badge_service.all_progress(profile_user)
        earned = sum(1 for r in rows if r.earned)
        return render(
            request,
            "badges/achievements.html",
            {
                "profile_user": profile_user,
                "rows": rows,
                "earned_count": earned,
                "total_count": len(rows),
                "is_self": request.user.is_authenticated and request.user.pk == profile_user.pk,
            },
        )


class BadgeDetailPartialView(GuestBrowseMixin, View):
    allowed_roles = ("student", "teacher", "admin")

    def get(self, request, username, slug):
        profile_user = get_object_or_404(User.objects.filter(is_active=True), username=username)
        if (
            request.user.is_authenticated
            and request.user.pk != profile_user.pk
            and is_blocked_either(request.user.pk, profile_user.pk)
        ):
            raise Http404()
        badge = get_object_or_404(Badge, slug=slug, is_active=True)
        earned_map = badge_service.user_badge_map(profile_user)
        ub = earned_map.get(badge.pk)
        current = badge_service.progress_value(profile_user, badge)
        target = 7 if badge.requirement_type == Badge.RequirementType.PERFECT_WEEK else badge.requirement_value
        progress = badge_service.BadgeProgress(
            badge=badge,
            current=min(current, target),
            target=target,
            earned=ub is not None,
            earned_at=ub.earned_at if ub else None,
        )
        return render(
            request,
            "badges/partials/badge_detail.html",
            {"profile_user": profile_user, "progress": progress},
        )


class BadgeToastPopView(RoleRequiredMixin, View):
    allowed_roles = ("student", "teacher", "admin")

    def get(self, request):
        items = badge_service.pop_toasts(request.user.pk)
        return JsonResponse({"badges": items})
