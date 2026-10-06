"""One-shot tester recheck for the Python course."""
from __future__ import annotations

import os
import re
import sys

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.local")
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import django

django.setup()

from apps.core.i18n.python_lessons_meta import PYTHON_LESSONS
from apps.core.python_content import build_python_modules
from apps.core.python_skill_tests import MODULE_SKILL_TESTS, skill_tests_for_module

EDITORIAL_RE = re.compile(r"^To‘g‘ri javob:\s*([A-D])")


def main() -> int:
    mods = build_python_modules()
    print(f"modules={len(mods)} lectures={sum(len(m['lectures']) for m in mods)}")

    missing_meta = [
        lec["slug"]
        for m in mods
        for lec in m["lectures"]
        if lec["slug"] not in PYTHON_LESSONS
    ]
    print(f"missing_meta={len(missing_meta)} {missing_meta[:5]}")

    structure_ok = 0
    structure_bad = []
    markers = ("Oddiy tilda", "Qadam-baqadam", "Dars maqsadi", "Lesson goal")
    for m in mods:
        for lec in m["lectures"]:
            html = lec.get("content") or ""
            if any(x in html for x in markers) and "py-editor" in html:
                structure_ok += 1
            else:
                structure_bad.append(lec["slug"])
    print(f"structure_ok={structure_ok} structure_bad={structure_bad}")

    ed_errs = []
    for mod in MODULE_SKILL_TESTS:
        for q in skill_tests_for_module(mod):
            ans = q["rows"][0][0]
            m = EDITORIAL_RE.match(q.get("editorial") or "")
            if not m or m.group(1) != ans:
                ed_errs.append(f"{mod}/{q['title']}: editorial={(m.group(1) if m else None)} ans={ans}")
    print(f"skill_editorial_mismatches={len(ed_errs)}")
    for e in ed_errs[:10]:
        print(" ", e)

    q = next(x for x in skill_tests_for_module("py-asoslari") if "bool(0)" in (x.get("task") or ""))
    print("bool(0)", q["rows"][0][0], q["quiz_options"])

    # DB freshness
    from django.apps import apps

    Course = None
    for label in ("courses.Course", "learning.Course", "catalog.Course", "content.Course"):
        try:
            Course = apps.get_model(label)
            break
        except LookupError:
            continue
    if Course is None:
        # discover
        for model in apps.get_models():
            if model.__name__ == "Course":
                Course = model
                break
    if Course is None:
        print("db=NO_COURSE_MODEL")
        return 0

    course = Course.objects.filter(slug="python").first()
    print(f"db_course={course}")
    if not course:
        return 0

    Lecture = None
    for model in apps.get_models():
        if model.__name__ == "Lecture":
            Lecture = model
            break
    if Lecture is None:
        print("db=NO_LECTURE_MODEL")
        return 0

    qs = Lecture.objects.filter(module__course=course)
    print(f"db_lectures={qs.count()}")
    sample = qs.filter(slug="py-noldan-start").first()
    if sample:
        html = sample.content or ""
        print(
            "db_start",
            {
                "Oddiy tilda": "Oddiy tilda" in html,
                "Dars maqsadi": "Dars maqsadi" in html,
                "py-editor": "py-editor" in html,
                "len": len(html),
            },
        )
        src = next(
            lec
            for m in mods
            for lec in m["lectures"]
            if lec["slug"] == "py-noldan-start"
        )
        stale = (sample.content or "").strip() != (src["content"] or "").strip()
        print(f"db_start_stale_vs_source={stale}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
