"""Presence via cache heartbeat (Redis or LocMem). No per-second DB writes."""

from __future__ import annotations

from django.conf import settings
from django.core.cache import cache

PRESENCE_KEY = "social:presence:{user_id}"


def presence_timeout() -> int:
    return int(getattr(settings, "SOCIAL_PRESENCE_TIMEOUT_SECONDS", 30))


def _key(user_id: int) -> str:
    return PRESENCE_KEY.format(user_id=int(user_id))


def heartbeat(user_id: int) -> None:
    """Mark user online for SOCIAL_PRESENCE_TIMEOUT_SECONDS."""
    timeout = presence_timeout()
    cache.set(_key(user_id), 1, timeout=max(timeout, 5))


def is_online(user_id: int) -> bool:
    return bool(cache.get(_key(user_id)))


def presence_status(*, viewer, target, blocked: bool = False) -> str:
    """
    Return: online | offline | blocked
    Does not expose exact last-seen timestamps.
    """
    if blocked:
        return "blocked"
    if viewer is not None and getattr(viewer, "is_authenticated", False) and viewer.pk == target.pk:
        return "online" if is_online(target.pk) else "offline"
    return "online" if is_online(target.pk) else "offline"
