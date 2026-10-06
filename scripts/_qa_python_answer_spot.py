"""Spot-check quiz answers that look suspicious (hardcoded heuristics)."""
from __future__ import annotations

import os
import re
import sys

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.local")
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from apps.core.python_content import build_python_modules
from apps.core.python_skill_tests import MODULE_SKILL_TESTS, skill_tests_for_module

suspects: list[str] = []


def ans(q):
    rows = q.get("rows") or []
    return (rows[0][0] if rows else q.get("answer") or "").strip().upper()[:1]


def opts(q):
    return q.get("quiz_options") or []


def text(q):
    return " ".join(
        [
            q.get("title") or "",
            q.get("description") or "",
            q.get("quiz_prompt") or q.get("task") or "",
            " ".join(opts(q)),
        ]
    ).lower()


CHECKS = []


def check(where, q):
    a = ans(q)
    t = text(q)
    # print -> usually screen output = first option often A, verify letter matches content
    if "print(" in t and "ekranga" in t:
        # correct option should mention ekranga / chiqar
        for o in opts(q):
            if o.startswith(f"{a})") and "ekran" not in o.lower() and "chiqar" not in o.lower() and "hi" not in o.lower():
                suspects.append(f"{where}: print answer {a} option looks wrong: {o}")
    if "nameerror" in t and "amout" in t:
        if a != "B" and "nameerror" not in "".join(opts(q)).lower().split(f"{a})")[0][-20:]:
            # answer should be NameError option
            correct = next((o for o in opts(q) if "nameerror" in o.lower()), None)
            if correct and not correct.startswith(f"{a})"):
                suspects.append(f"{where}: NameError should be {correct[:1]} not {a}")
    if "unterminated string" in t or "qo‘shtirnoq yopilmagan" in t or "qoshtirnoq" in t:
        correct = next((o for o in opts(q) if "qo" in o.lower() or "string" in o.lower() or "yopil" in o.lower()), None)
        if correct and not correct.startswith(f"{a})"):
            suspects.append(f"{where}: string error answer mismatch {a} vs {correct}")
    if "shape?" in t or "200 qator" in t:
        if a != "B":
            suspects.append(f"{where}: shape (200,8) should be B got {a}")
    if "cities[-1]" in t or "cities = ['a','b','c']" in t:
        if a != "C":
            suspects.append(f"{where}: cities[-1] should be C got {a}")
    if "np.mean([10, 20, 30])" in t:
        if a != "A":
            suspects.append(f"{where}: mean should be A=20 got {a}")
    if "revenue = 2000000" in t and "vip" in t and "regular" in t:
        if a != "B":
            suspects.append(f"{where}: 2mln segment should be Regular/B got {a}")
    if "amounts = [10, 20, 30]" in t and "yig" in t:
        if a != "A":
            suspects.append(f"{where}: sum 60 should be A got {a}")
    if "bool(0)" in t:
        correct = next((o for o in opts(q) if "false" in o.lower()), None)
        if correct and not correct.startswith(f"{a})"):
            suspects.append(f"{where}: bool(0) False option mismatch {a} vs {correct}")
    if 'amount = "100"' in t or "amount = \"100\"" in t:
        # skill test
        if "'100100'" in t or "100100" in t:
            correct = next((o for o in opts(q) if "100100" in o), None)
            if correct and not correct.startswith(f"{a})"):
                suspects.append(f"{where}: str*2 answer mismatch")


def main():
    for m in build_python_modules():
        for lec, items in (m.get("practice") or {}).items():
            for q in items if isinstance(items, list) else [items]:
                check(f"{m['slug']}/{lec}/{q['slug']}", q)
        for q in m.get("exercises") or []:
            check(f"{m['slug']}/ex/{q['slug']}", q)
    for mod in MODULE_SKILL_TESTS:
        for q in skill_tests_for_module(mod):
            check(f"skill/{mod}/{q['slug']}", q)

    path = os.path.join(os.path.dirname(__file__), "_qa_python_answer_spot.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(f"suspects={len(suspects)}\n")
        for s in suspects:
            fh.write(s + "\n")
    print(f"Wrote {path} suspects={len(suspects)}")
    for s in suspects:
        print("SUSPECT:", s)
    return 1 if suspects else 0


if __name__ == "__main__":
    raise SystemExit(main())
