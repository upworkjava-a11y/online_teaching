import logging
import re
import time

from django.conf import settings
from django.core.cache import cache

from apps.sandbox.comparison import compare_results
from apps.sandbox.exceptions import SandboxError
from apps.sandbox.executor import sql_executor

from .models import Exercise, ExerciseAttempt

logger = logging.getLogger("apps.exercises")


class RateLimited(Exception):
    def __init__(self, message="Juda ko‘p so‘rov yuborildi. Biroz kuting."):
        super().__init__(message)
        self.message = message


def _normalize_quiz_answer(value: str) -> str:
    text = (value or "").strip().upper()
    text = text.replace("’", "'").replace("‘", "'")
    # Accept "A", "A)", "A.", "VARIANT A"
    match = re.match(r"^(?:VARIANT\s*)?([A-D])\b", text)
    if match:
        return match.group(1)
    return re.sub(r"\s+", " ", text)


class ExerciseService:
    def run(self, student, exercise: Exercise, submission: str) -> ExerciseAttempt:
        if exercise.kind == Exercise.Kind.QUIZ:
            return self._run_quiz(student, exercise, submission)
        return self._run_sql(student, exercise, submission)

    def _run_quiz(self, student, exercise: Exercise, answer: str) -> ExerciseAttempt:
        started = time.monotonic()
        expected = exercise.expected_result
        expected_raw = ""
        if expected and expected.rows:
            expected_raw = str(expected.rows[0][0]) if expected.rows[0] else ""
        ok = _normalize_quiz_answer(answer) == _normalize_quiz_answer(expected_raw)
        attempt = ExerciseAttempt(
            student=student,
            exercise=exercise,
            sql_query=answer,
            is_correct=ok,
            score=exercise.max_score if ok else 0,
            error_message="" if ok else "Noto‘g‘ri javob. Qayta urinib ko‘ring.",
            result_preview={
                "columns": ["javob"],
                "rows": [[answer]],
                "message": "To‘g‘ri!" if ok else "Noto‘g‘ri.",
            },
            execution_ms=int((time.monotonic() - started) * 1000),
        )
        attempt.save()
        logger.info(
            "exercise_attempt",
            extra={"exercise_id": exercise.pk, "student_id": student.pk, "is_correct": ok, "kind": "quiz"},
        )
        if ok:
            self._on_correct(student, exercise)
        return attempt

    def _run_sql(self, student, exercise: Exercise, sql: str) -> ExerciseAttempt:
        cache_key = f"sql-rate:{student.pk}"
        current = cache.get(cache_key, 0)
        if current >= settings.SQL_RATE_LIMIT_PER_MINUTE:
            raise RateLimited()
        cache.set(cache_key, current + 1, 60)

        started = time.monotonic()
        attempt = ExerciseAttempt(student=student, exercise=exercise, sql_query=sql)
        try:
            result = sql_executor.execute(sql)
            expected = exercise.expected_result
            is_correct, message = compare_results(
                actual_columns=result.columns,
                actual_rows=result.rows,
                expected_columns=expected.columns,
                expected_rows=expected.rows,
                require_row_order=exercise.require_row_order,
                require_column_order=exercise.require_column_order,
            )
            attempt.is_correct = is_correct
            attempt.score = exercise.max_score if is_correct else 0
            attempt.result_preview = {
                "columns": result.columns,
                "rows": result.rows[:50],
                "truncated": result.truncated,
                "message": message,
            }
            if not is_correct:
                attempt.error_message = "Noto‘g‘ri. Qayta urinib ko‘ring."
        except SandboxError as exc:
            attempt.is_correct = False
            attempt.score = 0
            attempt.error_message = exc.message
            attempt.result_preview = {"columns": [], "rows": [], "message": exc.message}
            logger.warning("exercise_sql_error", extra={"exercise_id": exercise.pk, "code": exc.code})
        attempt.execution_ms = int((time.monotonic() - started) * 1000)
        attempt.save()
        logger.info(
            "exercise_attempt",
            extra={
                "exercise_id": exercise.pk,
                "student_id": student.pk,
                "is_correct": attempt.is_correct,
                "execution_ms": attempt.execution_ms,
            },
        )
        if attempt.is_correct:
            self._on_correct(student, exercise)
        return attempt

    def _on_correct(self, student, exercise: Exercise) -> None:
        from apps.contests.services import sync_student_contests_on_solve
        from apps.progress.certificates import issue_course_certificate, issue_module_certificate
        from apps.progress.streak import record_correct_solve

        record_correct_solve(student)
        sync_student_contests_on_solve(student, exercise)
        issue_module_certificate(student, exercise.module)
        issue_course_certificate(student, exercise.module.course)


exercise_service = ExerciseService()
