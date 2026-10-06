"""Generate 20 collectible SVG badge artworks into static/badges/."""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1] / "static" / "badges"

# Category palettes: (rim, face, accent, highlight)
PALETTES = {
    "problem": ("#1d4ed8", "#3b82f6", "#93c5fd", "#dbeafe"),
    "mastery": ("#6d28d9", "#8b5cf6", "#c4b5fd", "#ede9fe"),
    "consistency": ("#c2410c", "#ea580c", "#fdba74", "#ffedd5"),
    "learning": ("#047857", "#10b981", "#6ee7b7", "#d1fae5"),
    "competition": ("#a16207", "#eab308", "#fde047", "#fef9c3"),
    "platform": ("#1e3a8a", "#4338ca", "#a5b4fc", "#e0e7ff"),
    "legend": ("#7c2d12", "#b45309", "#fbbf24", "#fff7ed"),
}


def frame(palette: str, inner: str, *, shape: str = "circle") -> str:
    rim, face, accent, hi = PALETTES[palette]
    if shape == "hex":
        base = f"""
  <polygon points="64,8 112,34 112,94 64,120 16,94 16,34" fill="{face}" stroke="{rim}" stroke-width="6"/>
  <polygon points="64,18 102,40 102,88 64,110 26,88 26,40" fill="{hi}" opacity="0.35"/>
"""
    elif shape == "shield":
        base = f"""
  <path d="M64 10 L108 28 V68 C108 96 88 114 64 120 C40 114 20 96 20 68 V28 Z"
        fill="{face}" stroke="{rim}" stroke-width="6"/>
  <path d="M64 20 L98 34 V66 C98 88 82 102 64 108 C46 102 30 88 30 66 V34 Z"
        fill="{hi}" opacity="0.28"/>
"""
    else:
        base = f"""
  <circle cx="64" cy="64" r="54" fill="{face}" stroke="{rim}" stroke-width="8"/>
  <circle cx="64" cy="64" r="46" fill="none" stroke="{accent}" stroke-width="3" opacity="0.7"/>
  <circle cx="48" cy="42" r="14" fill="{hi}" opacity="0.45"/>
"""
    ribbon = f"""
  <path d="M34 98 L28 122 L44 112 Z" fill="{rim}"/>
  <path d="M94 98 L100 122 L84 112 Z" fill="{rim}"/>
  <path d="M44 100 H84 V110 H44 Z" fill="{accent}"/>
"""
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 128 128" role="img">{base}{ribbon}{inner}</svg>'


BADGES: dict[str, tuple[str, str, str]] = {}

