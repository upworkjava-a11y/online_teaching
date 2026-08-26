import json
import logging
import secrets
from dataclasses import dataclass
from urllib.parse import urlencode
from urllib.request import Request, urlopen

from django.conf import settings
from django.contrib.auth import login
from django.db import transaction
from django.urls import reverse

from .models import GoogleAccount, User
from .utils import unique_username_from_email

logger = logging.getLogger("apps.accounts")

GOOGLE_AUTH_URL = "https://accounts.google.com/o/oauth2/v2/auth"
GOOGLE_TOKEN_URL = "https://oauth2.googleapis.com/token"
GOOGLE_USERINFO_URL = "https://openidconnect.googleapis.com/v1/userinfo"
SESSION_STATE_KEY = "google_oauth_state"
SESSION_NEXT_KEY = "google_oauth_next"


class GoogleOAuthError(Exception):
    def __init__(self, message: str):
        super().__init__(message)
        self.message = message


@dataclass
class GoogleProfile:
    sub: str
    email: str
    email_verified: bool
    given_name: str
    family_name: str


def google_signin_enabled() -> bool:
    return bool(getattr(settings, "GOOGLE_CLIENT_ID", ""))


def google_oauth_configured() -> bool:
    return bool(settings.GOOGLE_CLIENT_ID and settings.GOOGLE_CLIENT_SECRET)


def build_redirect_uri(request) -> str:
    configured = getattr(settings, "GOOGLE_OAUTH_REDIRECT_URI", "") or ""
    if configured:
        return configured
    return request.build_absolute_uri(reverse("accounts:google_callback"))


def authorization_url(request) -> str:
    if not google_oauth_configured():
        raise GoogleOAuthError("Google orqali kirish hozircha sozlanmagan.")
    state = secrets.token_urlsafe(32)
    request.session[SESSION_STATE_KEY] = state
    next_url = request.GET.get("next") or ""
    if next_url.startswith("/"):
        request.session[SESSION_NEXT_KEY] = next_url
    params = {
        "client_id": settings.GOOGLE_CLIENT_ID,
        "redirect_uri": build_redirect_uri(request),
        "response_type": "code",
        "scope": "openid email profile",
        "state": state,
        "access_type": "online",
        "include_granted_scopes": "true",
        "prompt": "select_account",
        "hl": "uz",
    }
    return f"{GOOGLE_AUTH_URL}?{urlencode(params)}"


def _post_form(url: str, data: dict) -> dict:
    encoded = urlencode(data).encode("utf-8")
    request = Request(url, data=encoded, method="POST")
    request.add_header("Content-Type", "application/x-www-form-urlencoded")
    request.add_header("Accept", "application/json")
    with urlopen(request, timeout=15) as response:
        payload = response.read().decode("utf-8")
    return json.loads(payload)


def _get_json(url: str, access_token: str) -> dict:
    request = Request(url, method="GET")
    request.add_header("Authorization", f"Bearer {access_token}")
    request.add_header("Accept", "application/json")
    with urlopen(request, timeout=15) as response:
        payload = response.read().decode("utf-8")
    return json.loads(payload)


def fetch_google_profile(code: str, redirect_uri: str) -> GoogleProfile:
    token_payload = _post_form(
        GOOGLE_TOKEN_URL,
        {
            "code": code,
            "client_id": settings.GOOGLE_CLIENT_ID,
            "client_secret": settings.GOOGLE_CLIENT_SECRET,
            "redirect_uri": redirect_uri,
            "grant_type": "authorization_code",
        },
    )
    access_token = token_payload.get("access_token")
    if not access_token:
        logger.warning("google_oauth_token_missing")
        raise GoogleOAuthError("Google hisobini tasdiqlab bo‘lmadi.")
    info = _get_json(GOOGLE_USERINFO_URL, access_token)
    email = (info.get("email") or "").strip().lower()
    sub = str(info.get("sub") or "").strip()
    if not email or not sub:
        raise GoogleOAuthError("Google email manzilini qaytarmadi.")
    return GoogleProfile(
        sub=sub,
        email=email,
        email_verified=bool(info.get("email_verified")),
        given_name=(info.get("given_name") or "").strip(),
        family_name=(info.get("family_name") or "").strip(),
    )


def profile_from_idinfo(idinfo: dict) -> GoogleProfile:
    email = (idinfo.get("email") or "").strip().lower()
    sub = str(idinfo.get("sub") or "").strip()
    if not email or not sub:
        raise GoogleOAuthError("Google email manzilini qaytarmadi.")
    return GoogleProfile(
        sub=sub,
        email=email,
        email_verified=bool(idinfo.get("email_verified")),
        given_name=(idinfo.get("given_name") or "").strip(),
        family_name=(idinfo.get("family_name") or "").strip(),
    )


def verify_google_id_token(credential: str) -> GoogleProfile:
    if not google_signin_enabled():
        raise GoogleOAuthError("Google orqali kirish hozircha sozlanmagan.")
    if not credential:
        raise GoogleOAuthError("Google hisobi tanlanmadi.")
    try:
        from google.auth.transport import requests as google_requests
        from google.oauth2 import id_token
    except ImportError as exc:
        raise GoogleOAuthError("Google tasdiqlash kutubxonasi o‘rnatilmagan.") from exc
    try:
        idinfo = id_token.verify_oauth2_token(
            credential,
            google_requests.Request(),
            settings.GOOGLE_CLIENT_ID,
            clock_skew_in_seconds=10,
        )
    except Exception as exc:
        logger.warning("google_id_token_invalid", extra={"error": type(exc).__name__})
        raise GoogleOAuthError("Google hisobini tasdiqlab bo‘lmadi.") from exc
    issuer = idinfo.get("iss")
    if issuer not in {"accounts.google.com", "https://accounts.google.com"}:
        raise GoogleOAuthError("Google hisobini tasdiqlab bo‘lmadi.")
    return profile_from_idinfo(idinfo)


@transaction.atomic
def login_or_register_google(request, profile: GoogleProfile):
    if not profile.email_verified:
        raise GoogleOAuthError("Google email manzili tasdiqlanmagan.")

    account = GoogleAccount.objects.select_related("user").filter(google_sub=profile.sub).first()
    if account:
        user = account.user
        if user.is_blocked or not user.is_active:
            raise GoogleOAuthError("Hisobingiz bloklangan. Administrator bilan bog‘laning.")
        if account.email != profile.email:
            account.email = profile.email
            account.save(update_fields=["email", "updated_at"])
        login(request, user)
        return user, False

    user = User.objects.filter(email__iexact=profile.email).first()
    created = False
    if user:
        if user.is_blocked or not user.is_active:
            raise GoogleOAuthError("Hisobingiz bloklangan. Administrator bilan bog‘laning.")
        if hasattr(user, "google_account"):
            raise GoogleOAuthError("Bu email boshqa Google hisobiga bog‘langan.")
    else:
        user = User(
            email=profile.email,
            username=unique_username_from_email(profile.email),
            first_name=profile.given_name[:150],
            last_name=profile.family_name[:150],
            role=User.Role.STUDENT,
        )
        user.set_unusable_password()
        user.save()
        created = True

    GoogleAccount.objects.create(user=user, google_sub=profile.sub, email=profile.email)
    login(request, user)
    logger.info("google_oauth_success", extra={"user_id": user.pk, "account_created": created})
    return user, created
