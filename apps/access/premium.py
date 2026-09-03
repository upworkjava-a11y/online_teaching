"""Premium narxlar va to‘lov ma’lumotlari."""

from django.conf import settings

# Fallback (kurs DB da yo‘q yoki premium_price=0 bo‘lsa)
COURSE_PREMIUM_PRICES: dict[str, int] = {
    "sql": 50_000,
    "python": 50_000,
    "excel": 50_000,
    "statistics": 50_000,
    "power-bi": 50_000,
    "real-projects": 50_000,
}

DEFAULT_PREMIUM_PRICE = 50_000

PREMIUM_CARD_NUMBER = "9860 1201 4053 1134"
PREMIUM_CARD_HOLDER = "Orzikulov Javokhir"
PREMIUM_TELEGRAM = "@just_585"
PREMIUM_TELEGRAM_URL = "https://t.me/just_585"


def price_for_course(slug: str, course=None) -> int:
    """Admin dagi Course.premium_price asosiy manba; yo‘q bo‘lsa fallback."""
    if course is not None:
        amount = getattr(course, "premium_price", None)
        if amount:
            return int(amount)
    try:
        from apps.courses.models import Course

        row = Course.objects.filter(slug=slug).values_list("premium_price", flat=True).first()
        if row:
            return int(row)
    except Exception:
        pass
    return COURSE_PREMIUM_PRICES.get(slug, DEFAULT_PREMIUM_PRICE)


def format_sum(amount: int) -> str:
    from apps.core.i18n.service import t

    return f"{amount:,}".replace(",", " ") + " " + t("so‘m")


def premium_offer_context(course=None) -> dict:
    from apps.courses.models import Course

    price_rows = []
    for c in Course.objects.filter(is_published=True).order_by("order", "id"):
        amount = price_for_course(c.slug, course=c)
        price_rows.append(
            {
                "slug": c.slug,
                "title": c.title,
                "amount": amount,
                "amount_label": format_sum(amount),
            }
        )
    # Agar DB bo‘sh bo‘lsa (testlar), fallback jadval
    if not price_rows:
        for slug, amount in COURSE_PREMIUM_PRICES.items():
            price_rows.append({"slug": slug, "amount": amount, "amount_label": format_sum(amount)})

    selected_price = price_for_course(course.slug, course=course) if course else DEFAULT_PREMIUM_PRICE
    return {
        "premium_price": selected_price,
        "premium_price_label": format_sum(selected_price),
        "premium_price_rows": price_rows,
        "premium_card_number": getattr(settings, "PREMIUM_CARD_NUMBER", PREMIUM_CARD_NUMBER),
        "premium_card_holder": getattr(settings, "PREMIUM_CARD_HOLDER", PREMIUM_CARD_HOLDER),
        "premium_telegram": getattr(settings, "PREMIUM_TELEGRAM", PREMIUM_TELEGRAM),
        "premium_telegram_url": getattr(settings, "PREMIUM_TELEGRAM_URL", PREMIUM_TELEGRAM_URL),
    }
