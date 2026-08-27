"""
Pre-production QA: hit all named routes as guest / student / teacher / admin.
Run: py manage.py shell < scripts/qa_url_matrix.py
  or: py -c "import django; ..."
"""
from __future__ import annotations

import json
import sys
from dataclasses import dataclass, field

import django
from django.contrib.auth import get_user_model
from django.test import Client
from django.urls import NoReverseMatch, get_resolver, reverse

django.setup()

from apps.contests.models import Contest
from apps.courses.models import Course, Lecture, Module
from apps.exercises.models import Exercise
from apps.homework.models import HomeworkAssignment, HomeworkSubmission
from apps.progress.models import Certificate

User = get_user_model()

PASSWORDS = {
    "student@example.com": "StudentPass123!",
    "teacher@example.com": "TeacherPass123!",
}


@dataclass
class Result:
    role: str
    method: str
    path: str
    name: str
    status: int | str
    ok: bool
    note: str = ""


@dataclass
class Report:
    results: list[Result] = field(default_factory=list)

    def add(self, **kwargs):
        self.results.append(Result(**kwargs))

    def print_summary(self):
        fails = [r for r in self.results if not r.ok]
        print("\n=== QA URL MATRIX SUMMARY ===")
        print(f"Total checks: {len(self.results)}")
        print(f"Pass: {len(self.results) - len(fails)}")
        print(f"Fail: {len(fails)}")
        if fails:
            print("\n--- FAILURES ---")
            for r in fails:
                print(f"[{r.role}] {r.method} {r.path} ({r.name}) -> {r.status} {r.note}")
        by_role = {}
        for r in self.results:
            by_role.setdefault(r.role, {"ok": 0, "fail": 0})
            by_role[r.role]["ok" if r.ok else "fail"] += 1
        print("\n--- BY ROLE ---")
        for role, counts in by_role.items():
            print(f"  {role}: {counts['ok']} ok, {counts['fail']} fail")


def expect_ok(status: int) -> bool:
    return status in (200, 302, 301, 303)


def expect_auth_gate(status: int, path: str, content: bytes) -> tuple[bool, str]:
    """Login-required pages: redirect to login OR auth_gate 200."""
    if status in (301, 302, 303):
        return True, "redirect"
    if status == 200 and (b"auth_gate" in content or b"Kirish" in content or b"login" in content.lower()):
        return True, "auth_gate/login page"
    if status == 403:
        return True, "forbidden"
    return False, f"expected auth redirect/gate, got {status}"


def expect_teacher_only(status: int) -> tuple[bool, str]:
    if status in (301, 302, 303, 403):
        return True, "blocked"
    if status == 200:
        return False, "teacher page leaked to non-teacher"
    return False, f"unexpected {status}"


def fixtures():
    course = Course.objects.filter(slug="sql", is_published=True).first()
    module = Module.objects.filter(course=course, is_published=True).order_by("order").first() if course else None
    lecture = Lecture.objects.filter(module=module, is_published=True).order_by("order").first() if module else None
    exercise = (
        Exercise.objects.filter(module__course=course, is_published=True).order_by("order").first()
        if course
        else None
    )
    homework = HomeworkAssignment.objects.filter(is_published=True).first()
    contest = Contest.objects.filter(is_published=True).first()
    cert = Certificate.objects.first()
    submission = HomeworkSubmission.objects.first()
    student = User.objects.filter(email="student@example.com").first()
    teacher = User.objects.filter(email="teacher@example.com").first()
    admin = User.objects.filter(is_superuser=True).first()
    return {
        "course": course,
        "module": module,
        "lecture": lecture,
        "exercise": exercise,
        "homework": homework,
        "contest": contest,
        "cert": cert,
        "submission": submission,
        "student": student,
        "teacher": teacher,
        "admin": admin,
    }


