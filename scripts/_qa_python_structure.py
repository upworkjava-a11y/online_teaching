"""Deep QA: structure of every Python lecture + code sample quality."""
from __future__ import annotations

import ast
import os
import re
import sys

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.local")
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from apps.core.python_content import build_python_modules
from apps.core.python_skill_tests import MODULE_SKILL_TESTS, skill_tests_for_module

errors: list[str] = []
warns: list[str] = []


def unescape(code: str) -> str:
    return (
        code.replace("&gt;", ">")
        .replace("&lt;", "<")
        .replace("&amp;", "&")
        .replace("&quot;", '"')
    )


def main() -> int:
    mods = build_python_modules()
    out_lines = []
    for m in mods:
        if not m.get("lectures"):
            errors.append(f"{m['slug']}: no lectures")
        if not m.get("practice"):
            errors.append(f"{m['slug']}: no practice")
        if len(m.get("exercises") or []) < 2:
            errors.append(f"{m['slug']}: exercises<{2}")
        if not m.get("homework"):
            warns.append(f"{m['slug']}: no homework")

        for lec in m["lectures"]:
            html = lec.get("content") or ""
            slug = lec["slug"]
            where = f"{m['slug']}/{slug}"
            if "<h2" not in html.lower():
                errors.append(f"{where}: missing h2 structure")
            if not any(
                marker in html
                for marker in ("Dars maqsadi", "Oddiy tilda", "Qadam-baqadam", "Lesson goal")
            ):
                warns.append(f"{where}: no beginner structure heading")
            # orphan text quality
            if re.search(r"\d+_\d{3}", html):
                errors.append(f"{where}: underscore number in HTML")
            # code should use editor chrome
            if re.search(r"<pre(?![^>]*py-editor)", html, flags=re.I):
                # bare pre outside editor is a fail for python course
                bare = re.findall(r"<pre\b(?![^>]*class=\"py-editor)[^>]*>", html, flags=re.I)
                # after format, pre should be inside py-editor__code
                if "py-editor__code" not in html and bare:
                    errors.append(f"{where}: bare <pre> without editor chrome")
            if "<pre" in html.lower() and "py-editor" not in html:
                errors.append(f"{where}: code present but no py-editor")

            # every pre / editor code should look like real code or clearly marked comments/pseudocode
            for i, raw in enumerate(
                re.findall(r"<pre[^>]*>(.*?)</pre>", html, flags=re.S)
            ):
                code = unescape(raw).strip()
                label = f"{where}/pre{i}"
                if not code:
                    errors.append(f"{label}: empty pre")
                    continue
                # strip code tags
                code = re.sub(r"</?code[^>]*>", "", code)
                code = unescape(code).strip()
                low = code.lower()
                if "pseudocode" in low or "python emas" in low:
                    continue
                if "→" in code and "def " not in code and "print" not in code:
                    errors.append(f"{label}: arrow in pre without being real python")
                active = [ln for ln in code.splitlines() if ln.strip() and not ln.strip().startswith("#")]
                if not active:
                    continue
                try:
                    ast.parse(code)
                except SyntaxError as e:
                    errors.append(f"{label}: SyntaxError {e.msg}")

                if "\t" in code:
                    warns.append(f"{label}: tabs (prefer spaces)")
                if any(len(ln) > 100 for ln in code.splitlines()):
                    warns.append(f"{label}: line >100 chars")

            # sql_examples should also parse
            for i, ex in enumerate(lec.get("sql_examples") or []):
                code = unescape(ex)
                label = f"{where}/ex{i}"
                active = [ln for ln in code.splitlines() if ln.strip() and not ln.strip().startswith("#")]
                if not active:
                    continue
                try:
                    ast.parse(code)
                except SyntaxError as e:
                    errors.append(f"{label}: SyntaxError {e.msg}")

            # practice for lecture
            items = (m.get("practice") or {}).get(slug)
            if not items:
                warns.append(f"{where}: no practice quiz")

    # skill tests structure
    for mod in mods:
        qs = skill_tests_for_module(mod["slug"])
        if len(qs) != 11:
            errors.append(f"skill {mod['slug']}: {len(qs)} != 11")
        titles = [q["title"] for q in qs]
        if len(titles) != len(set(titles)):
            warns.append(f"skill {mod['slug']}: duplicate titles {titles}")

    # module order continuity
    orders = [m["order"] for m in mods]
    if orders != list(range(1, len(mods) + 1)):
        errors.append(f"module orders not 1..n: {orders}")

    path = os.path.join(os.path.dirname(__file__), "_qa_python_structure_out.txt")
    lines = [
        f"modules={len(mods)} lectures={sum(len(m['lectures']) for m in mods)}",
        f"ERRORS={len(errors)} WARNS={len(warns)}",
        *[f"ERR: {e}" for e in errors],
        *[f"WARN: {w}" for w in warns[:60]],
    ]
    with open(path, "w", encoding="utf-8") as fh:
        fh.write("\n".join(lines) + "\n")
    print(f"Wrote {path} errors={len(errors)} warns={len(warns)}")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
