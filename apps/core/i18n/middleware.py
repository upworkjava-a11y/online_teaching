from django.utils.deprecation import MiddlewareMixin

from apps.core.i18n.languages import (
    DEFAULT_LANGUAGE,
    LANGUAGE_COOKIE,
    LANGUAGE_SESSION_KEY,
    normalize_language,
)
from apps.core.i18n.service import set_language


class LanguageMiddleware(MiddlewareMixin):
    def process_request(self, request):
        session_lang = None
        if hasattr(request, "session"):
            session_lang = request.session.get(LANGUAGE_SESSION_KEY)
        cookie_lang = request.COOKIES.get(LANGUAGE_COOKIE)
        lang = normalize_language(session_lang or cookie_lang or DEFAULT_LANGUAGE)
        request.LANGUAGE_CODE = lang
        set_language(lang)
        return None

    def process_response(self, request, response):
        lang = getattr(request, "LANGUAGE_CODE", DEFAULT_LANGUAGE)
        response.set_cookie(
            LANGUAGE_COOKIE,
            lang,
            max_age=60 * 60 * 24 * 365,
            samesite="Lax",
            httponly=False,
        )
        return response
