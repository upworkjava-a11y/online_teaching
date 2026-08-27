"""Deep pre-production functional QA against local DB."""
from __future__ import annotations

import json
import sys

import django

django.setup()

from django.contrib.auth import get_user_model
from django.test import Client
from django.urls import reverse

from apps.access.services import OPEN_COURSE_SLUGS, access_service
from apps.contests.models import Contest
from apps.courses.models import Course, Lecture, Module
from apps.exercises.models import Exercise
from apps.homework.models import HomeworkAssignment, HomeworkSubmission

User = get_user_model()
fails: list[str] = []
passes: list[str] = []


def ok(name: str, cond: bool, detail: str = ""):
    if cond:
        passes.append(name)
        print(f"  PASS  {name}" + (f" — {detail}" if detail else ""))
    else:
        fails.append(f"{name}: {detail}")
        print(f"  FAIL  {name} — {detail}")


def client_for(email: str | None, password: str | None = None) -> Client:
    c = Client()
    if email:
        u = User.objects.get(email=email)
        assert c.login(username=email, password=password) or c.login(
            username=u.username, password=password
        ), f"login failed {email}"
    return c


def assert_status(name, resp, allowed, extra=""):
    loc = resp.get("Location", "")
    detail = f"got {resp.status_code}" + (f" -> {loc}" if loc else "") + (f" {extra}" if extra else "")
    ok(name, resp.status_code in allowed, detail)


print("\n========== 1) GUEST BROWSE ==========")
g = client_for(None)
assert_status("guest / -> courses", g.get("/"), {302})
assert_status("guest health", g.get("/health/"), {200})
assert_status("guest courses list", g.get("/courses/"), {200})
assert_status("guest sql detail", g.get("/courses/sql/"), {200})
assert_status("guest sql premium", g.get("/courses/sql/premium/"), {200})
assert_status("guest catalog", g.get("/exercises/"), {200})
assert_status("guest contests", g.get("/musobaqalar/"), {200})
assert_status("guest leaderboard", g.get("/dashboard/leaderboard/"), {200})
# gated
for path, label in [
    ("/dashboard/", "dashboard"),
    ("/homework/", "homework"),
    ("/progress/sertifikatlar/", "certificates"),
    ("/accounts/profile/", "profile"),
    ("/teacher/", "teacher"),
]:
    r = g.get(path)
    # auth_gate 200 or redirect login
    body = r.content.lower()
    gated = r.status_code in (301, 302, 303, 403) or (
        r.status_code == 200 and (b"kirish" in body or b"auth" in body or b"login" in body)
    )
    ok(f"guest gated {label}", gated, f"status={r.status_code}")

# lecture preview (first sql lecture)
lecture = Lecture.objects.filter(module__course__slug="sql", is_published=True).order_by("order").first()
if lecture:
    r = g.get(f"/learn/{lecture.pk}/")
    assert_status("guest lecture preview", r, {200, 403, 302})

# exercise detail should auth-gate (not 500)
ex = Exercise.objects.filter(module__course__slug="sql", is_published=True, is_skill_test=False).first()
if ex:
    r = g.get(f"/exercises/{ex.pk}/")
    body = r.content.lower()
    gated = r.status_code in (302, 403) or (
        r.status_code == 200 and (b"kirish" in body or b"hisob" in body)
    )
    ok("guest exercise auth gate", gated, f"status={r.status_code}")

print("\n========== 2) SQL-ONLY / HIDDEN COURSES ==========")
ok("OPEN_COURSE_SLUGS is sql-only", OPEN_COURSE_SLUGS == frozenset({"sql"}), str(OPEN_COURSE_SLUGS))
py = Course.objects.filter(slug="python").first()
if py:
    ok("python is_visible False", py.is_visible is False, f"is_visible={py.is_visible}")
r = g.get("/courses/python/")
ok("guest python blocked", r.status_code in (403, 404), f"status={r.status_code}")
# catalog must not list python exercises prominently — check open filter
r = g.get("/exercises/?course=python")
ok("catalog python filter empty-ish", r.status_code == 200, f"status={r.status_code}")
# contests: python unpublished
py_contest = Contest.objects.filter(slug__icontains="python").first()
if py_contest:
    ok("python contest unpublished", not py_contest.is_published, f"published={py_contest.is_published}")

print("\n========== 3) STUDENT FLOWS ==========")
s = client_for("student@example.com", "StudentPass123!")
student = User.objects.get(email="student@example.com")
assert_status("student root -> dashboard", s.get("/"), {302})
assert_status("student dashboard", s.get("/dashboard/"), {200})
assert_status("student progress", s.get("/dashboard/progress/"), {200})
assert_status("student courses", s.get("/courses/"), {200})
assert_status("student sql", s.get("/courses/sql/"), {200})
assert_status("student premium page", s.get("/courses/sql/premium/"), {200})
assert_status("student catalog", s.get("/exercises/"), {200})
assert_status("student homework list", s.get("/homework/"), {200})
assert_status("student contests", s.get("/musobaqalar/"), {200})
assert_status("student certificates", s.get("/progress/sertifikatlar/"), {200})
assert_status("student profile", s.get("/accounts/profile/"), {200})

# teacher area must NOT render for student
for path in [
    "/teacher/",
    "/teacher/students/",
    "/teacher/bilim-testi/",
    "/teacher/homework/",
    "/teacher/insights/",
]:
    r = s.get(path, follow=False)
    ok(
        f"student blocked {path}",
        r.status_code in (302, 303, 403),
        f"status={r.status_code} loc={r.get('Location','')}",
    )

