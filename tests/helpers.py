from django.core.files.uploadedfile import SimpleUploadedFile

from apps.accounts.models import TeacherProfile, User
from apps.courses.models import Course, CourseEnrollment, Lecture, Module
from apps.exercises.models import Exercise, ExerciseExpectedResult
from apps.homework.models import HomeworkAssignment


def make_user(email, role=User.Role.STUDENT, password="StrongPass123!", **kwargs):
    defaults = {
        "username": email.split("@")[0],
        "first_name": kwargs.pop("first_name", "Test"),
        "last_name": kwargs.pop("last_name", "User"),
        "role": role,
    }
    defaults.update(kwargs)
    user = User.objects.create_user(email=email, password=password, **defaults)
    return user


def make_course(slug="sql", published=True, visible=True, title="SQL"):
    return Course.objects.create(
        title=title,
        slug=slug,
        description="Test course",
        order=1,
        is_published=published,
        is_visible=visible,
    )


def make_module(course, slug="basics", published=True, title="SQL asoslari", order=1):
    return Module.objects.create(
        course=course,
        title=title,
        slug=slug,
        description="Test module",
        order=order,
        is_published=published,
    )


def make_lecture(module, slug="select", published=True, title="SELECT nima?", order=1):
    return Lecture.objects.create(
        module=module,
        title=title,
        slug=slug,
        content="<p>Test ma’ruza</p>",
        sql_examples=["SELECT 1;"],
        order=order,
        is_published=published,
    )


def make_exercise(module, slug="ex1", published=True, lecture=None, difficulty=None, title="Test mashq", order=1):
    exercise = Exercise.objects.create(
        module=module,
        lecture=lecture,
        title=title,
        slug=slug,
        description="Tavsif",
        task="SELECT name FROM customers",
        hints=["hint"],
        order=order,
        is_published=published,
        difficulty=difficulty or Exercise.Difficulty.EASY,
        require_row_order=False,
        require_column_order=False,
    )
    ExerciseExpectedResult.objects.create(
        exercise=exercise,
        columns=["name"],
        rows=[["Ali Valiyev"], ["Malika Karimova"], ["Javohir Saidov"], ["Dilnoza Yusupova"], ["Sardor Ergashev"]],
    )
    return exercise


def make_homework(lecture):
    return HomeworkAssignment.objects.create(
        lecture=lecture,
        title="Uy vazifasi",
        instructions="Matn yozing",
        max_score=100,
        is_published=True,
    )


def txt_file(content="SELECT 1;", name="homework.txt"):
    return SimpleUploadedFile(name, content.encode("utf-8"), content_type="text/plain")


def enroll(student, course):
    return CourseEnrollment.objects.get_or_create(student=student, course=course)[0]


def assign_teacher(teacher, course):
    profile, _ = TeacherProfile.objects.get_or_create(user=teacher)
    profile.assigned_courses.add(course)
    return profile
