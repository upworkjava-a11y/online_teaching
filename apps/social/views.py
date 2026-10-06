"""Social views: profile, chat, follow/block, presence, activity HTMX."""

from __future__ import annotations

import datetime as dt

from django.core.exceptions import ValidationError
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.http import Http404, HttpResponse, HttpResponseBadRequest, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views import View

from apps.core.views import GuestBrowseMixin, RoleRequiredMixin
from apps.progress.streak import get_streak
from apps.social.profile_data import course_progress_rows, profile_bio, recent_learning_items
from apps.social.forms import AvatarPresetForm, AvatarUploadForm, MessageForm, ProfileBioForm
from apps.social.models import Conversation, Follow
from apps.social.services import activity as activity_svc
from apps.social.services import avatar as avatar_svc
from apps.social.services import chat as chat_svc
from apps.social.services import presence as presence_svc
from apps.social.services.relations import (
    SocialRelationError,
    block,
    followers_count,
    following_count,
    is_blocked_either,
    is_blocking,
    is_following,
    follow,
    unblock,
    unfollow,
)

User = get_user_model()


def _profile_user(username: str):
    return get_object_or_404(
        User.objects.select_related("social_profile", "streak").filter(is_active=True),
        username=username,
    )


def _viewer_blocked(viewer, target) -> bool:
    if not viewer or not getattr(viewer, "is_authenticated", False):
        return False
    if viewer.pk == target.pk:
        return False
    return is_blocked_either(viewer.pk, target.pk)


class PublicProfileView(GuestBrowseMixin, View):
    allowed_roles = ("student", "teacher", "admin")

    def get(self, request, username):
        profile_user = _profile_user(username)
        viewer = request.user if request.user.is_authenticated else None
        blocked = False
        i_block = False
        they_block = False
        following = False
        if viewer and viewer.is_authenticated:
            blocked = is_blocked_either(viewer.pk, profile_user.pk)
            i_block = is_blocking(viewer.pk, profile_user.pk)
            they_block = is_blocking(profile_user.pk, viewer.pk)
            following = is_following(viewer.pk, profile_user.pk)

        if blocked and viewer and viewer.pk != profile_user.pk:
            return render(
                request,
                "social/profile_blocked.html",
                {
                    "profile_user": profile_user,
                    "avatar_url": avatar_svc.resolve_avatar_url(profile_user),
                    "i_block": i_block,
                    "they_block": they_block,
                    "blocked": True,
                    "is_self": False,
                },
                status=403,
            )

        year = int(request.GET.get("year") or dt.date.today().year)
        cal = activity_svc.year_calendar(profile_user, year)
        streak = getattr(profile_user, "streak", None) or get_streak(profile_user)
        status = presence_svc.presence_status(
            viewer=viewer,
            target=profile_user,
            blocked=blocked and viewer is not None and viewer.pk != profile_user.pk,
        )
        bio = profile_bio(profile_user)

        badge_rows = []
        badge_earned = 0
        badge_total = 0
        badge_showcase = []
        try:
            from apps.badges.services import service as badge_service

            if viewer is not None and viewer.pk == profile_user.pk:
                badge_service.evaluate(profile_user, trigger="all")
            badge_rows = badge_service.all_progress(profile_user)
            badge_earned = sum(1 for r in badge_rows if r.earned)
            badge_total = len(badge_rows)
            earned_rows = [r for r in badge_rows if r.earned][:8]
            if len(earned_rows) < 6:
                locked = [r for r in badge_rows if not r.earned][: 6 - len(earned_rows)]
                badge_showcase = earned_rows + locked
            else:
                badge_showcase = earned_rows
        except Exception:
            pass

        return render(
            request,
            "social/profile.html",
            {
                "profile_user": profile_user,
                "avatar_url": avatar_svc.resolve_avatar_url(profile_user),
                "bio": bio,
                "presence_status": status,
                "followers": followers_count(profile_user.pk),
                "following": following_count(profile_user.pk),
                "is_self": viewer is not None and viewer.pk == profile_user.pk,
                "is_following": following,
                "i_block": i_block,
                "they_block": they_block,
                "blocked": blocked,
                "calendar": cal,
                "streak": streak,
                "can_message": bool(
                    viewer
                    and viewer.is_authenticated
                    and viewer.pk != profile_user.pk
                    and not blocked
                ),
                "badge_earned": badge_earned,
                "badge_total": badge_total,
                "badge_showcase": badge_showcase,
                "course_rows": course_progress_rows(profile_user),
                "recent_items": recent_learning_items(profile_user),
            },
        )


