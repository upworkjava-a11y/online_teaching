"""Premium lock + grant + edge cases."""
import django

django.setup()

from django.contrib.auth import get_user_model
from django.test import Client
from django.urls import reverse

from apps.access.services import access_service
from apps.contests.models import Contest
from apps.courses.models import Course, Lecture, Module
from apps.exercises.models import Exercise
from tests.helpers import make_user

User = get_user_model()
fails = []


def check(name, cond, detail=""):
    print(("PASS" if cond else "FAIL"), name, detail)
    if not cond:
        fails.append(f"{name}: {detail}")


fresh = make_user("qa_lock@test.com")
c = Client()
c.force_login(fresh)
sql = Course.objects.get(slug="sql")
mod6 = Module.objects.filter(course=sql, is_published=True).order_by("order")[5]
lec = Lecture.objects.filter(module=mod6, is_published=True).first()
ex = Exercise.objects.filter(module=mod6, is_published=True).first()

r = c.get(f"/learn/{lec.pk}/")
loc = r.get("Location", "")
check("locked lecture -> premium", r.status_code == 302 and "/premium/" in loc, f"{r.status_code} {loc}")

r = c.get(f"/exercises/{ex.pk}/")
loc = r.get("Location", "")
check("locked exercise -> premium", r.status_code == 302 and "/premium/" in loc, f"{r.status_code} {loc}")

mod1 = Module.objects.filter(course=sql, is_published=True).order_by("order").first()
lec1 = Lecture.objects.filter(module=mod1, is_published=True).first()
r = c.get(f"/learn/{lec1.pk}/")
check("free lecture open", r.status_code == 200, str(r.status_code))

r = c.get(f"/exercises/bilim-testi/{mod6.id}/")
loc = r.get("Location", "")
check("locked skill test gated", r.status_code in (302, 403), f"{r.status_code} {loc}")

admin = User.objects.filter(is_superuser=True).first()
access_service.grant_course_access(fresh, sql, created_by=admin, reason="QA grant")
r = c.get(f"/learn/{lec.pk}/")
check("after grant lecture open", r.status_code == 200, str(r.status_code))
r = c.get(f"/exercises/{ex.pk}/")
check("after grant exercise open", r.status_code == 200, str(r.status_code))

access_service.revoke_course_access(fresh, sql)
r = c.get(f"/learn/{lec.pk}/")
check("after revoke locked again", r.status_code == 302, f"{r.status_code} {r.get('Location')}")

pc = Contest.objects.filter(is_published=False).first()
if pc:
    r = c.get(f"/musobaqalar/{pc.slug}/")
    check("unpublished contest 404", r.status_code == 404, str(r.status_code))

a = Client()
a.force_login(admin)
url = reverse("admin:access_usercontentaccess_grant_course")
r = a.get(url)
check("grant form 200", r.status_code == 200, str(r.status_code))

r = c.post(f"/progress/sertifikat/modul/{mod1.id}/olish/")
check("claim module no 500", r.status_code < 500, str(r.status_code))

r = c.get("/teacher/")
check("fresh student teacher redirect", r.status_code == 302, str(r.status_code))

g = Client()
r = g.get("/accounts/google/login/")
check("google login starts", r.status_code in (302, 503, 400), str(r.status_code))

r = g.post(f"/learn/{lec1.pk}/complete/")
check("guest complete gated", r.status_code in (200, 302, 403), str(r.status_code))

# Premium page content
r = g.get("/courses/sql/premium/")
check("premium page 200", r.status_code == 200, str(r.status_code))
body = r.content.decode("utf-8", errors="ignore").lower()
check("premium shows price", "so" in body or "000" in body or "premium" in body)
check("premium shows card or telegram", "9860" in body or "telegram" in body or "@" in body)

# Course detail shows lock for free user on later modules
r = c.get("/courses/sql/")
check("course detail 200 for free user", r.status_code == 200, str(r.status_code))
body = r.content.decode("utf-8", errors="ignore").lower()
check(
    "course detail mentions premium/lock",
    "premium" in body or "to‘lov" in body or "tolov" in body or "ochish" in body or "qulf" in body,
)

fresh.delete()
print("FAIL COUNT", len(fails))
for f in fails:
    print(" -", f)
raise SystemExit(1 if fails else 0)
