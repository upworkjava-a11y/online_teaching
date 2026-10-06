"""1-to-1 chat with rate limits and block enforcement."""

from __future__ import annotations

import hashlib
import time

from django.conf import settings
from django.core.cache import cache
from django.db import transaction
from django.db.models import Count, OuterRef, Prefetch, Subquery
from django.db.models.functions import Coalesce
from django.utils import timezone

from apps.social.models import Conversation, ConversationParticipant, Message, conversation_pair_key
from apps.social.services.relations import SocialRelationError, is_blocked_either


class ChatError(SocialRelationError):
    pass


def _max_len() -> int:
    return int(getattr(settings, "SOCIAL_MESSAGE_MAX_LENGTH", 1000))


def _rate_minute() -> int:
    return int(getattr(settings, "SOCIAL_MESSAGE_RATE_PER_MINUTE", 20))


def _rate_hour() -> int:
    return int(getattr(settings, "SOCIAL_MESSAGE_RATE_PER_HOUR", 200))


def _min_interval() -> float:
    return float(getattr(settings, "SOCIAL_MESSAGE_MIN_INTERVAL_SECONDS", 1.0))


def _page_size() -> int:
    return int(getattr(settings, "SOCIAL_CHAT_PAGE_SIZE", 30))


def _check_rate_limit(user_id: int, text: str) -> None:
    now = time.time()
    last_key = f"social:msg:last:{user_id}"
    last = cache.get(last_key)
    if last is not None and (now - float(last)) < _min_interval():
        raise ChatError("Juda tez yozdingiz. Biroz kuting.", "rate")

    digest = hashlib.sha256(text.strip().encode("utf-8")).hexdigest()[:16]
    dup_key = f"social:msg:dup:{user_id}:{digest}"
    if cache.get(dup_key):
        raise ChatError("Bir xil xabarni qayta-qayta yubormang.", "duplicate_text")

    minute_key = f"social:msg:m:{user_id}"
    hour_key = f"social:msg:h:{user_id}"
    minute_count = int(cache.get(minute_key) or 0)
    hour_count = int(cache.get(hour_key) or 0)
    if minute_count >= _rate_minute():
        raise ChatError("Daqiqada juda ko‘p xabar. Keyinroq urinib ko‘ring.", "rate_minute")
    if hour_count >= _rate_hour():
        raise ChatError("Soatda juda ko‘p xabar. Keyinroq urinib ko‘ring.", "rate_hour")

    cache.set(last_key, now, timeout=60)
    cache.set(dup_key, 1, timeout=10)
    if not cache.add(minute_key, 1, timeout=60):
        try:
            cache.incr(minute_key)
        except ValueError:
            cache.set(minute_key, minute_count + 1, timeout=60)
    if not cache.add(hour_key, 1, timeout=3600):
        try:
            cache.incr(hour_key)
        except ValueError:
            cache.set(hour_key, hour_count + 1, timeout=3600)


@transaction.atomic
def get_or_create_conversation(user_a, user_b) -> Conversation:
    if user_a.pk == user_b.pk:
        raise ChatError("O‘zingizga xabar yozolmaysiz.", "self")
    if is_blocked_either(user_a.pk, user_b.pk):
        raise ChatError("Bu foydalanuvchi bilan yozishish mumkin emas.", "blocked")

    pair = conversation_pair_key(user_a.pk, user_b.pk)
    conversation, created = Conversation.objects.get_or_create(pair_key=pair)
    for user in (user_a, user_b):
        ConversationParticipant.objects.get_or_create(conversation=conversation, user=user)
    return conversation


def user_can_access(conversation: Conversation, user) -> bool:
    return ConversationParticipant.objects.filter(conversation=conversation, user=user).exists()


def other_participant(conversation: Conversation, user):
    return (
        conversation.participants.exclude(pk=user.pk)
        .select_related("social_profile")
        .first()
    )


@transaction.atomic
def send_message(sender, conversation: Conversation, text: str) -> Message:
    text = (text or "").strip()
    if not text:
        raise ChatError("Xabar bo‘sh bo‘lmasin.", "empty")
    if len(text) > _max_len():
        raise ChatError(f"Xabar {_max_len()} belgidan oshmasin.", "too_long")
    if not user_can_access(conversation, sender):
        raise ChatError("Bu suhbatga ruxsat yo‘q.", "forbidden")

    other = other_participant(conversation, sender)
    if other is None:
        raise ChatError("Suhbat topilmadi.", "missing")
    if is_blocked_either(sender.pk, other.pk):
        raise ChatError("Bu foydalanuvchi bilan yozishish mumkin emas.", "blocked")

    _check_rate_limit(sender.pk, text)

    message = Message.objects.create(
        conversation=conversation,
        sender=sender,
        text=text,
    )
    Conversation.objects.filter(pk=conversation.pk).update(updated_at=timezone.now())
    return message


def mark_conversation_read(conversation: Conversation, user) -> int:
    now = timezone.now()
    ConversationParticipant.objects.filter(conversation=conversation, user=user).update(
        last_read_at=now
    )
    return (
        Message.objects.filter(conversation=conversation, read_at__isnull=True)
        .exclude(sender=user)
        .update(read_at=now)
    )


def conversation_messages(conversation: Conversation, *, before_id: int | None = None, limit: int | None = None):
    limit = limit or _page_size()
    qs = (
        Message.objects.filter(conversation=conversation)
        .select_related("sender")
        .order_by("-created_at")
    )
    if before_id:
        qs = qs.filter(id__lt=before_id)
    rows = list(qs[: limit + 1])
    has_more = len(rows) > limit
    rows = rows[:limit]
    rows.reverse()
    return rows, has_more


def list_conversations_for(user):
    User = user.__class__
    latest = (
        Message.objects.filter(conversation_id=OuterRef("pk"))
        .order_by("-created_at")
        .values("text")[:1]
    )
    latest_at = (
        Message.objects.filter(conversation_id=OuterRef("pk"))
        .order_by("-created_at")
        .values("created_at")[:1]
    )
    unread = (
        Message.objects.filter(conversation_id=OuterRef("pk"), read_at__isnull=True)
        .exclude(sender=user)
        .order_by()
        .values("conversation")
        .annotate(c=Count("id"))
        .values("c")[:1]
    )
    return (
        Conversation.objects.filter(participants=user)
        .annotate(
            last_text=Subquery(latest),
            last_at=Subquery(latest_at),
            unread_count=Subquery(unread),
        )
        .prefetch_related(
            Prefetch(
                "participants",
                queryset=User.objects.select_related("social_profile"),
            )
        )
        .order_by(Coalesce("last_at", "updated_at").desc())
    )


def unread_total(user) -> int:
    return (
        Message.objects.filter(
            conversation__participants=user,
            read_at__isnull=True,
        )
        .exclude(sender=user)
        .count()
    )
