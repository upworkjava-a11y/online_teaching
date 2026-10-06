"""Execute runnable Python lecture examples; report failures."""
from __future__ import annotations

import contextlib
import io
import os
import re
import sys
import traceback

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.local")
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from apps.core.python_content import build_python_modules

SKIP_MARKERS = (
    "agar revenue",
    "if amount = 0",
    "syntaxerror",
    "qavs yopilmagan",
    "yopilmagan",
    "pseudocode",
    "python emas",
)


def looks_like_python(code: str) -> bool:
    code = code.strip()
    if not code:
        return False
    low = code.lower()
    if any(m in low for m in SKIP_MARKERS):
        return False
    if "→" in code or "=>" in code and "def " not in code and "=" not in code.split("\n")[0]:
        if "def " not in code and "print" not in code and "import" not in code:
            return False
    # require at least one python-ish token
    return bool(
        re.search(
            r"\b(def|print|import|for|if|return|np\.|pd\.|df\[|=\s*)\b",
            code,
        )
    )


def unescape(code: str) -> str:
    return (
        code.replace("&gt;", ">")
        .replace("&lt;", "<")
        .replace("&amp;", "&")
        .replace("&quot;", '"')
    )


def main() -> int:
    fails = []
    ok = 0
    skipped = 0
    for m in build_python_modules():
        for lec in m["lectures"]:
            samples = list(lec.get("sql_examples") or [])
            for block in re.findall(r"<pre[^>]*>(.*?)</pre>", lec.get("content") or "", flags=re.S):
                samples.append(block)
            for i, raw in enumerate(samples):
                code = unescape(raw)
                code = re.sub(r"</?code[^>]*>", "", code).strip()
                label = f"{m['slug']}/{lec['slug']}#{i}"
                if not looks_like_python(code):
                    skipped += 1
                    continue
                buf = io.StringIO()
                try:
                    with contextlib.redirect_stdout(buf), contextlib.redirect_stderr(buf):
                        # isolated namespace
                        ns = {}
                        exec(compile(code, label, "exec"), ns, ns)
                    ok += 1
                except Exception as exc:  # noqa: BLE001
                    fails.append((label, f"{type(exc).__name__}: {exc}", code[:200]))

    out = os.path.join(os.path.dirname(__file__), "_qa_python_exec_out.txt")
    lines = [f"ok={ok} fail={len(fails)} skipped={skipped}"]
    for label, err, snip in fails:
        lines.append(f"FAIL {label}: {err}")
        lines.append(f"  CODE: {snip!r}")
    with open(out, "w", encoding="utf-8") as fh:
        fh.write("\n".join(lines) + "\n")
    print(f"Wrote {out} ok={ok} fail={len(fails)} skipped={skipped}")
    return 1 if fails else 0


if __name__ == "__main__":
    raise SystemExit(main())
