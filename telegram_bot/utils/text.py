from __future__ import annotations

import html
import re
from html.parser import HTMLParser


class _TextExtractor(HTMLParser):
    def __init__(self):
        super().__init__()
        self.parts: list[str] = []
        self.links: list[str] = []
        self._skip = False

    def handle_starttag(self, tag, attrs):
        attrs_d = dict(attrs)
        if tag in {"script", "style"}:
            self._skip = True
        if tag in {"p", "br", "div", "h1", "h2", "h3", "li", "tr"}:
            self.parts.append("\n")
        href = attrs_d.get("href") or attrs_d.get("src")
        if href:
            self.links.append(href)

    def handle_endtag(self, tag):
        if tag in {"script", "style"}:
            self._skip = False

    def handle_data(self, data):
        if not self._skip:
            self.parts.append(data)


def html_to_text(raw: str, limit: int = 3500) -> str:
    if not raw:
        return ""
    parser = _TextExtractor()
    try:
        parser.feed(raw)
    except Exception:
        raw = re.sub(r"<[^>]+>", " ", raw)
        return raw[:limit]
    text = re.sub(r"\n{3,}", "\n\n", "".join(parser.parts)).strip()
    if len(text) > limit:
        text = text[: limit - 20] + "\n…"
    return text


def extract_links(raw: str) -> list[str]:
    if not raw:
        return []
    parser = _TextExtractor()
    try:
        parser.feed(raw)
    except Exception:
        return re.findall(r'https?://[^\s"<>]+', raw)[:8]
    seen = []
    for item in parser.links:
        if item not in seen:
            seen.append(item)
    return seen[:8]


def tg_escape(text: str) -> str:
    return html.escape(text or "", quote=False)