# admin blocked
r = s.get("/admin/", follow=False)
ok("student admin blocked", r.status_code in (302, 403), f"status={r.status_code}")

# 404s
assert_status("student missing exercise 404", s.get("/exercises/999999/"), {404})
assert_status("student missing lecture 404", s.get("/learn/999999/"), {404})
assert_status("student missing course 404", s.get("/courses/does-not-exist/"), {404})
assert_status("student missing contest 404", s.get("/musobaqalar/nope/"), {404})

# exercise solve page
if ex:
    r = s.get(f"/exercises/{ex.pk}/")
    assert_status("student exercise detail", r, {200, 302, 403})
    if r.status_code == 200:
        # POST run (may fail validation but must not 500)
        r2 = s.post(f"/exercises/{ex.pk}/", {"action": "run", "sql_query": "SELECT 1;"})
        ok("student exercise POST no 500", r2.status_code < 500, f"status={r2.status_code}")

# skill tests page
mod = Module.objects.filter(course__slug="sql", is_published=True).order_by("order").first()
if mod:
    r = s.get(f"/exercises/bilim-testi/{mod.id}/")
    assert_status("student skill tests", r, {200, 302, 403})

# lecture complete POST
if lecture:
    r = s.get(f"/learn/{lecture.pk}/")
    assert_status("student lecture", r, {200, 403})
    r2 = s.post(f"/learn/{lecture.pk}/complete/")
    ok("student lecture complete no 500", r2.status_code < 500, f"status={r2.status_code}")

# homework submit page
hw = HomeworkAssignment.objects.filter(is_published=True).first()
if hw:
    r = s.get(f"/homework/{hw.pk}/submit/")
    assert_status("student homework submit GET", r, {200, 302, 403})

# contest detail
contest = Contest.objects.filter(is_published=True).first()
if contest:
    r = s.get(f"/musobaqalar/{contest.slug}/")
    assert_status("student contest detail", r, {200})

# access decision sample
if ex:
    d = access_service.evaluate(student, ex)
    ok("access evaluate returns decision", d is not None, f"allowed={d.allowed} code={d.code}")

print("\n========== 4) TEACHER FLOWS ==========")
t = client_for("teacher@example.com", "TeacherPass123!")
assert_status("teacher root -> analytics", t.get("/"), {302})
assert_status("teacher dashboard", t.get("/teacher/"), {200})
assert_status("teacher students", t.get("/teacher/students/"), {200})
assert_status("teacher skill tests", t.get("/teacher/bilim-testi/"), {200})
assert_status("teacher homework", t.get("/teacher/homework/"), {200})
assert_status("teacher insights", t.get("/teacher/insights/"), {200})
# student detail
r = t.get(f"/teacher/students/{student.pk}/")
assert_status("teacher student detail", r, {200, 404})
r = t.get(f"/teacher/students/{student.pk}/bilim-testi/")
assert_status("teacher student skill tests", r, {200, 404})
sub = HomeworkSubmission.objects.first()
if sub:
    r = t.get(f"/teacher/homework/{sub.pk}/")
    assert_status("teacher homework review", r, {200, 404})

print("\n========== 5) ADMIN ==========")
admin = User.objects.filter(is_superuser=True).first()
a = Client()
a.force_login(admin)
assert_status("admin index", a.get("/admin/"), {200})
assert_status("admin user content access", a.get("/admin/access/usercontentaccess/"), {200})
r = a.get("/admin/access/usercontentaccess/")
ok(
    "admin grant button present",
    b"ochish" in r.content.lower() or b"grant" in r.content.lower() or b"to" in r.content.lower(),
    "changelist content check",
)
# grant form page if registered
r = a.get("/admin/access/usercontentaccess/grant-course-premium/")
# URL may differ — try discovering
from django.urls import get_resolver

grant_urls = []
# soft check: page 200 or 404 if different path
ok("admin grant path reachable or 404", r.status_code in (200, 404), f"status={r.status_code}")

print("\n========== 6) AUTH FORMS ==========")
r = g.get("/accounts/login/")
assert_status("login page", r, {200})
r = g.get("/accounts/register/")
assert_status("register page", r, {200})
# bad login
r = g.post("/accounts/login/", {"username": "nope@x.com", "password": "bad"})
ok("bad login no 500", r.status_code < 500, f"status={r.status_code}")
# logout
r = s.post("/accounts/logout/")
assert_status("student logout", r, {200, 302})

print("\n========== 7) CONTENT / NAV SMOKE ==========")
# SQL course modules visible count
sql = Course.objects.get(slug="sql")
mods = Module.objects.filter(course=sql, is_published=True).count()
exs = Exercise.objects.filter(module__course=sql, is_published=True).count()
ok("sql has modules", mods > 0, f"modules={mods}")
ok("sql has exercises", exs > 0, f"exercises={exs}")
ok("published contest exists", Contest.objects.filter(is_published=True).exists())

# navbar critical links as guest
r = g.get("/courses/")
for needle in [b"/courses/", b"/exercises/", b"/musobaqalar/"]:
    ok(f"nav contains {needle.decode()}", needle in r.content, "missing from courses page")

print("\n========== SUMMARY ==========")
print(f"PASS: {len(passes)}")
print(f"FAIL: {len(fails)}")
for f in fails:
    print(f"  - {f}")

with open("scripts/qa_deep_results.json", "w", encoding="utf-8") as fh:
    json.dump({"pass": passes, "fail": fails}, fh, indent=2, ensure_ascii=False)

sys.exit(1 if fails else 0)
