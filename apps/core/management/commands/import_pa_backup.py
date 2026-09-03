"""
Import student accounts + progress from an old PythonAnywhere SQLite dump
into the current local/platform database.

Preserves password hashes (students keep the same login password).
Maps content by slug (courses/modules/lectures/exercises).

Example:
  set DJANGO_SETTINGS_MODULE=config.settings.local
  python manage.py import_pa_backup ^
    --platform "C:\\Users\\Asus Tuf A16\\Downloads\\pa_platform.sqlite3" ^
    --sandbox "C:\\Users\\Asus Tuf A16\\Downloads\\pa_sandbox.sqlite3"
"""

from __future__ import annotations

import json
import shutil
import sqlite3
from pathlib import Path

from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
from django.db import transaction
from django.utils import timezone
from django.utils.dateparse import parse_datetime


def _row_dicts(cur, sql: str, params=()):
    cur.execute(sql, params)
    cols = [d[0] for d in cur.description]
    for row in cur.fetchall():
        yield dict(zip(cols, row))


def _parse_dt(value):
    if not value:
        return None
    if hasattr(value, "isoformat"):
        dt = value
    else:
        text = str(value).replace(" ", "T", 1)
        dt = parse_datetime(text) or parse_datetime(str(value))
    if dt is None:
        return None
    if timezone.is_naive(dt):
        return timezone.make_aware(dt, timezone.get_current_timezone())
    return dt


def _json_load(value, default=None):
    if value is None or value == "":
        return {} if default is None else default
    if isinstance(value, (dict, list)):
        return value
    try:
        return json.loads(value)
    except (TypeError, json.JSONDecodeError):
        return {} if default is None else default