class OwnProfileRedirectView(RoleRequiredMixin, View):
    """ /profile/ → /profile/<username>/ """

    allowed_roles = ("student", "teacher", "admin")

    def get(self, request):
        return redirect("social:profile", username=request.user.username)


class ProfileSettingsView(RoleRequiredMixin, View):
    """Unified Edit Profile: account fields + avatar + bio."""

    allowed_roles = ("student", "teacher", "admin")

    def get(self, request):
        from apps.accounts.forms import ProfileForm

        profile = avatar_svc.get_or_create_profile(request.user)
        return render(
            request,
            "social/settings.html",
            {
                "account_form": ProfileForm(instance=request.user),
                "preset_form": AvatarPresetForm(initial={"avatar_preset": profile.avatar_preset}),
                "upload_form": AvatarUploadForm(),
                "bio_form": ProfileBioForm(initial={"bio": profile.bio}),
                "avatar_url": avatar_svc.resolve_avatar_url(request.user),
                "profile": profile,
            },
        )

    def post(self, request):
        from apps.accounts.forms import ProfileForm
        from django.contrib.auth import update_session_auth_hash

        profile = avatar_svc.get_or_create_profile(request.user)
        action = request.POST.get("action") or "account"
        try:
            if action == "preset":
                form = AvatarPresetForm(request.POST)
                if form.is_valid():
                    avatar_svc.set_preset_avatar(request.user, form.cleaned_data["avatar_preset"])
                    messages.success(request, "Avatar yangilandi.")
            elif action == "upload":
                form = AvatarUploadForm(request.POST, request.FILES)
                if form.is_valid():
                    avatar_svc.upload_avatar(request.user, form.cleaned_data["avatar"])
                    messages.success(request, "Avatar yuklandi.")
                else:
                    messages.error(request, "Rasmni yuklab bo‘lmadi.")
            elif action == "bio":
                form = ProfileBioForm(request.POST)
                if form.is_valid():
                    profile.bio = form.cleaned_data["bio"]
                    profile.save(update_fields=["bio", "updated_at"])
                    messages.success(request, "Bio saqlandi.")
            else:
                form = ProfileForm(request.POST, instance=request.user)
                if form.is_valid():
                    password_changed = bool(form.cleaned_data.get("new_password1"))
                    user = form.save()
                    if password_changed:
                        update_session_auth_hash(request, user)
                        messages.success(request, "Profil va parol yangilandi.")
                    else:
                        messages.success(request, "Profil yangilandi.")
                    return redirect("social:profile", username=user.username)
                return render(
                    request,
                    "social/settings.html",
                    {
                        "account_form": form,
                        "preset_form": AvatarPresetForm(initial={"avatar_preset": profile.avatar_preset}),
                        "upload_form": AvatarUploadForm(),
                        "bio_form": ProfileBioForm(initial={"bio": profile.bio}),
                        "avatar_url": avatar_svc.resolve_avatar_url(request.user),
                        "profile": profile,
                    },
                )
        except ValidationError as exc:
            messages.error(request, "; ".join(exc.messages) if hasattr(exc, "messages") else str(exc))
        except Exception as exc:  # noqa: BLE001
            messages.error(request, str(getattr(exc, "message", None) or exc))
        return redirect("social:settings")


class FollowToggleView(RoleRequiredMixin, View):
    allowed_roles = ("student", "teacher", "admin")

    def post(self, request, username):
        target = _profile_user(username)
        action = request.POST.get("action", "follow")
        try:
            if action == "unfollow":
                unfollow(request.user, target)
            else:
                follow(request.user, target)
        except SocialRelationError as exc:
            if request.htmx:
                return HttpResponseBadRequest(exc.message)
            messages.error(request, exc.message)
        if request.htmx:
            return render(
                request,
                "social/partials/follow_button.html",
                {
                    "profile_user": target,
                    "is_following": is_following(request.user.pk, target.pk),
                    "followers": followers_count(target.pk),
                },
            )
        return redirect("social:profile", username=target.username)


class BlockToggleView(RoleRequiredMixin, View):
    allowed_roles = ("student", "teacher", "admin")

    def post(self, request, username):
        target = _profile_user(username)
        action = request.POST.get("action", "block")
        try:
            if action == "unblock":
                unblock(request.user, target)
            else:
                block(request.user, target)
        except SocialRelationError as exc:
            messages.error(request, exc.message)
        return redirect("social:profile", username=target.username)


