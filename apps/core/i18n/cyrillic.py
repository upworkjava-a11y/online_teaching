"""Uzbek Latin → Cyrillic. SQL/code must be protected before calling this."""

from __future__ import annotations

import re

# Normalize curly / modifier apostrophes used in the content.
_APOS = str.maketrans(
    {
        "‘": "'",
        "’": "'",
        "ʻ": "'",
        "ʼ": "'",
        "´": "'",
        "`": "'",
        "′": "'",
    }
)

# Multi-char first (order matters).
_MULTI = [
    ("yo'", "йў"),
    ("Yo'", "Йў"),
    ("YO'", "ЙЎ"),
    ("o'", "ў"),
    ("O'", "Ў"),
    ("g'", "ғ"),
    ("G'", "Ғ"),
    ("sh", "ш"),
    ("Sh", "Ш"),
    ("SH", "Ш"),
    ("ch", "ч"),
    ("Ch", "Ч"),
    ("CH", "Ч"),
    ("ng", "нг"),
    ("Ng", "Нг"),
    ("NG", "НГ"),
    ("yo", "ё"),
    ("Yo", "Ё"),
    ("YO", "Ё"),
    ("yu", "ю"),
    ("Yu", "Ю"),
    ("YU", "Ю"),
    ("ya", "я"),
    ("Ya", "Я"),
    ("YA", "Я"),
    ("ye", "е"),
    ("Ye", "Е"),
    ("YE", "Е"),
]

_SINGLE = {
    "a": "а",
    "b": "б",
    "d": "д",
    "e": "е",
    "f": "ф",
    "g": "г",
    "h": "ҳ",
    "i": "и",
    "j": "ж",
    "k": "к",
    "l": "л",
    "m": "м",
    "n": "н",
    "o": "о",
    "p": "п",
    "q": "қ",
    "r": "р",
    "s": "с",
    "t": "т",
    "u": "у",
    "v": "в",
    "x": "х",
    "y": "й",
    "z": "з",
    "A": "А",
    "B": "Б",
    "D": "Д",
    "E": "Е",
    "F": "Ф",
    "G": "Г",
    "H": "Ҳ",
    "I": "И",
    "J": "Ж",
    "K": "К",
    "L": "Л",
    "M": "М",
    "N": "Н",
    "O": "О",
    "P": "П",
    "Q": "Қ",
    "R": "Р",
    "S": "С",
    "T": "Т",
    "U": "У",
    "V": "В",
    "X": "Х",
    "Y": "Й",
    "Z": "З",
}

_CYR_RE = re.compile(r"[А-Яа-яЁёЎўҚқҒғҲҳ]")


def looks_cyrillic(text: str) -> bool:
    if not text:
        return False
    letters = [ch for ch in text if ch.isalpha()]
    if not letters:
        return False
    cyr = sum(1 for ch in letters if _CYR_RE.match(ch))
    return cyr / len(letters) > 0.4


def latin_to_cyrillic(text: str) -> str:
    if not text or looks_cyrillic(text):
        return text
    out = text.translate(_APOS)
    for src, dst in _MULTI:
        out = out.replace(src, dst)
    return "".join(_SINGLE.get(ch, ch) for ch in out)