def build_cases(fx):
    cases = [
        ("root", "GET", "/", None, {}),
        ("health", "GET", "/health/", "health", {}),
        ("accounts:register", "GET", None, "accounts:register", {}),
        ("accounts:login", "GET", None, "accounts:login", {}),
        ("accounts:logout", "POST", None, "accounts:logout", {}),
        ("accounts:profile", "GET", None, "accounts:profile", {}),
        ("accounts:google_login", "GET", None, "accounts:google_login", {}),
        ("dashboard:home", "GET", None, "dashboard:home", {}),
        ("dashboard:progress", "GET", None, "dashboard:progress", {}),
        ("dashboard:leaderboard", "GET", None, "dashboard:leaderboard", {}),
        ("courses:list", "GET", None, "courses:list", {}),
        ("exercises:catalog", "GET", None, "exercises:catalog", {}),
        ("homework:list", "GET", None, "homework:list", {}),
        ("contests:list", "GET", None, "contests:list", {}),
        ("progress:certificates", "GET", None, "progress:certificates", {}),
        ("analytics:dashboard", "GET", None, "analytics:dashboard", {}),
        ("analytics:students", "GET", None, "analytics:students", {}),
        ("analytics:skill_tests", "GET", None, "analytics:skill_tests", {}),
        ("analytics:homework", "GET", None, "analytics:homework", {}),
        ("analytics:insights", "GET", None, "analytics:insights", {}),
        ("admin:index", "GET", "/admin/", None, {}),
        ("admin:login", "GET", "/admin/login/", None, {}),
    ]
    if fx["course"]:
        cases += [
            ("courses:detail", "GET", None, "courses:detail", {"slug": fx["course"].slug}),
            ("courses:premium", "GET", None, "courses:premium", {"slug": fx["course"].slug}),
        ]
    if fx["module"]:
        cases.append(
            ("exercises:skill_tests", "GET", None, "exercises:skill_tests", {"module_id": fx["module"].id})
        )
        cases.append(
            ("progress:claim_module", "POST", None, "progress:claim_module", {"module_id": fx["module"].id})
        )
    if fx["lecture"]:
        cases += [
            ("learning:lecture", "GET", None, "learning:lecture", {"pk": fx["lecture"].pk}),
            ("learning:complete", "POST", None, "learning:complete", {"pk": fx["lecture"].pk}),
        ]
    if fx["exercise"]:
        cases.append(("exercises:detail", "GET", None, "exercises:detail", {"pk": fx["exercise"].pk}))
    if fx["homework"]:
        cases.append(("homework:submit", "GET", None, "homework:submit", {"pk": fx["homework"].pk}))
    if fx["contest"]:
        cases.append(("contests:detail", "GET", None, "contests:detail", {"slug": fx["contest"].slug}))
    if fx["cert"]:
        cases.append(
            ("progress:certificate_detail", "GET", None, "progress:certificate_detail", {"code": fx["cert"].code})
        )
    if fx["course"]:
        cases.append(
            ("progress:claim_course", "POST", None, "progress:claim_course", {"course_id": fx["course"].id})
        )
    if fx["student"]:
        cases.append(
            (
                "analytics:student_detail",
                "GET",
                None,
                "analytics:student_detail",
                {"pk": fx["student"].pk},
            )
        )
        cases.append(
            (
                "analytics:student_skill_tests",
                "GET",
                None,
                "analytics:student_skill_tests",
                {"pk": fx["student"].pk},
            )
        )
    if fx["submission"]:
        cases += [
            ("homework:download", "GET", None, "homework:download", {"pk": fx["submission"].pk}),
            ("homework:delete", "POST", None, "homework:delete", {"pk": fx["submission"].pk}),
            (
                "analytics:homework_review",
                "GET",
                None,
                "analytics:homework_review",
                {"pk": fx["submission"].pk},
            ),
        ]
    # Negative / edge
    cases += [
        ("courses:detail-missing", "GET", "/courses/does-not-exist/", None, {}),
        ("exercises:detail-missing", "GET", "/exercises/999999/", None, {}),
        ("learning:missing", "GET", "/learn/999999/", None, {}),
        ("contests:missing", "GET", "/musobaqalar/does-not-exist/", None, {}),
        ("courses:python-if-hidden", "GET", "/courses/python/", None, {}),
    ]
    return cases


# Paths that guests may browse (200)
GUEST_OK = {
    "root",
    "health",
    "accounts:register",
    "accounts:login",
    "accounts:google_login",
    "courses:list",
    "courses:detail",
    "courses:premium",
    "exercises:catalog",
    "exercises:detail",
    "exercises:skill_tests",
    "learning:lecture",
    "contests:list",
    "contests:detail",
    "dashboard:leaderboard",
    "admin:login",
}

