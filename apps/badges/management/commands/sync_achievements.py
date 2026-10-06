"""Backfill activity calendar + evaluate badges from existing ExerciseAttempt data."""

from __future__ import annotations

from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
from django.utils import timezone

from apps.badges.catalog import ensure_badges
from apps.badges.services import service as badge_service
from apps.exercises.models import ExerciseAttempt
from apps.social.models import UserActivity

User = get_user_model()


class Command(BaseCommand):
    help = (
        "Sync badge catalog, rebuild UserActivity from historical correct attempts, "
        "and evaluate badges for all active students (idempotent)."
    )

    def add_arguments(self, parser):
        parser.add_argument(
            "--skip-activity",
            action="store_true",
            help="Do not rebuild activity calendar from attempts",
        )
        parser.add_argument(
            "--user",
            type=str,
            default="",
            help="Only process one username/email",
        )

    def handle(self, *args, **options):
        n = ensure_badges()
        self.stdout.write(self.style.SUCCESS(f"Badge catalog upserted: {n} definitions"))

        users = User.objects.filter(is_active=True, role=User.Role.STUDENT)
        if options["user"]:
            key = options["user"]
            users = users.filter(username=key) | User.objects.filter(email__iexact=key)
        users = list(users.distinct())
        self.stdout.write(f"Evaluating {len(users)} user(s)…")

        if not options["skip_activity"]:
            rebuilt = self._rebuild_activity(users)
            self.stdout.write(self.style.SUCCESS(f"Activity days touched: {rebuilt}"))

        awarded = 0
        for user in users:
            newly = badge_service.evaluate(user, trigger="all")
            awarded += len(newly)
            if newly:
                self.stdout.write(f"  {user.username}: +{len(newly)} badge(s)")

        self.stdout.write(self.style.SUCCESS(f"Done. Newly awarded this run: {awarded}"))

    def _rebuild_activity(self, users) -> int:
        """Aggregate historical correct solves into UserActivity (exercise/quiz)."""
        touched = 0
        user_ids = [u.pk for u in users]
        rows = (
            ExerciseAttempt.objects.filter(
                student_id__in=user_ids,
                is_correct=True,
                exercise__is_published=True,
            )
            .select_related("exercise")
            .only("student_id", "created_at", "exercise__is_skill_test")
        )
        # Group by student + local date + kind
        from collections import defaultdict

        day_counts: dict[tuple[int, object, str], int] = defaultdict(int)
        for a in rows.iterator(chunk_size=1000):
            day = timezone.localtime(a.created_at).date()
            kind = (
                UserActivity.ActivityType.QUIZ
                if a.exercise.is_skill_test
                else UserActivity.ActivityType.EXERCISE
            )
            day_counts[(a.student_id, day, kind)] += 1

        for (uid, day, kind), count in day_counts.items():
            obj, _ = UserActivity.objects.update_or_create(
                user_id=uid,
                date=day,
                activity_type=kind,
                defaults={"count": count},
            )
            # Ensure count is at least historical (don't shrink if live system added more)
            if obj.count < count:
                obj.count = count
                obj.save(update_fields=["count"])
            touched += 1
        return touched