# slug -> (palette, shape, inner paths)
BADGES["first-step"] = (
    "problem",
    "circle",
    """
  <path d="M52 78 V50 H44 V42 H72 V50 H64 V78 Z" fill="#fff"/>
  <circle cx="64" cy="34" r="8" fill="#fff"/>
""",
)
BADGES["problem-solver"] = (
    "problem",
    "circle",
    """
  <rect x="38" y="40" width="24" height="24" rx="4" fill="#fff"/>
  <rect x="66" y="40" width="24" height="24" rx="4" fill="#fff" opacity="0.85"/>
  <rect x="38" y="68" width="24" height="24" rx="4" fill="#fff" opacity="0.85"/>
  <path d="M70 72 H86 V86 H70 Z" fill="none" stroke="#fff" stroke-width="4"/>
  <path d="M74 68 V60 M82 68 V60" stroke="#fff" stroke-width="3" stroke-linecap="round"/>
""",
)
BADGES["rising-coder"] = (
    "problem",
    "hex",
    """
  <path d="M40 84 L58 58 L70 70 L90 40" fill="none" stroke="#fff" stroke-width="6" stroke-linecap="round" stroke-linejoin="round"/>
  <path d="M78 40 H90 V52" fill="none" stroke="#fff" stroke-width="5" stroke-linecap="round"/>
  <rect x="42" y="86" width="10" height="6" fill="#fff" opacity="0.8"/>
  <rect x="56" y="80" width="10" height="12" fill="#fff"/>
  <rect x="70" y="74" width="10" height="18" fill="#fff" opacity="0.9"/>
""",
)
BADGES["challenge-hunter"] = (
    "problem",
    "shield",
    """
  <circle cx="64" cy="58" r="22" fill="none" stroke="#fff" stroke-width="5"/>
  <circle cx="64" cy="58" r="12" fill="none" stroke="#fff" stroke-width="4"/>
  <circle cx="64" cy="58" r="4" fill="#fff"/>
  <path d="M64 30 V38 M64 78 V86 M36 58 H44 M84 58 H92" stroke="#fff" stroke-width="4" stroke-linecap="round"/>
""",
)
BADGES["sql-explorer"] = (
    "mastery",
    "circle",
    """
  <ellipse cx="54" cy="48" rx="22" ry="10" fill="none" stroke="#fff" stroke-width="4"/>
  <path d="M32 48 V68 C32 74 42 78 54 78 C66 78 76 74 76 68 V48" fill="none" stroke="#fff" stroke-width="4"/>
  <circle cx="84" cy="78" r="14" fill="none" stroke="#fff" stroke-width="4"/>
  <path d="M94 88 L106 100" stroke="#fff" stroke-width="5" stroke-linecap="round"/>
""",
)
BADGES["join-master"] = (
    "mastery",
    "hex",
    """
  <circle cx="44" cy="58" r="14" fill="none" stroke="#fff" stroke-width="5"/>
  <circle cx="84" cy="58" r="14" fill="none" stroke="#fff" stroke-width="5"/>
  <path d="M58 58 H70" stroke="#fff" stroke-width="5" stroke-linecap="round"/>
  <circle cx="64" cy="58" r="5" fill="#fff"/>
  <path d="M44 44 V36 M84 44 V36 M44 72 V80 M84 72 V80" stroke="#fff" stroke-width="3" opacity="0.7"/>
""",
)
BADGES["window-wizard"] = (
    "mastery",
    "circle",
    """
  <rect x="36" y="36" width="56" height="48" rx="4" fill="none" stroke="#fff" stroke-width="4"/>
  <path d="M64 36 V84 M36 60 H92" stroke="#fff" stroke-width="4"/>
  <path d="M78 30 L82 38 L90 40 L82 42 L78 50 L74 42 L66 40 L74 38 Z" fill="#fff"/>
""",
)
BADGES["python-starter"] = (
    "mastery",
    "circle",
    """
  <path d="M52 34 C44 34 40 40 40 48 V58 H56 V52 C56 48 60 46 64 46 H78 C84 46 88 50 88 56 V66 C88 74 82 78 74 78 H64 C58 78 56 82 56 86 V94 H72 C80 94 88 88 88 78 V68 H72 V74 C72 76 70 78 66 78 H54 C46 78 40 72 40 64 V52 C40 42 46 34 56 34 Z" fill="#fff"/>
  <circle cx="70" cy="42" r="3" fill="#4338ca"/>
  <circle cx="58" cy="86" r="3" fill="#4338ca"/>
""",
)
BADGES["streak-3"] = (
    "consistency",
    "circle",
    """
  <path d="M64 28 C58 42 48 48 48 62 C48 76 56 84 64 92 C72 84 80 76 80 62 C80 48 70 42 64 28 Z" fill="#fff"/>
  <path d="M64 52 C62 58 58 60 58 66 C58 72 61 76 64 78 C67 76 70 72 70 66 C70 60 66 58 64 52 Z" fill="#ea580c"/>
""",
)
BADGES["streak-7"] = (
    "consistency",
    "hex",
    """
  <path d="M64 22 C56 40 44 46 44 64 C44 82 54 92 64 102 C74 92 84 82 84 64 C84 46 72 40 64 22 Z" fill="#fff"/>
  <path d="M64 48 C61 56 56 58 56 66 C56 74 60 78 64 82 C68 78 72 74 72 66 C72 58 67 56 64 48 Z" fill="#c2410c"/>
  <path d="M52 36 L48 28 M76 36 L80 28" stroke="#fff" stroke-width="3" stroke-linecap="round" opacity="0.8"/>
""",
)
BADGES["streak-30"] = (
    "consistency",
    "shield",
    """
  <path d="M64 18 C52 40 38 48 38 68 C38 90 50 102 64 112 C78 102 90 90 90 68 C90 48 76 40 64 18 Z" fill="#fff"/>
  <path d="M64 44 C60 54 52 58 52 68 C52 78 58 84 64 90 C70 84 76 78 76 68 C76 58 68 54 64 44 Z" fill="#9a3412"/>
  <circle cx="64" cy="34" r="4" fill="#fde68a"/>
""",
)
BADGES["first-lesson"] = (
    "learning",
    "circle",
    """
  <path d="M34 40 H62 V88 H34 Z" fill="#fff" opacity="0.9"/>
  <path d="M66 40 H94 V88 H66 Z" fill="#fff"/>
  <path d="M64 40 V88" stroke="#047857" stroke-width="3"/>
  <path d="M40 50 H56 M40 60 H56 M70 50 H86 M70 60 H86" stroke="#047857" stroke-width="3" opacity="0.5"/>
""",
)
BADGES["knowledge-seeker"] = (
    "learning",
    "hex",
    """
  <path d="M40 70 L64 42 L88 70 Z" fill="none" stroke="#fff" stroke-width="5"/>
  <circle cx="64" cy="70" r="10" fill="none" stroke="#fff" stroke-width="4"/>
  <path d="M64 80 V92" stroke="#fff" stroke-width="4" stroke-linecap="round"/>
  <rect x="48" y="34" width="32" height="8" rx="2" fill="#fff" opacity="0.85"/>
""",
)
BADGES["course-finisher"] = (
    "learning",
    "shield",
    """
  <circle cx="64" cy="52" r="18" fill="none" stroke="#fff" stroke-width="5"/>
  <path d="M50 70 L42 96 L64 84 L86 96 L78 70" fill="#fff"/>
  <path d="M56 48 L62 56 L74 42" fill="none" stroke="#047857" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>
""",
)
BADGES["top-10"] = (
    "competition",
    "circle",
    """
  <rect x="30" y="70" width="20" height="24" fill="#fff" opacity="0.75"/>
  <rect x="54" y="50" width="20" height="44" fill="#fff"/>
  <rect x="78" y="62" width="20" height="32" fill="#fff" opacity="0.85"/>
  <text x="64" y="42" text-anchor="middle" font-family="Arial,sans-serif" font-size="18" font-weight="700" fill="#fff">10</text>
""",
)
BADGES["top-3"] = (
    "competition",
    "hex",
    """
  <rect x="28" y="68" width="22" height="26" fill="#cd7f32"/>
  <rect x="53" y="48" width="22" height="46" fill="#fbbf24"/>
  <rect x="78" y="58" width="22" height="36" fill="#94a3b8"/>
  <text x="64" y="40" text-anchor="middle" font-family="Arial,sans-serif" font-size="16" font-weight="700" fill="#fff">TOP 3</text>
""",
)
BADGES["number-one"] = (
    "competition",
    "shield",
    """
  <path d="M40 34 H88 L80 48 H48 Z" fill="#fde047"/>
  <circle cx="64" cy="70" r="22" fill="#fff"/>
  <text x="64" y="78" text-anchor="middle" font-family="Arial,sans-serif" font-size="28" font-weight="800" fill="#a16207">1</text>
""",
)
BADGES["perfect-week"] = (
    "consistency",
    "circle",
    """
  <g fill="#fff">
    <rect x="30" y="44" width="12" height="12" rx="2"/>
    <rect x="46" y="44" width="12" height="12" rx="2"/>
    <rect x="62" y="44" width="12" height="12" rx="2"/>
    <rect x="78" y="44" width="12" height="12" rx="2"/>
    <rect x="38" y="62" width="12" height="12" rx="2"/>
    <rect x="54" y="62" width="12" height="12" rx="2"/>
    <rect x="70" y="62" width="12" height="12" rx="2"/>
  </g>
  <path d="M34 50 L38 54 L44 46" fill="none" stroke="#c2410c" stroke-width="2"/>
""",
)
BADGES["night-coder"] = (
    "platform",
    "hex",
    """
  <path d="M72 34 C58 36 48 48 50 62 C52 78 68 88 84 84 C72 90 56 84 50 70 C44 54 52 38 72 34 Z" fill="#fff"/>
  <rect x="40" y="78" width="48" height="22" rx="3" fill="#fff" opacity="0.9"/>
  <rect x="46" y="84" width="36" height="8" fill="#1e3a8a" opacity="0.35"/>
""",
)
BADGES["legend"] = (
    "legend",
    "shield",
    """
  <path d="M64 28 L70 48 L92 48 L74 62 L80 84 L64 70 L48 84 L54 62 L36 48 L58 48 Z" fill="#fbbf24" stroke="#fff" stroke-width="2"/>
  <circle cx="64" cy="56" r="26" fill="none" stroke="#fff" stroke-width="4" opacity="0.6"/>
""",
)