# Guest should be gated (redirect/login/auth_gate/403)
GUEST_GATED = {
    "accounts:profile",
    "accounts:logout",
    "dashboard:home",
    "dashboard:progress",
    "homework:list",
    "homework:submit",
    "homework:download",
    "homework:delete",
    "learning:complete",
    "progress:certificates",
    "progress:claim_module",
    "progress:claim_course",
    "analytics:dashboard",
    "analytics:students",
    "analytics:student_detail",
    "analytics:student_skill_tests",
    "analytics:skill_tests",
    "analytics:homework",
    "analytics:homework_review",
    "analytics:insights",
    "admin:index",
}

TEACHER_ONLY = {
    "analytics:dashboard",
    "analytics:students",
    "analytics:student_detail",
    "analytics:student_skill_tests",
    "analytics:skill_tests",
    "analytics:homework",
    "analytics:homework_review",
    "analytics:insights",
}

# Destructive POSTs we only check for auth, not execute as mutating success
SKIP_MUTATE_AS = {"homework:delete"}  # still hit for auth check but don't require 200 for owner


def resolve_path(path, name, kwargs):
    if path:
        return path
    try:
        return reverse(name, kwargs=kwargs)
    except NoReverseMatch as exc:
        return None, str(exc)


def check_role(report: Report, role: str, client: Client, cases, fx):
    for label, method, path, name, kwargs in cases:
        resolved = path
        if not resolved and name:
            try:
                resolved = reverse(name, kwargs=kwargs)
            except NoReverseMatch as exc:
                report.add(
                    role=role,
                    method=method,
                    path=str(kwargs),
                    name=label,
                    status="NO_REVERSE",
                    ok=False,
                    note=str(exc),
                )
                continue

        # Avoid actually deleting homework during QA
        if label == "homework:delete" and role in ("student", "teacher", "admin"):
            # Only verify login wall for guest; for authed users skip mutate
            if role != "guest":
                report.add(
                    role=role,
                    method=method,
                    path=resolved,
                    name=label,
                    status="SKIP",
                    ok=True,
                    note="skip destructive POST",
                )
                continue

        try:
            if method == "GET":
                resp = client.get(resolved, follow=False)
            else:
                resp = client.post(resolved, follow=False)
        except Exception as exc:  # noqa: BLE001
            report.add(
                role=role,
                method=method,
                path=resolved,
                name=label,
                status="EXC",
                ok=False,
                note=repr(exc),
            )
            continue

        status = resp.status_code
        content = getattr(resp, "content", b"") or b""
        ok = True
        note = ""

        if label.endswith("-missing") or label.endswith("-if-hidden"):
            # 404 expected for missing; python may 404 or 200 if visible
            if label == "courses:python-if-hidden":
                # SQL-only release: python should not be openly usable
                if status == 404:
                    ok, note = True, "hidden/missing ok"
                elif status == 200:
                    ok, note = False, "python course still publicly reachable"
                elif status in (301, 302):
                    ok, note = True, f"redirect {resp.get('Location', '')}"
                else:
                    ok, note = False, f"unexpected {status}"
            else:
                ok = status == 404
                note = "expected 404" if ok else f"expected 404 got {status}"
        elif role == "guest":
            if label in GUEST_OK:
                ok = status == 200
                note = "" if ok else f"guest browse expected 200 got {status}"
            elif label in GUEST_GATED or label.startswith("analytics:") or label.startswith("homework:"):
                ok, note = expect_auth_gate(status, resolved, content)
            elif label.startswith("admin:"):
                ok = status in (200, 302)
            else:
                ok = expect_ok(status)
        elif role == "student":
            if label in TEACHER_ONLY or label.startswith("analytics:"):
                ok, note = expect_teacher_only(status)
            elif label == "admin:index":
                ok = status in (302, 403)
                note = "student must not reach admin" if ok else f"admin leak {status}"
            elif label in ("learning:complete", "progress:claim_module", "progress:claim_course"):
                # may 200/302/403 depending on access/premium
                ok = status in (200, 302, 303, 403)
                note = f"complete/claim status {status}"
            else:
                ok = expect_ok(status) or status == 403
                if not ok:
                    note = f"unexpected {status}"
        elif role == "teacher":
            if label == "admin:index":
                ok = status in (200, 302, 403)
            else:
                ok = expect_ok(status) or status == 403
                if not ok:
                    note = f"unexpected {status}"
        elif role == "admin":
            ok = expect_ok(status) or status == 403
            if not ok:
                note = f"unexpected {status}"

        # Server errors always fail
        if isinstance(status, int) and status >= 500:
            ok = False
            note = f"server error {status}"

        report.add(
            role=role,
            method=method,
            path=resolved,
            name=label,
            status=status,
            ok=ok,
            note=note,
        )


