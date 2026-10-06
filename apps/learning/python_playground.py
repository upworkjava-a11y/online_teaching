"""Helpers for Python lesson playground."""

from __future__ import annotations

import html
import re

_PRE_RE = re.compile(r"<pre[^>]*>(.*?)</pre>", re.I | re.S)
_TAG_RE = re.compile(r"<[^>]+>")


def extract_python_starter(content: str = "", examples: list | None = None) -> str:
    """Pick a short starter snippet for the lesson playground."""

    def looks_python(text: str) -> bool:
        low = text.lower()
        if "select " in low or low.startswith("select") or " from " in low:
            return False
        return any(
            token in low
            for token in ("print(", "import ", "def ", "for ", "if ", "=", "lambda")
        )

    for example in examples or []:
        text = str(example or "").strip()
        if text and "pseudocode" not in text.lower() and looks_python(text):
            return text
    for match in _PRE_RE.finditer(content or ""):
        raw = match.group(1)
        text = _TAG_RE.sub("", raw)
        text = html.unescape(text).strip()
        if not text:
            continue
        low = text.lower()
        if "pseudocode" in low or "python emas" in low:
            continue
        if looks_python(text):
            return text
    return 'print("Salom, tahlil!")\nprint(2 + 2)'
