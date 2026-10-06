"""Audit Python course quizzes + lecture code for structural/content errors."""
from __future__ import annotations

import ast
import os
import re
import sys

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.local")
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from apps.core.python_content import build_python_modules
from apps.core.python_puzzles import _quiz_topic_fingerprint
from apps.core.python_skill_tests import MODULE_SKILL_TESTS, skill_tests_for_module
from apps.core.python_teacher_lessons import LECTURES

errors: list[str] = []
warns: list[str] = []


def check_quiz(where: str, q: dict) -> None:
    opts = q.get("quiz_options") or []
    rows = q.get("rows") or []
    ans = rows[0][0] if rows else q.get("answer")
    if isinstance(ans, str):
        ans = ans.strip().upper()[:1]
    letters = []
    for o in opts:
        m = re.match(r"^([A-D])\)", str(o).strip())
        if m:
            letters.append(m.group(1))
    if len(opts) != 4:
        errors.append(f"{where}: expected 4 options got {len(opts)}")
    if letters and ans not in letters:
        errors.append(f"{where}: answer {ans!r} not in {letters} title={q.get('title')}")
    if len(set(letters)) != len(letters):
        errors.append(f"{where}: duplicate option letters")
    for k in ("slug", "title"):
        if not (q.get(k) or "").strip():
            errors.append(f"{where}: empty {k}")
    # Option text empty after letter
    for o in opts:
        body = re.sub(r"^[A-D]\)\s*", "", str(o).strip())
        if not body:
            errors.append(f"{where}: empty option body in {o!r}")


def extract_pre(html: str) -> list[str]:
    return re.findall(r"<pre>(.*?)</pre>", html or "", flags=re.S)


def check_code(label: str, code: str) -> None:
    code = (
        code.replace("&gt;", ">")
        .replace("&lt;", "<")
        .replace("&amp;", "&")
        .replace("&quot;", '"')
    )
    low = code.lower()
    if "pseudocode" in low or "python emas" in low or "agar revenue" in low:
        return
    if re.search(r"(?<![A-Za-z0-9_])\d+_\d+", code):
        errors.append(f"{label}: underscore number literal -> {code[:90]!r}")
    lines = [ln for ln in code.splitlines() if ln.strip() and not ln.strip().startswith("#")]
    if not lines:
        return
    # intentional broken demos
    if "syntaxerror" in low and "yopilmagan" in low:
        return
    if "if amount = 0" in code:
        return
    try:
        ast.parse(code)
    except SyntaxError as exc:
        errors.append(f"{label}: SyntaxError {exc.msg} line={exc.lineno} :: {code[:100]!r}")


def dump_quiz_review() -> None:
    """Print all quizzes for manual answer review (compact)."""
    print("\n========== QUIZ REVIEW ==========")
    mods = build_python_modules()
    for m in mods:
        print(f"\n## {m['slug']}")
        for lec_slug, items in (m.get("practice") or {}).items():
            for q in items if isinstance(items, list) else [items]:
                ans = (q.get("rows") or [["?"]])[0][0]
                print(f"  [{lec_slug}] {q['slug']} | {q['title']} | ANS={ans}")
                print(f"    Q: {q.get('description','')} // {q.get('quiz_prompt') or q.get('task','')}")
                for o in q.get("quiz_options") or []:
                    print(f"      {o}")
        for q in m.get("exercises") or []:
            ans = (q.get("rows") or [["?"]])[0][0]
            print(f"  [module-ex] {q['slug']} | {q['title']} | ANS={ans}")
            print(f"    Q: {q.get('description','')} // {q.get('quiz_prompt') or q.get('task','')}")
            for o in q.get("quiz_options") or []:
                print(f"      {o}")

    print("\n========== SKILL TESTS ==========")
    for mod_slug in MODULE_SKILL_TESTS:
        print(f"\n## skill {mod_slug}")
        for q in skill_tests_for_module(mod_slug):
            ans = (q.get("rows") or [["?"]])[0][0]
            print(f"  {q['slug']} | {q['title']} | ANS={ans}")
            print(f"    Q: {q.get('description','')} // {q.get('quiz_prompt') or q.get('task','')}")
            for o in q.get("quiz_options") or []:
                print(f"      {o}")