# Data-driven expansion (same visual language)
_EXTRA = {
    "century-coder": ("problem", "hex", '<text x="64" y="72" text-anchor="middle" font-family="Arial,sans-serif" font-size="28" font-weight="800" fill="#fff">100</text>'),
    "easy-starter": ("problem", "circle", '<text x="64" y="70" text-anchor="middle" font-family="Arial,sans-serif" font-size="18" font-weight="700" fill="#fff">EASY</text>'),
    "medium-solver": ("problem", "circle", '<text x="64" y="70" text-anchor="middle" font-family="Arial,sans-serif" font-size="14" font-weight="700" fill="#fff">MED</text>'),
    "hard-crusher": ("problem", "hex", '<text x="64" y="72" text-anchor="middle" font-family="Arial,sans-serif" font-size="16" font-weight="800" fill="#fff">HARD</text>'),
    "select-starter": ("mastery", "circle", '<text x="64" y="70" text-anchor="middle" font-family="Arial,sans-serif" font-size="14" font-weight="700" fill="#fff">SEL</text>'),
    "aggregation-master": ("mastery", "hex", '<text x="64" y="72" text-anchor="middle" font-family="Arial,sans-serif" font-size="13" font-weight="700" fill="#fff">AGG</text>'),
    "subquery-specialist": ("mastery", "circle", '<text x="64" y="70" text-anchor="middle" font-family="Arial,sans-serif" font-size="11" font-weight="700" fill="#fff">SUBQ</text>'),
    "cte-explorer": ("mastery", "hex", '<text x="64" y="72" text-anchor="middle" font-family="Arial,sans-serif" font-size="16" font-weight="800" fill="#fff">CTE</text>'),
    "case-crafter": ("mastery", "circle", '<text x="64" y="70" text-anchor="middle" font-family="Arial,sans-serif" font-size="14" font-weight="700" fill="#fff">CASE</text>'),
    "sql-solver": ("mastery", "shield", '<text x="64" y="72" text-anchor="middle" font-family="Arial,sans-serif" font-size="14" font-weight="700" fill="#fff">SQL</text>'),
    "sql-master": ("legend", "shield", '<text x="64" y="72" text-anchor="middle" font-family="Arial,sans-serif" font-size="12" font-weight="800" fill="#fff">SQL★</text>'),
    "banking-starter": ("learning", "circle", '<text x="64" y="70" text-anchor="middle" font-family="Arial,sans-serif" font-size="12" font-weight="700" fill="#fff">BANK</text>'),
    "deven-starter": ("learning", "circle", '<text x="64" y="70" text-anchor="middle" font-family="Arial,sans-serif" font-size="12" font-weight="700" fill="#fff">EN</text>'),
    "devru-starter": ("learning", "circle", '<text x="64" y="70" text-anchor="middle" font-family="Arial,sans-serif" font-size="12" font-weight="700" fill="#fff">RU</text>'),
    "python-solver": ("mastery", "hex", '<text x="64" y="72" text-anchor="middle" font-family="Arial,sans-serif" font-size="12" font-weight="700" fill="#fff">PY</text>'),
    "multi-skilled": ("platform", "hex", '<text x="64" y="72" text-anchor="middle" font-family="Arial,sans-serif" font-size="18" font-weight="800" fill="#fff">2+</text>'),
    "polyglot-learner": ("platform", "shield", '<text x="64" y="72" text-anchor="middle" font-family="Arial,sans-serif" font-size="18" font-weight="800" fill="#fff">3+</text>'),
    "streak-14": ("consistency", "circle", '<text x="64" y="70" text-anchor="middle" font-family="Arial,sans-serif" font-size="20" font-weight="800" fill="#fff">14</text>'),
}
for _slug, _spec in _EXTRA.items():
    BADGES[_slug] = _spec


def main() -> None:
    ROOT.mkdir(parents=True, exist_ok=True)
    # shared lock overlay used by CSS/UI optionally
    lock = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none">
  <rect x="5" y="10" width="14" height="10" rx="2" fill="#0f172a" fill-opacity="0.75"/>
  <path d="M8 10 V8 a4 4 0 0 1 8 0 v2" stroke="#f8fafc" stroke-width="2" stroke-linecap="round"/>
  <circle cx="12" cy="15" r="1.5" fill="#f8fafc"/>
</svg>"""
    (ROOT / "_lock.svg").write_text(lock, encoding="utf-8")
    for slug, (palette, shape, inner) in BADGES.items():
        svg = frame(palette, inner, shape=shape)
        (ROOT / f"{slug}.svg").write_text(svg, encoding="utf-8")
        print("wrote", slug)
    print("done", len(BADGES), "badges ->", ROOT)


if __name__ == "__main__":
    main()
