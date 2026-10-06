"""Bilingual chrome for Python lessons (.py-* / np-* / pd-*)."""

from __future__ import annotations

import html as html_lib
import re

from .languages import LANG_EN, LANG_UZ, normalize_language
from .python_lessons_meta import PYTHON_BANNER, PYTHON_LESSONS

_H2_RE = re.compile(r"<h2>(.*?)</h2>", re.I | re.S)

_HEADING_LOC = {
    "Dars maqsadi": {
        LANG_UZ: "Dars maqsadi",
        "uz-cyrl": "Дарс мақсади",
        "ru": "Цель урока",
        LANG_EN: "Lesson goal",
    },
    "Kim uchun?": {
        LANG_UZ: "Kim uchun?",
        "uz-cyrl": "Ким учун?",
        "ru": "Для кого?",
        LANG_EN: "Who is this for?",
    },
    "Xulosa": {
        LANG_UZ: "Xulosa",
        "uz-cyrl": "Хулоса",
        "ru": "Итог",
        LANG_EN: "Summary",
    },
}


def _t(pack: dict[str, str], lang: str) -> str:
    return pack.get(lang) or pack.get(LANG_UZ) or next(iter(pack.values()), "")


def enhance_python_lesson(html: str, lang: str | None, slug: str | None) -> str:
    if not html:
        return ""
    lang = normalize_language(lang)
    slug = (slug or "").strip()
    meta = PYTHON_LESSONS.get(slug, {})
    goal = _t(meta["goal"], lang) if meta.get("goal") else ""

    def heading_sub(match: re.Match) -> str:
        inner = match.group(1).strip()
        plain = re.sub(r"<[^>]+>", "", inner).strip()
        pack = _HEADING_LOC.get(plain)
        if pack and lang not in (LANG_UZ, LANG_EN):
            loc = _t(pack, lang)
            return f'<h2 class="py-h">{inner}<span class="py-h-loc"> · {html_lib.escape(loc)}</span></h2>'
        return f'<h2 class="py-h">{inner}</h2>'

    out = _H2_RE.sub(heading_sub, html)
    banner = html_lib.escape(_t(PYTHON_BANNER, lang))
    explain_lbl = html_lib.escape(
        _t(
            {"uz": "Tushuntirish", "uz-cyrl": "Тушунтириш", "ru": "Пояснение", "en": "Explanation"},
            lang,
        )
    )
    goal_box = ""
    if goal:
        goal_box = (
            f'<aside class="py-explain"><div class="py-explain-label">{explain_lbl}</div>'
            f"<p>{html_lib.escape(goal)}</p></aside>"
        )
    return (
        f'<div class="py-lesson">'
        f'<div class="py-banner">{banner}</div>'
        f"{goal_box}"
        f"{out}"
        f"</div>"
    )
