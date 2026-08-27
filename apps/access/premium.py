"""Premium narxlar va to‘lov ma’lumotlari."""

from django.conf import settings

# Kurs slug → so‘m (default 50_000)
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


def price_for_course(slug: str) -> int:
    return COURSE_PREMIUM_PRICES.get(slug, DEFAULT_PREMIUM_PRICE)


def format_sum(amount: int) -> str:
    return f"{amount:,}".replace(",", " ") + " so‘m"


def premium_offer_context(course=None) -> dict:
    price_rows = []
    for slug, amount in COURSE_PREMIUM_PRICES.items():
        price_rows.append({"slug": slug, "amount": amount, "amount_label": format_sum(amount)})
    selected_price = price_for_course(course.slug) if course else DEFAULT_PREMIUM_PRICE
    return {
        "premium_price": selected_price,
        "premium_price_label": format_sum(selected_price),
        "premium_price_rows": price_rows,
        "premium_card_number": getattr(settings, "PREMIUM_CARD_NUMBER", PREMIUM_CARD_NUMBER),
        "premium_card_holder": getattr(settings, "PREMIUM_CARD_HOLDER", PREMIUM_CARD_HOLDER),
        "premium_telegram": getattr(settings, "PREMIUM_TELEGRAM", PREMIUM_TELEGRAM),
        "premium_telegram_url": getattr(settings, "PREMIUM_TELEGRAM_URL", PREMIUM_TELEGRAM_URL),
    }
