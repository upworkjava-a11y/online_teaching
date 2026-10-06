"""Avatar preset + secure upload (validate, crop square, WebP)."""

from __future__ import annotations

import io

from django.conf import settings
from django.core.exceptions import ValidationError
from django.core.files.base import ContentFile
from django.utils import timezone

from apps.accounts.avatars import DEFAULT_AVATAR_KEY, avatar_url as preset_url, normalize_avatar_key
from apps.social.models import SocialProfile

ALLOWED_CONTENT_TYPES = {"image/jpeg", "image/png", "image/webp"}
ALLOWED_FORMATS = {"JPEG", "PNG", "WEBP"}


def max_avatar_bytes() -> int:
    return int(getattr(settings, "SOCIAL_AVATAR_MAX_BYTES", 2 * 1024 * 1024))


def avatar_pixel_size() -> int:
    return int(getattr(settings, "SOCIAL_AVATAR_SIZE", 256))


def get_or_create_profile(user) -> SocialProfile:
    profile, _ = SocialProfile.objects.get_or_create(user=user)
    return profile


def resolve_avatar_url(user) -> str:
    profile = SocialProfile.objects.filter(user_id=user.pk).first()
    if profile is None:
        return preset_url(DEFAULT_AVATAR_KEY)
    if profile.avatar_image:
        return profile.avatar_image.url
    return preset_url(profile.avatar_preset or DEFAULT_AVATAR_KEY)


def set_preset_avatar(user, key: str) -> SocialProfile:
    profile = get_or_create_profile(user)
    profile.avatar_preset = normalize_avatar_key(key)
    if profile.avatar_image:
        profile.avatar_image.delete(save=False)
        profile.avatar_image = None
    profile.save()
    return profile


def _validate_and_process(uploaded) -> ContentFile:
    if uploaded is None:
        raise ValidationError("Rasm tanlanmadi.")
    size = getattr(uploaded, "size", 0) or 0
    if size <= 0:
        raise ValidationError("Bo‘sh fayl.")
    if size > max_avatar_bytes():
        raise ValidationError("Rasm hajmi juda katta.")

    content_type = getattr(uploaded, "content_type", "") or ""
    if content_type and content_type.lower() not in ALLOWED_CONTENT_TYPES:
        raise ValidationError("Faqat JPEG, PNG yoki WebP ruxsat etiladi.")

    # Reject SVG / HTML disguised as images
    name = (getattr(uploaded, "name", "") or "").lower()
    if name.endswith((".svg", ".svgz", ".html", ".htm", ".xml", ".gif")):
        raise ValidationError("Bu format ruxsat etilmagan.")

    try:
        from PIL import Image, UnidentifiedImageError
    except ImportError as exc:
        raise ValidationError("Rasm ishlov berish mavjud emas.") from exc

    raw = uploaded.read()
    uploaded.seek(0)
    # Magic-byte sniff: reject obvious non-images
    head = raw[:32].lstrip()
    if head.startswith(b"<") or head.startswith(b"<?xml") or b"<svg" in head[:200].lower():
        raise ValidationError("SVG/HTML ruxsat etilmagan.")

    try:
        img = Image.open(io.BytesIO(raw))
        # Decompression-bomb guard before full decode
        w0, h0 = img.size
        max_side = int(getattr(settings, "SOCIAL_AVATAR_MAX_DIMENSION", 4096))
        max_pixels = int(getattr(settings, "SOCIAL_AVATAR_MAX_PIXELS", 25_000_000))
        if w0 <= 0 or h0 <= 0:
            raise ValidationError("Noto‘g‘ri rasm o‘lchami.")
        if w0 > max_side or h0 > max_side or (w0 * h0) > max_pixels:
            raise ValidationError("Rasm o‘lchami juda katta.")
        img.load()
    except UnidentifiedImageError as exc:
        raise ValidationError("Haqiqiy rasm fayli emas.") from exc
    except ValidationError:
        raise
    except Exception as exc:  # noqa: BLE001
        raise ValidationError("Rasmni o‘qib bo‘lmadi.") from exc

    if (img.format or "").upper() not in ALLOWED_FORMATS:
        raise ValidationError("Faqat JPEG, PNG yoki WebP.")

    # Square center-crop
    w, h = img.size
    side = min(w, h)
    left = (w - side) // 2
    top = (h - side) // 2
    img = img.crop((left, top, left + side, top + side))
    target = avatar_pixel_size()
    img = img.resize((target, target), Image.Resampling.LANCZOS)
    if img.mode not in ("RGB", "RGBA"):
        img = img.convert("RGBA" if "A" in img.getbands() else "RGB")
    if img.mode == "RGBA":
        background = Image.new("RGB", img.size, (255, 255, 255))
        background.paste(img, mask=img.split()[-1])
        img = background
    elif img.mode != "RGB":
        img = img.convert("RGB")

    out = io.BytesIO()
    img.save(out, format="WEBP", quality=82, method=6)
    return ContentFile(out.getvalue())


def upload_avatar(user, uploaded) -> SocialProfile:
    processed = _validate_and_process(uploaded)
    profile = get_or_create_profile(user)
    filename = f"u{user.pk}-{int(timezone.now().timestamp())}.webp"
    if profile.avatar_image:
        profile.avatar_image.delete(save=False)
    profile.avatar_image.save(filename, processed, save=True)
    return profile