def main() -> int:
    mods = build_python_modules()
    quiz_count = 0
    for m in mods:
        for lec_slug, items in (m.get("practice") or {}).items():
            for q in items if isinstance(items, list) else [items]:
                check_quiz(f"{m['slug']}/{lec_slug}/{q['slug']}", q)
                quiz_count += 1
        for q in m.get("exercises") or []:
            check_quiz(f"{m['slug']}/ex/{q['slug']}", q)
            quiz_count += 1
        # topic dedupe within module
        module_tags: set[str] = set()
        for items in (m.get("practice") or {}).values():
            for q in items if isinstance(items, list) else [items]:
                tags = set(_quiz_topic_fingerprint(q))
                if tags & module_tags:
                    # same lecture pair already enforced; module-wide soft warn
                    warns.append(f"{m['slug']}: soft topic reuse {tags & module_tags} in {q['slug']}")
                module_tags |= tags
        for q in m.get("exercises") or []:
            tags = set(_quiz_topic_fingerprint(q))
            if tags & module_tags:
                errors.append(f"{m['slug']}: module ex {q['slug']} overlaps lecture topics {tags & module_tags}")
            module_tags |= tags

        for lec in m["lectures"]:
            for i, ex in enumerate(lec.get("sql_examples") or []):
                check_code(f"{m['slug']}/{lec['slug']}/ex{i}", ex)
            for j, block in enumerate(extract_pre(lec.get("content") or "")):
                check_code(f"{m['slug']}/{lec['slug']}/pre{j}", block)

    for slug, html in LECTURES.items():
        for j, block in enumerate(extract_pre(html)):
            check_code(f"teacher/{slug}/pre{j}", block)

    skill_count = 0
    for mod_slug in MODULE_SKILL_TESTS:
        for q in skill_tests_for_module(mod_slug):
            check_quiz(f"skill/{mod_slug}/{q.get('slug')}", q)
            skill_count += 1

    # lecture slug uniqueness
    lec_slugs = []
    for m in mods:
        for lec in m["lectures"]:
            lec_slugs.append(lec["slug"])
    dup_lec = {s for s in lec_slugs if lec_slugs.count(s) > 1}
    if dup_lec:
        errors.append(f"duplicate lecture slugs: {sorted(dup_lec)}")

    # exercise slug uniqueness across course
    all_slugs = []
    for m in mods:
        for items in (m.get("practice") or {}).values():
            for q in items if isinstance(items, list) else [items]:
                all_slugs.append(q["slug"])
        for q in m.get("exercises") or []:
            all_slugs.append(q["slug"])
    for mod_slug in MODULE_SKILL_TESTS:
        for q in skill_tests_for_module(mod_slug):
            all_slugs.append(q["slug"])
    seen = {}
    for s in all_slugs:
        seen[s] = seen.get(s, 0) + 1
    for s, n in sorted(seen.items()):
        if n > 1:
            errors.append(f"duplicate exercise/skill slug {s} x{n}")

    out_path = os.path.join(os.path.dirname(__file__), "_qa_python_audit_out.txt")
    lines = [
        f"modules={len(mods)} practice+module_ex={quiz_count} skill={skill_count}",
        f"ERRORS={len(errors)} WARNS={len(warns)}",
    ]
    lines.extend(f"ERR: {e}" for e in errors)
    lines.extend(f"WARN: {w}" for w in warns[:80])
    text = "\n".join(lines) + "\n"
    with open(out_path, "w", encoding="utf-8") as fh:
        fh.write(text)
        if "--review" in sys.argv:
            # capture review into same file
            import io
            buf = io.StringIO()
            old = sys.stdout
            sys.stdout = buf
            try:
                dump_quiz_review()
            finally:
                sys.stdout = old
            fh.write(buf.getvalue())
    print(f"Wrote {out_path} errors={len(errors)} warns={len(warns)}")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
