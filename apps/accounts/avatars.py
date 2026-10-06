"""Preset profile avatars (small static SVGs, ~0.5–1.5 KB each)."""

from __future__ import annotations

DEFAULT_AVATAR_KEY = "avatar-01"

# id -> (label for picker, static path under /static/)
AVATAR_PRESETS: dict[str, tuple[str, str]] = {
    "avatar-01": ("Ko‘k", "avatars/avatar-01.svg"),
    "avatar-02": ("Yashil", "avatars/avatar-02.svg"),
    "avatar-03": ("Binafsha", "avatars/avatar-03.svg"),
    "avatar-04": ("To‘q sariq", "avatars/avatar-04.svg"),
    "avatar-05": ("Qizil", "avatars/avatar-05.svg"),
    "avatar-06": ("Moviy", "avatars/avatar-06.svg"),
    "avatar-07": ("Pushti", "avatars/avatar-07.svg"),
    "avatar-08": ("Kulrang", "avatars/avatar-08.svg"),
    "avatar-09": ("To‘q ko‘k", "avatars/avatar-09.svg"),
    "avatar-10": ("Zaytun", "avatars/avatar-10.svg"),
    "avatar-11": ("Indigo", "avatars/avatar-11.svg"),
    "avatar-12": ("Teal", "avatars/avatar-12.svg"),
}


def normalize_avatar_key(key: str | None) -> str:
    k = (key or "").strip()
    if k in AVATAR_PRESETS:
        return k
    return DEFAULT_AVATAR_KEY


def avatar_static_path(key: str | None) -> str:
    return AVATAR_PRESETS[normalize_avatar_key(key)][1]


def avatar_url(key: str | None) -> str:
    return f"/static/{avatar_static_path(key)}"


def avatar_choices() -> list[tuple[str, str]]:
    return [(k, label) for k, (label, _) in AVATAR_PRESETS.items()]
