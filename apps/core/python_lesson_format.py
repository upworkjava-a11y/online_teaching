"""Format Python lesson HTML: healthy headings + VS Code-like editor blocks."""

from __future__ import annotations

import re

_PRE_RE = re.compile(r"<pre(\s[^>]*)?>(.*?)</pre>", re.I | re.S)
_H2_RE = re.compile(r"<h2\b", re.I)
_FIRST_P_RE = re.compile(r"<p>(.*?)</p>", re.I | re.S)
_ESP_RE = re.compile(
    r'(<div class="esp-(?:visual|try|scenario|cards)[^"]*">.*?</div>\s*)+',
    re.I | re.S,
)


def _guess_filename(code: str) -> str:
    low = code.lower()
    if "pseudocode" in low or "python emas" in low:
        return "notes.txt"
    if "import pandas" in low or "pd." in low:
        return "analysis.py"
    if "import numpy" in low or "np." in low:
        return "arrays.py"
    if "matplotlib" in low or "seaborn" in low or "plt." in low or "sns." in low:
        return "charts.py"
    if "def segment" in low:
        return "segment.py"
    if "def aov" in low or "def kpi" in low:
        return "metrics.py"
    if "read_csv" in low or "open(" in low or "csv" in low:
        return "io_demo.py"
    if "print(" in low and "def " not in low and "import " not in low:
        return "hello.py"
    return "main.py"


def wrap_code_editors(html: str) -> str:
    """Turn bare <pre> into a small editor chrome (traffic lights + filename)."""

    def repl(match: re.Match) -> str:
        inner = match.group(2)
        plain = re.sub(r"<[^>]+>", "", inner)
        plain = (
            plain.replace("&gt;", ">")
            .replace("&lt;", "<")
            .replace("&amp;", "&")
            .replace("&quot;", '"')
        )
        fname = _guess_filename(plain)
        is_notes = fname.endswith(".txt")
        lang = "Text" if is_notes else "Python"
        lang_cls = "is-notes" if is_notes else ""
        return (
            f'<div class="py-editor {lang_cls}">'
            f'<div class="py-editor__bar">'
            f'<span class="py-editor__dots" aria-hidden="true"><i></i><i></i><i></i></span>'
            f'<span class="py-editor__title">{fname}</span>'
            f'<span class="py-editor__lang">{lang}</span>'
            f"</div>"
            f'<pre class="py-editor__code"><code>{inner}</code></pre>'
            f"</div>"
        )

    return _PRE_RE.sub(repl, html)


def extract_goal_paragraph(structured_html: str) -> str:
    """Pull first paragraph under 'Dars maqsadi' from MODULES skeleton."""
    if not structured_html:
        return ""
    m = re.search(
        r"<h2[^>]*>\s*Dars maqsadi\s*</h2>\s*(<p>.*?</p>)",
        structured_html,
        flags=re.I | re.S,
    )
    return (m.group(1).strip() if m else "")


def ensure_healthy_structure(html: str, goal_p: str = "") -> str:
    """
    Teacher narrative lessons often have no h2. Inject a clear outline:
    Dars maqsadi → Batafsil → (code editors already in body).
    """
    if not html or _H2_RE.search(html):
        return html

    esp = ""
    body = html.strip()
    esp_m = _ESP_RE.match(body)
    if esp_m:
        esp = esp_m.group(0).rstrip() + "\n\n"
        body = body[esp_m.end() :].lstrip()

    goal_block = goal_p.strip()
    if not goal_block:
        first = _FIRST_P_RE.search(body)
        if first:
            # Use a short goal: keep first p as goal only if short
            text = re.sub(r"<[^>]+>", "", first.group(1)).strip()
            if len(text) <= 220:
                goal_block = first.group(0)
                body = (body[: first.start()] + body[first.end() :]).lstrip()
            else:
                goal_block = (
                    "<p>Bu darsda mavzuni o‘qiysiz, kod namunalarini ko‘rasiz "
                    "va keyin mashq yechasiz.</p>"
                )
        else:
            goal_block = (
                "<p>Bu darsda mavzuni o‘qiysiz, kod namunalarini ko‘rasiz "
                "va keyin mashq yechasiz.</p>"
            )

    # Label code sections lightly: insert h2 before first editor/pre if missing
    if "<pre" in body.lower() or "py-editor" in body:
        # Ensure a heading before the first code block
        body = re.sub(
            r"(?i)(?P<pre>(?:<div class=\"py-editor)|<pre\b)",
            r"<h2>Kod namunasi</h2>\n\g<pre>",
            body,
            count=1,
        )

    return (
        f"{esp}"
        f"<h2>Dars maqsadi</h2>\n{goal_block}\n\n"
        f"<h2>Batafsil tushuntirish</h2>\n{body}"
    )


def format_python_lesson(html: str, goal_p: str = "") -> str:
    html = ensure_healthy_structure(html.strip(), goal_p=goal_p)
    return wrap_code_editors(html)
