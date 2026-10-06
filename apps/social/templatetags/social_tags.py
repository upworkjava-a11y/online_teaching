from django import template

from apps.social.services.avatar import resolve_avatar_url
from apps.social.services.chat import unread_total
from apps.social.services.presence import presence_status

register = template.Library()


@register.simple_tag
def user_avatar_url(user):
    if not user:
        return ""
    return resolve_avatar_url(user)


@register.simple_tag(takes_context=True)
def user_presence(context, user):
    request = context.get("request")
    viewer = getattr(request, "user", None) if request else None
    if not user:
        return "offline"
    blocked = False
    if viewer and getattr(viewer, "is_authenticated", False) and viewer.pk != user.pk:
        from apps.social.services.relations import is_blocked_either

        blocked = is_blocked_either(viewer.pk, user.pk)
    return presence_status(viewer=viewer, target=user, blocked=blocked)


@register.simple_tag(takes_context=True)
def unread_messages_count(context):
    request = context.get("request")
    user = getattr(request, "user", None) if request else None
    if not user or not user.is_authenticated:
        return 0
    return unread_total(user)


@register.inclusion_tag("social/partials/presence_dot.html")
def presence_dot(status: str):
    return {"status": status or "offline"}
