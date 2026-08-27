import django

django.setup()

from django.test import Client
from django.contrib.auth import get_user_model
from apps.courses.models import Course, Lecture, Module
from apps.exercises.models import Exercise

User = get_user_model()
g = Client()
sql = Course.objects.get(slug="sql")
mod6 = Module.objects.filter(course=sql, is_published=True).order_by("order")[5]
mod1 = Module.objects.filter(course=sql, is_published=True).order_by("order").first()
lec6 = Lecture.objects.filter(module=mod6, is_published=True).first()
lec1 = Lecture.objects.filter(module=mod1, is_published=True).first()
ex6 = Exercise.objects.filter(module=mod6, is_published=True, is_skill_test=False).first()

print("guest free lec", g.get(f"/learn/{lec1.pk}/").status_code)
r = g.get(f"/learn/{lec6.pk}/")
print("guest locked lec", r.status_code, r.get("Location"))
r = g.get(f"/exercises/{ex6.pk}/")
print("guest locked ex (auth gate expected)", r.status_code, b"kirish" in r.content.lower() or b"hisob" in r.content.lower())

t = Client()
teacher = User.objects.get(email="teacher@example.com")
t.login(username=teacher.email, password="TeacherPass123!") or t.login(
    username=teacher.username, password="TeacherPass123!"
)
ex1 = Exercise.objects.filter(module=mod1, is_published=True, is_skill_test=False).first()
r = t.get(f"/exercises/{ex1.pk}/")
print("teacher exercise detail", r.status_code, r.get("Location"))
r = t.get(f"/learn/{lec1.pk}/")
print("teacher lecture", r.status_code, r.get("Location"))
r = t.get("/homework/")
print("teacher homework list", r.status_code, r.get("Location"))
r = t.get("/dashboard/")
print("teacher student dashboard", r.status_code, r.get("Location"))