class StartChatView(RoleRequiredMixin, View):
    allowed_roles = ("student", "teacher", "admin")

    def post(self, request, username):
        target = _profile_user(username)
        try:
            conversation = chat_svc.get_or_create_conversation(request.user, target)
        except chat_svc.ChatError as exc:
            messages.error(request, exc.message)
            return redirect("social:profile", username=target.username)
        return redirect("social:chat_detail", pk=conversation.pk)


class ConversationListView(RoleRequiredMixin, View):
    allowed_roles = ("student", "teacher", "admin")

    def get(self, request):
        rows = []
        for conv in chat_svc.list_conversations_for(request.user):
            other = next((p for p in conv.participants.all() if p.pk != request.user.pk), None)
            rows.append(
                {
                    "conversation": conv,
                    "other": other,
                    "avatar_url": avatar_svc.resolve_avatar_url(other) if other else "",
                    "presence": presence_svc.presence_status(
                        viewer=request.user,
                        target=other,
                        blocked=is_blocked_either(request.user.pk, other.pk) if other else False,
                    )
                    if other
                    else "offline",
                    "last_text": conv.last_text or "",
                    "unread": int(conv.unread_count or 0),
                }
            )
        return render(
            request,
            "social/inbox.html",
            {"rows": rows, "unread_total": chat_svc.unread_total(request.user)},
        )


class ConversationDetailView(RoleRequiredMixin, View):
    allowed_roles = ("student", "teacher", "admin")

    def get(self, request, pk):
        conversation = get_object_or_404(Conversation.objects.prefetch_related("participants"), pk=pk)
        if not chat_svc.user_can_access(conversation, request.user):
            raise Http404()
        other = chat_svc.other_participant(conversation, request.user)
        if other and is_blocked_either(request.user.pk, other.pk):
            return render(
                request,
                "social/chat_blocked.html",
                {"other": other},
                status=403,
            )
        chat_svc.mark_conversation_read(conversation, request.user)
        msgs, has_more = chat_svc.conversation_messages(conversation)
        return render(
            request,
            "social/chat.html",
            {
                "conversation": conversation,
                "other": other,
                "avatar_url": avatar_svc.resolve_avatar_url(other) if other else "",
                "presence": presence_svc.presence_status(viewer=request.user, target=other)
                if other
                else "offline",
                "chat_messages": msgs,
                "has_more": has_more,
                "form": MessageForm(),
                "oldest_id": msgs[0].pk if msgs else None,
                "latest_id": msgs[-1].pk if msgs else 0,
            },
        )

    def post(self, request, pk):
        conversation = get_object_or_404(Conversation, pk=pk)
        if not chat_svc.user_can_access(conversation, request.user):
            raise Http404()
        form = MessageForm(request.POST)
        if not form.is_valid():
            if request.htmx:
                return HttpResponseBadRequest("Xato")
            messages.error(request, "Xabar yuborilmadi.")
            return redirect("social:chat_detail", pk=pk)
        try:
            msg = chat_svc.send_message(request.user, conversation, form.cleaned_data["text"])
        except chat_svc.ChatError as exc:
            if request.htmx:
                return HttpResponseBadRequest(exc.message)
            messages.error(request, exc.message)
            return redirect("social:chat_detail", pk=pk)
        if request.htmx:
            return render(request, "social/partials/message_bubble.html", {"message": msg, "user": request.user})
        return redirect("social:chat_detail", pk=pk)


class ChatHistoryView(RoleRequiredMixin, View):
    """Older messages for infinite scroll."""

    allowed_roles = ("student", "teacher", "admin")

    def get(self, request, pk):
        conversation = get_object_or_404(Conversation, pk=pk)
        if not chat_svc.user_can_access(conversation, request.user):
            raise Http404()
        other = chat_svc.other_participant(conversation, request.user)
        if other and is_blocked_either(request.user.pk, other.pk):
            raise Http404()
        before = request.GET.get("before")
        before_id = int(before) if before and before.isdigit() else None
        msgs, has_more = chat_svc.conversation_messages(conversation, before_id=before_id)
        return render(
            request,
            "social/partials/message_page.html",
            {
                "messages": msgs,
                "has_more": has_more,
                "oldest_id": msgs[0].pk if msgs else None,
                "conversation": conversation,
                "user": request.user,
            },
        )


