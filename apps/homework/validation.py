import os
import re

from django.conf import settings
from django.core.exceptions import ValidationError

from apps.core.i18n.service import t

ALLOWED_EXTENSIONS = {".txt"}
ALLOWED_MIME_PREFIXES = ("text/plain", "text/", "application/octet-stream")
SAFE_FILENAME = re.compile(r"^[\w\-. ]+$")


def validate_homework_file(uploaded) -> str:
    if not uploaded:
        raise ValidationError(t("Fayl tanlang."))

    name = os.path.basename(uploaded.name or "")
    if not name or not SAFE_FILENAME.match(name):
        raise ValidationError(t("Fayl nomi noto‘g‘ri."))

    ext = os.path.splitext(name)[1].lower()
    if ext not in ALLOWED_EXTENSIONS:
        raise ValidationError(t("Faqat .txt fayl yuborish mumkin."))

    max_bytes = settings.MAX_HOMEWORK_UPLOAD_MB * 1024 * 1024
    if uploaded.size > max_bytes:
        raise ValidationError(
            t("Fayl hajmi {n} MB dan oshmasligi kerak.").replace(
                "{n}", str(settings.MAX_HOMEWORK_UPLOAD_MB)
            )
        )

    content_type = (getattr(uploaded, "content_type", "") or "").lower()
    if content_type and not content_type.startswith(ALLOWED_MIME_PREFIXES):
        raise ValidationError(t("Fayl turi qo‘llab-quvvatlanmaydi."))

    raw = uploaded.read()
    uploaded.seek(0)
    if not raw:
        raise ValidationError(t("Fayl bo‘sh bo‘lmasligi kerak."))
    try:
        raw.decode("utf-8")
    except UnicodeDecodeError as exc:
        raise ValidationError(t("Fayl UTF-8 matn formatida bo‘lishi kerak.")) from exc

    if b"\x00" in raw:
        raise ValidationError(t("Ikkilik fayllar qabul qilinmaydi."))
    return name
