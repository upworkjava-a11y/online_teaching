import secrets
import string

from apps.courses.models import Course, Module
from apps.exercises.models import Exercise, ExerciseAttempt
from apps.progress.models import Certificate, LectureProgress


def _code() -> str:
    alphabet = string.ascii_uppercase + string.digits
    return "CW-" + "".join(secrets.choice(alphabet) for _ in range(10))


def module_completion(student, module: Module) -> dict:
    lectures = list(module.lectures.filter(is_published=True))
    exercises = list(module.exercises.filter(is_published=True, is_skill_test=False))
    skill_tests = list(module.exercises.filter(is_published=True, is_skill_test=True))
    lecture_ids = [x.pk for x in lectures]
    exercise_ids = [x.pk for x in exercises]
    skill_ids = [x.pk for x in skill_tests]

    done_lectures = LectureProgress.objects.filter(
        student=student, lecture_id__in=lecture_ids, completed=True
    ).count()
    done_exercises = (
        ExerciseAttempt.objects.filter(student=student, exercise_id__in=exercise_ids, is_correct=True)
        .values("exercise_id")
        .distinct()
        .count()
        if exercise_ids
        else 0
    )
    done_skills = (
        ExerciseAttempt.objects.filter(student=student, exercise_id__in=skill_ids, is_correct=True)
        .values("exercise_id")
        .distinct()
        .count()
        if skill_ids
        else 0
    )

    lectures_ok = done_lectures >= len(lectures) if lectures else True
    exercises_ok = done_exercises >= len(exercises) if exercises else True
    skills_ok = done_skills >= len(skill_tests) if skill_tests else True
    ready = lectures_ok and exercises_ok and skills_ok
    return {
        "ready": ready,
        "done_lectures": done_lectures,
        "total_lectures": len(lectures),
        "done_exercises": done_exercises,
        "total_exercises": len(exercises),
        "done_skills": done_skills,
        "total_skills": len(skill_tests),
    }


def issue_module_certificate(student, module: Module) -> Certificate | None:
    status = module_completion(student, module)
    if not status["ready"]:
        return None
    existing = Certificate.objects.filter(student=student, kind=Certificate.Kind.MODULE, module=module).first()
    if existing:
        return existing
    title = f"{module.course.title} — {module.title} moduli"
    return Certificate.objects.create(
        student=student,
        kind=Certificate.Kind.MODULE,
        module=module,
        course=module.course,
        title=title,
        code=_code(),
    )


def issue_course_certificate(student, course: Course) -> Certificate | None:
    modules = list(course.modules.filter(is_published=True))
    if not modules:
        return None
    for module in modules:
        if not module_completion(student, module)["ready"]:
            return None
        issue_module_certificate(student, module)
    existing = Certificate.objects.filter(student=student, kind=Certificate.Kind.COURSE, course=course).first()
    if existing:
        return existing
    return Certificate.objects.create(
        student=student,
        kind=Certificate.Kind.COURSE,
        course=course,
        title=f"{course.title} — kurs sertifikati",
        code=_code(),
    )