class ChatUpdatesView(RoleRequiredMixin, View):
    """Newer messages for HTMX polling (near real-time on hosts without WebSockets)."""

    allowed_roles = ("student", "teacher", "admin")

    def get(self, request, pk):
        conversation = get_object_or_404(Conversation, pk=pk)
        if not chat_svc.user_can_access(conversation, request.user):
            raise Http404()
        other = chat_svc.other_participant(conversation, request.user)
        if other and is_blocked_either(request.user.pk, other.pk):
            raise Http404()
        after = request.GET.get("after")
        after_id = int(after) if after and str(after).isdigit() else 0
        msgs = chat_svc.messages_after(conversation, after_id=after_id)
        if msgs:
            chat_svc.mark_conversation_read(conversation, request.user)
        # Empty body keeps the poller quiet when nothing new arrived.
        if not msgs:
            return HttpResponse("")
        return render(
            request,
            "social/partials/message_updates.html",
            {"messages": msgs, "user": request.user},
        )


class HeartbeatView(RoleRequiredMixin, View):
    allowed_roles = ("student", "teacher", "admin")

    def post(self, request):
        presence_svc.heartbeat(request.user.pk)
        return JsonResponse({"ok": True, "status": "online"})


class PresenceStatusView(RoleRequiredMixin, View):
    allowed_roles = ("student", "teacher", "admin")

    def get(self, request, username):
        target = _profile_user(username)
        blocked = is_blocked_either(request.user.pk, target.pk)
        status = presence_svc.presence_status(
            viewer=request.user, target=target, blocked=blocked
        )
        return JsonResponse({"username": target.username, "status": status})


class ActivityMonthView(GuestBrowseMixin, View):
    allowed_roles = ("student", "teacher", "admin")

    def get(self, request, username):
        profile_user = _profile_user(username)
        if _viewer_blocked(request.user, profile_user):
            raise Http404()
        try:
            year = int(request.GET.get("year") or dt.date.today().year)
            month = int(request.GET.get("month") or dt.date.today().month)
        except ValueError:
            return HttpResponseBadRequest("bad date")
        data = activity_svc.month_calendar(profile_user, year, month)
        return render(
            request,
            "social/partials/activity_month.html",
            {"month_data": data, "profile_user": profile_user},
        )


class ActivityDayView(GuestBrowseMixin, View):
    allowed_roles = ("student", "teacher", "admin")

    def get(self, request, username):
        profile_user = _profile_user(username)
        if _viewer_blocked(request.user, profile_user):
            raise Http404()
        raw = request.GET.get("date") or ""
        try:
            day = dt.date.fromisoformat(raw)
        except ValueError:
            return HttpResponseBadRequest("bad date")
        data = activity_svc.day_breakdown(profile_user, day)
        return render(
            request,
            "social/partials/activity_day.html",
            {"day_data": data, "profile_user": profile_user},
        )


class FollowersListView(GuestBrowseMixin, View):
    allowed_roles = ("student", "teacher", "admin")

    def get(self, request, username):
        profile_user = _profile_user(username)
        if _viewer_blocked(request.user, profile_user):
            raise Http404()
        kind = request.GET.get("kind", "followers")
        if kind == "following":
            qs = (
                Follow.objects.filter(follower=profile_user)
                .select_related("following__social_profile")
                .order_by("-created_at")[:100]
            )
            users = [row.following for row in qs]
            title = "Kuzatayotganlar"
        else:
            qs = (
                Follow.objects.filter(following=profile_user)
                .select_related("follower__social_profile")
                .order_by("-created_at")[:100]
            )
            users = [row.follower for row in qs]
            title = "Kuzatuvchilar"
        cards = []
        for u in users:
            pair_blocked = (
                is_blocked_either(request.user.pk, u.pk)
                if request.user.is_authenticated
                else False
            )
            cards.append(
                {
                    "user": u,
                    "avatar_url": avatar_svc.resolve_avatar_url(u),
                    "presence": presence_svc.presence_status(
                        viewer=request.user,
                        target=u,
                        blocked=pair_blocked,
                    )
                    if request.user.is_authenticated
                    else "offline",
                }
            )
        return render(
            request,
            "social/follow_list.html",
            {"profile_user": profile_user, "cards": cards, "title": title, "kind": kind},
        )

