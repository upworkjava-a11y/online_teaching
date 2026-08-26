from django.urls import path

from .views import (
    GoogleIdentityTokenView,
    GoogleOAuthCallbackView,
    GoogleOAuthStartView,
    ProfileView,
    RegisterView,
    StudentLoginView,
    StudentLogoutView,
)

app_name = "accounts"

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", StudentLoginView.as_view(), name="login"),
    path("logout/", StudentLogoutView.as_view(), name="logout"),
    path("profile/", ProfileView.as_view(), name="profile"),
    path("google/login/", GoogleOAuthStartView.as_view(), name="google_login"),
    path("google/callback/", GoogleOAuthCallbackView.as_view(), name="google_callback"),
    path("google/token/", GoogleIdentityTokenView.as_view(), name="google_token"),
]