class Command(BaseCommand):
    help = "Import users/passwords/scores/progress from an old PA SQLite dump."

    def add_arguments(self, parser):
        parser.add_argument(
            "--platform",
            required=True,
            help="Path to old pa_platform.sqlite3",
        )
        parser.add_argument(
            "--sandbox",
            default="",
            help="Optional path to old pa_sandbox.sqlite3 (copied over local sandbox)",
        )
        parser.add_argument(
            "--dry-run",
            action="store_true",
            help="Show counts only; do not write",
        )
        parser.add_argument(
            "--skip-demo-overwrite",
            action="store_true",
            help="Do not overwrite password hashes for *@example.com demo accounts",
        )

    def handle(self, *args, **options):
        platform_path = Path(options["platform"]).expanduser().resolve()
        if not platform_path.exists():
            raise CommandError(f"Platform DB not found: {platform_path}")

        sandbox_path = options["sandbox"].strip()
        dry_run = options["dry_run"]
        skip_demo = options["skip_demo_overwrite"]

        self.stdout.write(f"Source platform: {platform_path}")
        self.stdout.write(f"Target DB: {settings.DATABASES['default']['NAME']}")

        old = sqlite3.connect(str(platform_path))
        old.row_factory = sqlite3.Row
        cur = old.cursor()

        try:
            summary = self._import_all(cur, dry_run=dry_run, skip_demo=skip_demo)
        finally:
            old.close()

        if sandbox_path:
            self._copy_sandbox(Path(sandbox_path).expanduser().resolve(), dry_run=dry_run)

        self.stdout.write(self.style.SUCCESS("Import finished."))
        for key, value in summary.items():
            self.stdout.write(f"  {key}: {value}")

    def _copy_sandbox(self, src: Path, *, dry_run: bool):
        if not src.exists():
            raise CommandError(f"Sandbox DB not found: {src}")
        dest = Path(settings.SANDBOX_DATABASE["NAME"])
        self.stdout.write(f"Sandbox copy: {src} -> {dest}")
        if dry_run:
            return
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dest)

    def _import_all(self, cur, *, dry_run: bool, skip_demo: bool) -> dict:
        from apps.accounts.models import StudentProfile, TeacherProfile, User
        from apps.contests.models import Contest, ContestScore
        from apps.courses.models import Course, CourseEnrollment, Lecture, Module
        from apps.exercises.models import Exercise, ExerciseAttempt, ExerciseComment
        from apps.progress.models import Certificate, CourseProgress, LectureProgress, StudentStreak

        course_by_slug = {c.slug: c for c in Course.objects.all()}
        module_by_slug = {m.slug: m for m in Module.objects.select_related("course")}
        lecture_by_slug = {lec.slug: lec for lec in Lecture.objects.select_related("module")}
        exercise_by_slug = {ex.slug: ex for ex in Exercise.objects.select_related("module")}
        contest_by_slug = {c.slug: c for c in Contest.objects.all()}

        old_ex_id_to_slug = {
            row["id"]: row["slug"] for row in _row_dicts(cur, "SELECT id, slug FROM exercises_exercise")
        }
        old_lec_id_to_slug = {
            row["id"]: row["slug"] for row in _row_dicts(cur, "SELECT id, slug FROM courses_lecture")
        }
        old_course_id_to_slug = {
            row["id"]: row["slug"] for row in _row_dicts(cur, "SELECT id, slug FROM courses_course")
        }
        old_module_id_to_slug = {
            row["id"]: row["slug"] for row in _row_dicts(cur, "SELECT id, slug FROM courses_module")
        }
        old_contest_id_to_slug = {
            row["id"]: row["slug"] for row in _row_dicts(cur, "SELECT id, slug FROM contests_contest")
        }

        summary = {
            "users_upserted": 0,
            "users_skipped_demo_password": 0,
            "student_profiles": 0,
            "teacher_profiles": 0,
            "teacher_course_links": 0,
            "enrollments": 0,
            "attempts": 0,
            "attempts_skipped_missing_exercise": 0,
            "comments": 0,
            "lecture_progress": 0,
            "course_progress": 0,
            "certificates": 0,
            "streaks": 0,
            "contest_scores": 0,
        }

        if dry_run:
            summary["users_upserted"] = cur.execute("SELECT COUNT(*) FROM accounts_user").fetchone()[0]
            summary["attempts"] = cur.execute("SELECT COUNT(*) FROM exercises_exerciseattempt").fetchone()[0]
            return summary

        with transaction.atomic():
            user_by_old_id: dict[int, User] = {}

            for row in _row_dicts(cur, "SELECT * FROM accounts_user ORDER BY id"):
                email = (row["email"] or "").strip().lower()
                if not email:
                    continue
                defaults = {
                    "username": row["username"],
                    "first_name": row["first_name"] or "",
                    "last_name": row["last_name"] or "",
                    "role": row["role"] or User.Role.STUDENT,
                    "is_staff": bool(row["is_staff"]),
                    "is_superuser": bool(row["is_superuser"]),
                    "is_active": bool(row["is_active"]),
                    "is_blocked": bool(row["is_blocked"]),
                    "is_premium": bool(row["is_premium"]),
                    "last_activity_at": _parse_dt(row["last_activity_at"]),
                    "date_joined": _parse_dt(row["date_joined"]),
                    "last_login": _parse_dt(row["last_login"]),
                }
                # Avoid username collisions when email differs
                if User.objects.filter(username=defaults["username"]).exclude(email__iexact=email).exists():
                    defaults["username"] = email.split("@")[0][:140]

                user, created = User.objects.update_or_create(email=email, defaults=defaults)
                demo = email.endswith("@example.com")
                if not (skip_demo and demo and not created):
                    # Preserve exact hash so old passwords still work.
                    User.objects.filter(pk=user.pk).update(password=row["password"])
                    user.refresh_from_db(fields=["password"])
                else:
                    summary["users_skipped_demo_password"] += 1
                user_by_old_id[row["id"]] = user
                summary["users_upserted"] += 1

            for row in _row_dicts(cur, "SELECT * FROM accounts_studentprofile"):
                user = user_by_old_id.get(row["user_id"])
                if not user:
                    continue
                StudentProfile.objects.update_or_create(
                    user=user,
                    defaults={"bio": row.get("bio") or ""},
                )
                summary["student_profiles"] += 1

            for row in _row_dicts(cur, "SELECT * FROM accounts_teacherprofile"):
                user = user_by_old_id.get(row["user_id"])
                if not user:
                    continue
                profile, _ = TeacherProfile.objects.update_or_create(
                    user=user,
                    defaults={"bio": row.get("bio") or ""},
                )
                summary["teacher_profiles"] += 1
                # assigned courses
                links = list(
                    _row_dicts(
                        cur,
                        "SELECT course_id FROM accounts_teacherprofile_assigned_courses WHERE teacherprofile_id=?",
                        (row["id"],),
                    )
                )
                courses = []
                for link in links:
                    slug = old_course_id_to_slug.get(link["course_id"])
                    course = course_by_slug.get(slug) if slug else None
                    if course:
                        courses.append(course)
                if courses:
                    profile.assigned_courses.set(courses)
                    summary["teacher_course_links"] += len(courses)

            for row in _row_dicts(cur, "SELECT * FROM courses_courseenrollment"):
                user = user_by_old_id.get(row["student_id"])
                slug = old_course_id_to_slug.get(row["course_id"])
                course = course_by_slug.get(slug) if slug else None
                if not user or not course:
                    continue
                CourseEnrollment.objects.update_or_create(
                    student=user,
                    course=course,
                    defaults={},
                )
                summary["enrollments"] += 1

            for row in _row_dicts(cur, "SELECT * FROM exercises_exerciseattempt ORDER BY id"):
                user = user_by_old_id.get(row["student_id"])
                slug = old_ex_id_to_slug.get(row["exercise_id"])
                exercise = exercise_by_slug.get(slug) if slug else None
                if not user or not exercise:
                    summary["attempts_skipped_missing_exercise"] += 1
                    continue
                created_at = _parse_dt(row["created_at"])
                exists = ExerciseAttempt.objects.filter(
                    student=user,
                    exercise=exercise,
                    created_at=created_at,
                    sql_query=row["sql_query"] or "",
                ).exists()
                if exists:
                    continue
                attempt = ExerciseAttempt(
                    student=user,
                    exercise=exercise,
                    sql_query=row["sql_query"] or "",
                    is_correct=bool(row["is_correct"]),
                    score=int(row["score"] or 0),
                    result_preview=_json_load(row["result_preview"]),
                    error_message=row["error_message"] or "",
                    execution_ms=int(row["execution_ms"] or 0),
                )
                attempt.save()
                # Keep original timestamps
                ExerciseAttempt.objects.filter(pk=attempt.pk).update(
                    created_at=created_at,
                    updated_at=_parse_dt(row["updated_at"]) or created_at,
                )
                summary["attempts"] += 1

            for row in _row_dicts(cur, "SELECT * FROM exercises_exercisecomment"):
                user = user_by_old_id.get(row["author_id"])
                slug = old_ex_id_to_slug.get(row["exercise_id"])
                exercise = exercise_by_slug.get(slug) if slug else None
                if not user or not exercise:
                    continue
                created_at = _parse_dt(row["created_at"])
                if ExerciseComment.objects.filter(
                    author=user, exercise=exercise, body=row["body"] or "", created_at=created_at
                ).exists():
                    continue
                comment = ExerciseComment(
                    author=user,
                    exercise=exercise,
                    body=row["body"] or "",
                    is_hidden=bool(row["is_hidden"]),
                )
                comment.save()
                ExerciseComment.objects.filter(pk=comment.pk).update(
                    created_at=created_at,
                    updated_at=_parse_dt(row["updated_at"]) or created_at,
                )
                summary["comments"] += 1

            for row in _row_dicts(cur, "SELECT * FROM progress_lectureprogress"):
                user = user_by_old_id.get(row["student_id"])
                slug = old_lec_id_to_slug.get(row["lecture_id"])
                lecture = lecture_by_slug.get(slug) if slug else None
                if not user or not lecture:
                    continue
                LectureProgress.objects.update_or_create(
                    student=user,
                    lecture=lecture,
                    defaults={
                        "completed": bool(row["completed"]),
                        "completed_at": _parse_dt(row["completed_at"]),
                        "last_viewed_at": _parse_dt(row["last_viewed_at"]),
                    },
                )
                summary["lecture_progress"] += 1

            for row in _row_dicts(cur, "SELECT * FROM progress_courseprogress"):
                user = user_by_old_id.get(row["student_id"])
                slug = old_course_id_to_slug.get(row["course_id"])
                course = course_by_slug.get(slug) if slug else None
                if not user or not course:
                    continue
                last_lecture = None
                if row.get("last_lecture_id"):
                    lec_slug = old_lec_id_to_slug.get(row["last_lecture_id"])
                    last_lecture = lecture_by_slug.get(lec_slug) if lec_slug else None
                CourseProgress.objects.update_or_create(
                    student=user,
                    course=course,
                    defaults={"last_lecture": last_lecture},
                )
                summary["course_progress"] += 1

            for row in _row_dicts(cur, "SELECT * FROM progress_certificate"):
                user = user_by_old_id.get(row["student_id"])
                if not user:
                    continue
                course = None
                module = None
                if row.get("course_id"):
                    course = course_by_slug.get(old_course_id_to_slug.get(row["course_id"]))
                if row.get("module_id"):
                    module = module_by_slug.get(old_module_id_to_slug.get(row["module_id"]))
                Certificate.objects.update_or_create(
                    code=row["code"],
                    defaults={
                        "student": user,
                        "kind": row["kind"],
                        "title": row["title"],
                        "issued_at": _parse_dt(row["issued_at"]),
                        "course": course,
                        "module": module,
                    },
                )
                summary["certificates"] += 1

            for row in _row_dicts(cur, "SELECT * FROM progress_studentstreak"):
                user = user_by_old_id.get(row["student_id"])
                if not user:
                    continue
                StudentStreak.objects.update_or_create(
                    student=user,
                    defaults={
                        "current_streak": int(row["current_streak"] or 0),
                        "longest_streak": int(row["longest_streak"] or 0),
                        "last_solved_date": row["last_solved_date"],
                    },
                )
                summary["streaks"] += 1

            for row in _row_dicts(cur, "SELECT * FROM contests_contestscore"):
                user = user_by_old_id.get(row["student_id"])
                slug = old_contest_id_to_slug.get(row["contest_id"])
                contest = contest_by_slug.get(slug) if slug else None
                if not user or not contest:
                    continue
                ContestScore.objects.update_or_create(
                    contest=contest,
                    student=user,
                    defaults={
                        "points": int(row["points"] or 0),
                        "solved_count": int(row["solved_count"] or 0),
                        "last_solved_at": _parse_dt(row["last_solved_at"]),
                    },
                )
                summary["contest_scores"] += 1

        return summary
