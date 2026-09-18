"""Bilingual chrome for Russian-for-IT lessons (.rit-* classes)."""

from __future__ import annotations

import html as html_lib

from .english_banking_bilingual import BANNER, LESSONS, _t, enhance_eb_lesson
from .languages import normalize_language
from .russian_it_lessons import RIT_BANNER, RIT_LESSONS

_META_READY = False


def _ensure_rit_meta() -> None:
    global _META_READY
    if _META_READY:
        return
    from .english_banking_dialogues import DIALOGUES, ROLES
    from .russian_it_dialogues import RIT_DIALOGUES, RIT_ROLES

    LESSONS.update(RIT_LESSONS)
    DIALOGUES.update(RIT_DIALOGUES)
    ROLES.update(RIT_ROLES)
    _META_READY = True


def enhance_rit_lesson(html: str, lang: str | None, slug: str | None) -> str:
    """Keep Russian learning text; add bilingual headings/banner with RU-IT styling."""
    _ensure_rit_meta()
    lang = normalize_language(lang)
    out = enhance_eb_lesson(html, lang, slug)
    old_banner = html_lib.escape(_t(BANNER, lang))
    new_banner = html_lib.escape(_t(RIT_BANNER, lang))
    if old_banner != new_banner:
        out = out.replace(old_banner, new_banner, 1)
    for old, new in (
        ("eb-explain-label", "rit-explain-label"),
        ("eb-dialogue-tr", "rit-dialogue-tr"),
        ("eb-loc-mean", "rit-loc-mean"),
        ("eb-en-mean", "rit-en-mean"),
        ("eb-meaning", "rit-meaning"),
        ("eb-th-loc", "rit-th-loc"),
        ("eb-h-loc", "rit-h-loc"),
        ("eb-explain", "rit-explain"),
        ("eb-banner", "rit-banner"),
        ("eb-lesson", "rit-lesson"),
        ("eb-h", "rit-h"),
    ):
        out = out.replace(old, new)
    return out
