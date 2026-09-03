"""Full English/Russian texts for SQL puzzles (description, task, hints).

Do not phrase-replace. SQL keywords and schema names stay Latin.
"""

from __future__ import annotations

from .languages import LANG_EN, LANG_RU
from .sql_puzzles_data import PUZZLES, PUZZLES_NORM


def _norm(text: str) -> str:
    return (
        text.replace("\r\n", "\n")
        .replace("\r", "\n")
        .replace("‘", "'")
        .replace("’", "'")
        .replace("ʻ", "'")
        .replace("ʼ", "'")
        .replace("´", "'")
        .strip()
    )


def lookup_puzzle(text: str | None, lang: str) -> str | None:
    if not text or lang not in (LANG_EN, LANG_RU):
        return None
    row = PUZZLES.get(text) or PUZZLES_NORM.get(_norm(text))
    if not row:
        return None
    return row.get(lang)
