"""Lookup English/Russian for SQL skill-test titles, tasks, options, editorials."""

from __future__ import annotations

import re

from .languages import LANG_EN, LANG_RU
from .sql_quizzes_data import QUIZZES, QUIZZES_NORM

_OPT_PREFIX = re.compile(r"^([A-D]\)\s*)(.*)$", re.S)
# Apostrophe variants in To'g'ri
_EDITORIAL = re.compile(
    r"^(To[\u2018\u2019\u02bb'ʻʼ´]?g[\u2018\u2019\u02bb'ʻʼ´]?ri javob:\s*)([A-D])(\.\s*)(.*)$",
    re.S,
)


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


def _row(text: str) -> dict[str, str] | None:
    return QUIZZES.get(text) or QUIZZES_NORM.get(_norm(text))


def lookup_quiz(text: str | None, lang: str) -> str | None:
    if not text or lang not in (LANG_EN, LANG_RU):
        return None

    row = _row(text)
    if row:
        return row.get(lang)

    opt = _OPT_PREFIX.match(text)
    if opt:
        body_row = _row(opt.group(2))
        if body_row and body_row.get(lang):
            return opt.group(1) + body_row[lang]

    ed = _EDITORIAL.match(text)
    if ed:
        prefix, letter, mid, rest = ed.groups()
        from .catalog import lookup_exact

        prefix_tr = lookup_exact("To‘g‘ri javob:", lang) or {
            LANG_EN: "Correct answer:",
            LANG_RU: "Правильный ответ:",
        }.get(lang, prefix)
        rest_row = _row(rest)
        rest_tr = rest_row.get(lang) if rest_row else None
        if rest_tr is None and not rest.strip():
            rest_tr = ""
        if rest_tr is not None:
            return f"{prefix_tr} {letter}{mid}{rest_tr}"

    return None
