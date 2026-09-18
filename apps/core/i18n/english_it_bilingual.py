"""
Bilingual chrome for English-for-IT lessons.

Reuses Banking enhancer (headings/banner/vocab/dialogues); swaps CSS to .eit-*.
"""

from __future__ import annotations

import html as html_lib

from .english_banking_bilingual import BANNER, LESSONS, _t, enhance_eb_lesson
from .english_it_lessons import EIT_BANNER, EIT_LESSONS
from .languages import normalize_language

_META_READY = False


def _ensure_eit_meta() -> None:
    global _META_READY
    if _META_READY:
        return
    from .english_banking_dialogues import DIALOGUES, ROLES
    from .english_it_dialogues import EIT_DIALOGUES, EIT_ROLES

    LESSONS.update(EIT_LESSONS)
    DIALOGUES.update(EIT_DIALOGUES)
    ROLES.update(EIT_ROLES)
    _META_READY = True


def enhance_eit_lesson(html: str, lang: str | None, slug: str | None) -> str:
    """Keep English learning text; add bilingual headings/banner with IT styling."""
    _ensure_eit_meta()
    lang = normalize_language(lang)
    out = enhance_eb_lesson(html, lang, slug)
    old_banner = html_lib.escape(_t(BANNER, lang))
    new_banner = html_lib.escape(_t(EIT_BANNER, lang))
    if old_banner != new_banner:
        out = out.replace(old_banner, new_banner, 1)
    for old, new in (
        ("eb-explain-label", "eit-explain-label"),
        ("eb-dialogue-tr", "eit-dialogue-tr"),
        ("eb-loc-mean", "eit-loc-mean"),
        ("eb-en-mean", "eit-en-mean"),
        ("eb-meaning", "eit-meaning"),
        ("eb-th-loc", "eit-th-loc"),
        ("eb-h-loc", "eit-h-loc"),
        ("eb-explain", "eit-explain"),
        ("eb-banner", "eit-banner"),
        ("eb-lesson", "eit-lesson"),
        ("eb-h", "eit-h"),
    ):
        out = out.replace(old, new)
    return out
