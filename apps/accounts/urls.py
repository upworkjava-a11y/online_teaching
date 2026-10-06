from django.urls import path
from django.views.generic import RedirectView

from .views import (
    GoogleIdentityTokenView,
    GoogleOAuthCallbackView,
    GoogleOAuthStartView,
    RegisterView,
    StudentLoginView,
    StudentLogoutView,
)

app_name = "accounts"

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", StudentLoginView.as_view(), name="login"),
    path("logout/", StudentLogoutView.as_view(), name="logout"),
    # Unified edit lives at /profile/edit/ — keep name for old reverse() / bookmarks
    path(
        "profile/",
        RedirectView.as_view(pattern_name="social:settings", permanent=False),
        name="profile",
    ),
    path("google/login/", GoogleOAuthStartView.as_view(), name="google_login"),
    path("google/callback/", GoogleOAuthCallbackView.as_view(), name="google_callback"),
    path("google/token/", GoogleIdentityTokenView.as_view(), name="google_token"),
]
