from django.db.models import Max
from django.utils import timezone

from apps.courses.models import Course, Lecture, Module
from apps.exercises.models import Exercise, ExerciseAttempt

from .models import CourseProgress, LectureProgress


class ProgressService:
    def touch_lecture(self, student, lecture: Lecture) -> LectureProgress:
        progress, _ = LectureProgress.objects.get_or_create(student=student, lecture=lecture)
        progress.last_viewed_at = timezone.now()
        progress.save(update_fields=["last_viewed_at", "updated_at"])
        course_progress, _ = CourseProgress.objects.get_or_create(student=student, course=lecture.course)
        course_progress.last_lecture = lecture
        course_progress.last_activity_at = timezone.now()
        course_progress.save(update_fields=["last_lecture", "last_activity_at", "updated_at"])
        return progress

    def complete_lecture(self, student, lecture: Lecture) -> LectureProgress:
        progress, _ = LectureProgress.objects.get_or_create(student=student, lecture=lecture)
        if not progress.completed:
            progress.completed = True
            progress.completed_at = timezone.now()
        progress.last_viewed_at = timezone.now()
        progress.save(update_fields=["completed", "completed_at", "last_viewed_at", "updated_at"])
        course_progress, _ = CourseProgress.objects.get_or_create(student=student, course=lecture.course)
        course_progress.last_lecture = lecture
        course_progress.last_activity_at = timezone.now()
        course_progress.save(update_fields=["last_lecture", "last_activity_at", "updated_at"])
        return progress

    def last_position(self, student, course: Course | None = None):
        qs = CourseProgress.objects.filter(student=student, last_lecture__isnull=False)
        if course:
            qs = qs.filter(course=course)
        row = qs.order_by("-last_activity_at").select_related("last_lecture", "course").first()
        return row.last_lecture if row else None

    def course_stats(self, student, course: Course) -> dict:
        lectures = Lecture.objects.filter(module__course=course, is_published=True)
        lecture_ids = list(lectures.values_list("id", flat=True))
        completed_lectures = LectureProgress.objects.filter(
            student=student, lecture_id__in=lecture_ids, completed=True
        ).count()
        total_lectures = len(lecture_ids)

        exercises = Exercise.objects.filter(module__course=course, is_published=True)
        exercise_ids = list(exercises.values_list("id", flat=True))
        completed_exercises = (
            ExerciseAttempt.objects.filter(student=student, exercise_id__in=exercise_ids, is_correct=True)
            .values("exercise_id")
            .distinct()
            .count()
        )
        total_exercises = len(exercise_ids)
        best_scores = list(
            ExerciseAttempt.objects.filter(student=student, exercise_id__in=exercise_ids)
            .values("exercise_id")
            .annotate(best=Max("score"))
        )
        average_score = 0.0
        if best_scores:
            average_score = round(sum(item["best"] or 0 for item in best_scores) / len(best_scores), 1)

        total_items = total_lectures + total_exercises
        completed_items = completed_lectures + completed_exercises
        percent = round((completed_items / total_items) * 100) if total_items else 0
        return {
            "completed_lectures": completed_lectures,
            "total_lectures": total_lectures,
            "completed_exercises": completed_exercises,
            "total_exercises": total_exercises,
            "average_score": average_score,
            "percent": percent,
        }

    def module_percent(self, student, module: Module) -> int:
        lectures = module.lectures.filter(is_published=True)
        exercises = module.exercises.filter(is_published=True)
        total = lectures.count() + exercises.count()
        if not total:
            return 0
        completed_lectures = LectureProgress.objects.filter(
            student=student, lecture__in=lectures, completed=True
        ).count()
        completed_exercises = (
            ExerciseAttempt.objects.filter(student=student, exercise__in=exercises, is_correct=True)
            .values("exercise_id")
            .distinct()
            .count()
        )
        return round(((completed_lectures + completed_exercises) / total) * 100)


progress_service = ProgressService()