def login_client(email: str) -> Client | None:
    client = Client()
    password = PASSWORDS.get(email)
    user = User.objects.filter(email=email).first()
    if not user:
        return None
    if password and client.login(username=email, password=password):
        return client
    # try username
    if password and client.login(username=user.username, password=password):
        return client
    return None


def main():
    fx = fixtures()
    print("=== FIXTURES ===")
    for k, v in fx.items():
        if v is None:
            print(f"  {k}: MISSING")
        else:
            print(f"  {k}: {v}")

    cases = build_cases(fx)
    report = Report()

    # Guest
    check_role(report, "guest", Client(), cases, fx)

    # Student
    student_client = login_client("student@example.com")
    if student_client:
        check_role(report, "student", student_client, cases, fx)
    else:
        report.add(
            role="student",
            method="LOGIN",
            path="/",
            name="login",
            status="FAIL",
            ok=False,
            note="could not login student@example.com",
        )

    # Teacher
    teacher_client = login_client("teacher@example.com")
    if teacher_client:
        check_role(report, "teacher", teacher_client, cases, fx)
    else:
        report.add(
            role="teacher",
            method="LOGIN",
            path="/",
            name="login",
            status="FAIL",
            ok=False,
            note="could not login teacher@example.com",
        )

    # Admin (if any with known password — skip login if unknown)
    admin = fx["admin"]
    if admin:
        admin_client = Client()
        # try common demo passwords
        logged = False
        for pwd in ("AdminPass123!", "admin", "password", "StrongPass123!"):
            if admin_client.login(username=admin.email, password=pwd) or admin_client.login(
                username=admin.username, password=pwd
            ):
                logged = True
                break
        if logged:
            check_role(report, "admin", admin_client, cases, fx)
        else:
            # force_login avoids password unknown
            admin_client.force_login(admin)
            check_role(report, "admin", admin_client, cases, fx)

    # Extra: POST exercise submit as student (smoke)
    if student_client and fx["exercise"]:
        url = reverse("exercises:detail", kwargs={"pk": fx["exercise"].pk})
        try:
            resp = student_client.post(url, {"sql_code": "SELECT 1;", "code": "SELECT 1;"})
            ok = resp.status_code < 500
            report.add(
                role="student",
                method="POST",
                path=url,
                name="exercises:submit-smoke",
                status=resp.status_code,
                ok=ok,
                note="submit smoke (any non-500)",
            )
        except Exception as exc:  # noqa: BLE001
            report.add(
                role="student",
                method="POST",
                path=url,
                name="exercises:submit-smoke",
                status="EXC",
                ok=False,
                note=repr(exc),
            )

    # List all URL patterns count
    flat = []

    def collect(patterns, prefix=""):
        for p in patterns:
            if hasattr(p, "url_patterns"):
                collect(p.url_patterns, prefix + str(p.pattern))
            else:
                flat.append(prefix + str(p.pattern))

    collect(get_resolver().url_patterns)
    print(f"\nResolved URL pattern leaves: {len(flat)}")

    report.print_summary()

    # Write JSON for review
    out = [
        {
            "role": r.role,
            "method": r.method,
            "path": r.path,
            "name": r.name,
            "status": r.status,
            "ok": r.ok,
            "note": r.note,
        }
        for r in report.results
    ]
    with open("scripts/qa_url_matrix_results.json", "w", encoding="utf-8") as f:
        json.dump(out, f, indent=2, ensure_ascii=False)
    print("\nWrote scripts/qa_url_matrix_results.json")

    fails = sum(1 for r in report.results if not r.ok)
    sys.exit(1 if fails else 0)


if __name__ == "__main__":
    main()
