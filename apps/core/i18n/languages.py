LANGUAGE_COOKIE = "platform_lang"
LANGUAGE_SESSION_KEY = "platform_lang"

LANG_UZ = "uz"
LANG_CYRL = "uz-cyrl"
LANG_RU = "ru"
LANG_EN = "en"

SUPPORTED_LANGUAGES = (LANG_UZ, LANG_CYRL, LANG_RU, LANG_EN)
DEFAULT_LANGUAGE = LANG_UZ

LANGUAGES = (
    {
        "code": LANG_UZ,
        "name": "O‘zbekcha",
        "short": "Lotin",
        "html_lang": "uz",
        "flag": "uz",
    },
    {
        "code": LANG_CYRL,
        "name": "Ўзбекча",
        "short": "Кирилл",
        "html_lang": "uz-Cyrl",
        "flag": "uz",
    },
    {
        "code": LANG_RU,
        "name": "Русский",
        "short": "RU",
        "html_lang": "ru",
        "flag": "ru",
    },
    {
        "code": LANG_EN,
        "name": "English",
        "short": "EN",
        "html_lang": "en",
        "flag": "gb",
    },
)


def normalize_language(code: str | None) -> str:
    if not code:
        return DEFAULT_LANGUAGE
    value = str(code).strip().lower().replace("_", "-")
    if value in ("uz-cyrl", "uz-cyr", "kirill", "cyrl", "cyrillic"):
        return LANG_CYRL
    if value.startswith("ru"):
        return LANG_RU
    if value.startswith("en"):
        return LANG_EN
    if value.startswith("uz"):
        return LANG_UZ
    return DEFAULT_LANGUAGE
