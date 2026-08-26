from django.conf import settings

from apps.accounts.google import google_oauth_configured, google_signin_enabled


def platform(request):
    return {
        "platform_name": getattr(settings, "PLATFORM_NAME", "Data Analytics Akademiyasi"),
        "google_oauth_enabled": google_signin_enabled(),
        "google_oauth_redirect_enabled": google_oauth_configured(),
        "google_client_id": getattr(settings, "GOOGLE_CLIENT_ID", ""),
    }
