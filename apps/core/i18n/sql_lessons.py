"""Full English/Russian HTML for SQL teacher lessons.

Phrase-level replacement turns lesson prose into mixed-language soup.
These are complete lesson bodies; SQL, <pre>/<code>, and schema names stay Latin.
"""

from __future__ import annotations

from .languages import LANG_EN, LANG_RU
from .sql_lessons_data import SQL_LESSON_HTML

_SOURCE_INDEX: dict[str, str] | None = None


def _norm(html: str) -> str:
    return " ".join((html or "").split())


def _source_index() -> dict[str, str]:
    global _SOURCE_INDEX
    if _SOURCE_INDEX is None:
        from apps.core.sql_teacher_lessons import ADVANCED_LECTURES, LECTURES

        _SOURCE_INDEX = {
            _norm(html): slug for slug, html in {**LECTURES, **ADVANCED_LECTURES}.items()
        }
    return _SOURCE_INDEX


def lookup_sql_lesson(html: str | None, lang: str, slug: str | None = None) -> str | None:
    if lang not in (LANG_EN, LANG_RU):
        return None
    key = (slug or "").strip() or None
    if not key:
        key = _source_index().get(_norm(html or ""))
    row = SQL_LESSON_HTML.get(key or "")
    if not row:
        return None
    return row.get(lang)
