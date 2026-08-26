from django.conf import settings

from apps.accounts.google import google_oauth_configured, google_signin_enabled


def platform(request):
    return {
        "platform_name": getattr(settings, "PLATFORM_NAME", "Code with me"),
        "platform_motto": getattr(settings, "PLATFORM_MOTTO", "Data analitikani biz bilan o‘rganing"),
        "platform_tagline": getattr(settings, "PLATFORM_TAGLINE", "Code with me o‘quv platformasi"),
        "telegram_channel_url": getattr(settings, "TELEGRAM_CHANNEL_URL", "https://t.me/code_with_javohir"),
        "telegram_channel_label": getattr(settings, "TELEGRAM_CHANNEL_LABEL", "Kanalga o‘tish"),
        "google_oauth_enabled": google_signin_enabled(),
        "google_oauth_redirect_enabled": google_oauth_configured(),
        "google_client_id": getattr(settings, "GOOGLE_CLIENT_ID", ""),
    }
