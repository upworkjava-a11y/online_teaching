from django.contrib.auth import views as auth_views
from django.urls import path, reverse_lazy

from .forms import StyledPasswordResetForm, StyledSetPasswordForm
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
    path(
        "parolni-tiklash/",
        auth_views.PasswordResetView.as_view(
            template_name="accounts/password_reset_form.html",
            email_template_name="accounts/password_reset_email.txt",
            subject_template_name="accounts/password_reset_subject.txt",
            form_class=StyledPasswordResetForm,
            success_url=reverse_lazy("accounts:password_reset_done"),
        ),
        name="password_reset",
    ),
    path(
        "parolni-tiklash/yuborildi/",
        auth_views.PasswordResetDoneView.as_view(
            template_name="accounts/password_reset_done.html",
        ),
        name="password_reset_done",
    ),
    path(
        "parolni-tiklash/<uidb64>/<token>/",
        auth_views.PasswordResetConfirmView.as_view(
            template_name="accounts/password_reset_confirm.html",
            form_class=StyledSetPasswordForm,
            success_url=reverse_lazy("accounts:password_reset_complete"),
        ),
        name="password_reset_confirm",
    ),
    path(
        "parolni-tiklash/tayyor/",
        auth_views.PasswordResetCompleteView.as_view(
            template_name="accounts/password_reset_complete.html",
        ),
        name="password_reset_complete",
    ),
    path("google/login/", GoogleOAuthStartView.as_view(), name="google_login"),
    path("google/callback/", GoogleOAuthCallbackView.as_view(), name="google_callback"),
    path("google/token/", GoogleIdentityTokenView.as_view(), name="google_token"),
]
