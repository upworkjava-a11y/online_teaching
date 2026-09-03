from __future__ import annotations

import re
import threading

from .catalog import lookup_exact
from .cyrillic import latin_to_cyrillic
from .languages import DEFAULT_LANGUAGE, LANG_CYRL, LANG_EN, LANG_RU, LANG_UZ, normalize_language
from .protect import protect_sql_and_code, restore_protected

_local = threading.local()
_HTML_SPLIT = re.compile(r"(<[^>]+>)")


def set_language(code: str) -> str:
    lang = normalize_language(code)
    _local.code = lang
    return lang


def get_language() -> str:
    return getattr(_local, "code", DEFAULT_LANGUAGE)


def t(message: str, lang: str | None = None) -> str:
    """Translate a UI/chrome string. Unknown strings fall through to localize()."""
    if not message:
        return message
    return localize(str(message), lang)


def localize(text: str | None, lang: str | None = None) -> str:
    if text is None:
        return ""
    raw = str(text)
    if not raw:
        return raw
    lang = normalize_language(lang or get_language())
    if lang == LANG_UZ:
        return raw

    exact = lookup_exact(raw, lang)
    if exact is not None:
        return exact

    stripped = raw.strip()
    if stripped != raw:
        exact = lookup_exact(stripped, lang)
        if exact is not None:
            return exact
        raw = stripped

    from .sql_puzzles import lookup_puzzle

    puzzle = lookup_puzzle(raw, lang)
    if puzzle is not None:
        return puzzle

    from .sql_quizzes import lookup_quiz

    quiz = lookup_quiz(raw, lang)
    if quiz is not None:
        return quiz

    suffix = " uy vazifasi"
    if raw.endswith(suffix) and lang in (LANG_CYRL, LANG_RU, LANG_EN):
        head = raw[: -len(suffix)].strip()
        head_tr = lookup_exact(head, lang)
        ending = {
            LANG_CYRL: " уй вазифаси",
            LANG_RU: " — домашнее задание",
            LANG_EN: " homework",
        }[lang]
        if head_tr:
            return head_tr + ending
        if lang == LANG_CYRL:
            masked, tokens = protect_sql_and_code(head)
            return restore_protected(latin_to_cyrillic(masked), tokens) + ending

    masked, tokens = protect_sql_and_code(raw)
    if lang == LANG_CYRL:
        masked = latin_to_cyrillic(masked)
    return restore_protected(masked, tokens)


def localize_html(html: str | None, lang: str | None = None, slug: str | None = None) -> str:
    if not html:
        return ""
    lang = normalize_language(lang or get_language())
    if lang == LANG_UZ:
        return html

    from .sql_lessons import lookup_sql_lesson

    translated = lookup_sql_lesson(html, lang, slug=slug)
    if translated:
        return translated

    masked, tokens = protect_sql_and_code(html)
    if lang == LANG_CYRL:
        parts = _HTML_SPLIT.split(masked)
        out = []
        for part in parts:
            if not part:
                continue
            if part.startswith("<") and part.endswith(">"):
                out.append(part)
            else:
                out.append(latin_to_cyrillic(part))
        return restore_protected("".join(out), tokens)
    # Russian/English: never stitch word-by-word. Untranslated HTML stays Uzbek.
    return html
