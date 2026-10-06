"""Follow / unfollow / block with atomic uniqueness."""

from __future__ import annotations

from django.db import IntegrityError, transaction
from django.db.models import Q

from apps.social.models import Block, Follow


class SocialRelationError(Exception):
    def __init__(self, message: str, code: str = "error"):
        super().__init__(message)
        self.message = message
        self.code = code


def is_blocked_either(user_a_id: int, user_b_id: int) -> bool:
    return Block.objects.filter(
        Q(blocker_id=user_a_id, blocked_id=user_b_id)
        | Q(blocker_id=user_b_id, blocked_id=user_a_id)
    ).exists()


def is_blocking(blocker_id: int, blocked_id: int) -> bool:
    return Block.objects.filter(blocker_id=blocker_id, blocked_id=blocked_id).exists()


def is_following(follower_id: int, following_id: int) -> bool:
    return Follow.objects.filter(follower_id=follower_id, following_id=following_id).exists()


def followers_count(user_id: int) -> int:
    return Follow.objects.filter(following_id=user_id).count()


def following_count(user_id: int) -> int:
    return Follow.objects.filter(follower_id=user_id).count()


@transaction.atomic
def follow(follower, following) -> Follow:
    if follower.pk == following.pk:
        raise SocialRelationError("O‘zingizni kuzata olmaysiz.", "self")
    if is_blocked_either(follower.pk, following.pk):
        raise SocialRelationError("Bu foydalanuvchi bilan aloqa yopilgan.", "blocked")
    try:
        obj, _ = Follow.objects.get_or_create(follower=follower, following=following)
    except IntegrityError as exc:
        raise SocialRelationError("Allaqachon kuzatyapsiz.", "duplicate") from exc
    return obj


@transaction.atomic
def unfollow(follower, following) -> bool:
    deleted, _ = Follow.objects.filter(follower=follower, following=following).delete()
    return deleted > 0


@transaction.atomic
def block(blocker, blocked) -> Block:
    if blocker.pk == blocked.pk:
        raise SocialRelationError("O‘zingizni bloklay olmaysiz.", "self")
    Follow.objects.filter(
        Q(follower=blocker, following=blocked) | Q(follower=blocked, following=blocker)
    ).delete()
    obj, _ = Block.objects.get_or_create(blocker=blocker, blocked=blocked)
    return obj


@transaction.atomic
def unblock(blocker, blocked) -> bool:
    deleted, _ = Block.objects.filter(blocker=blocker, blocked=blocked).delete()
    return deleted > 0
