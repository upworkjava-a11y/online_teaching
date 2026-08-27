"""Mashqdan keyin keyingi masala / dars navigatsiyasi."""

from django.db.models import Q

from apps.access.services import access_service

from .models import Exercise


def next_exercise_for(user, exercise: Exercise) -> Exercise | None:
    """Bir xil dars ichida, keyin modul ichida keyingi ochiq mashq."""
    candidates = []
    if exercise.lecture_id:
        lecture_next = (
            Exercise.objects.filter(
                lecture_id=exercise.lecture_id,
                is_published=True,
            )
            .filter(Q(order__gt=exercise.order) | Q(order=exercise.order, id__gt=exercise.pk))
            .order_by("order", "id")
            .first()
        )
        if lecture_next:
            candidates.append(lecture_next)

    module_next = (
        Exercise.objects.filter(
            module_id=exercise.module_id,
            is_published=True,
        )
        .filter(Q(order__gt=exercise.order) | Q(order=exercise.order, id__gt=exercise.pk))
        .order_by("order", "id")
        .first()
    )
    if module_next and module_next not in candidates:
        candidates.append(module_next)

    for candidate in candidates:
        if access_service.can_access(user, candidate):
            return candidate
    return None


def next_lecture_for(user, exercise: Exercise):
    lecture = exercise.lecture
    if not lecture:
        return None
    nxt = lecture.get_next()
    if nxt and access_service.can_access(user, nxt):
        return nxt
    return None


def exercise_nav_context(user, exercise: Exercise) -> dict:
    return {
        "next_exercise": next_exercise_for(user, exercise),
        "next_lecture": next_lecture_for(user, exercise),
    }
