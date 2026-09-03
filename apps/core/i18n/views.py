from django.shortcuts import redirect
from django.views import View

from apps.accounts.redirects import safe_next_url
from apps.core.i18n.languages import LANGUAGE_COOKIE, LANGUAGE_SESSION_KEY, normalize_language
from apps.core.i18n.service import set_language


class SetLanguageView(View):
    def post(self, request):
        lang = normalize_language(request.POST.get("language"))
        request.session[LANGUAGE_SESSION_KEY] = lang
        set_language(lang)
        request.LANGUAGE_CODE = lang
        nxt = safe_next_url(request, request.POST.get("next") or request.META.get("HTTP_REFERER"), fallback="/courses/")
        response = redirect(nxt or "/courses/")
        response.set_cookie(
            LANGUAGE_COOKIE,
            lang,
            max_age=60 * 60 * 24 * 365,
            samesite="Lax",
        )
        return response

    def get(self, request):
        return redirect(safe_next_url(request, request.GET.get("next"), fallback="/courses/") or "/courses/")
