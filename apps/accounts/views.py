import logging
from urllib.error import HTTPError, URLError

from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import FormView, UpdateView

from .forms import EmailAuthenticationForm, ProfileForm, StudentRegistrationForm
from .google import (
    GoogleOAuthError,
    SESSION_NEXT_KEY,
    SESSION_STATE_KEY,
    authorization_url,
    build_redirect_uri,
    fetch_google_profile,
    google_oauth_configured,
    google_signin_enabled,
    login_or_register_google,
    verify_google_id_token,
)
from .models import User
from .redirects import safe_next_url

logger = logging.getLogger("apps.accounts")


class RegisterView(FormView):
    template_name = "accounts/register.html"
    form_class = StudentRegistrationForm
    success_url = reverse_lazy("dashboard:home")

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("root")
        return super().dispatch(request, *args, **kwargs)

    def get_success_url(self):
        next_url = self.request.GET.get("next") or self.request.POST.get("next")
        return safe_next_url(self.request, next_url, fallback=super().get_success_url())

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        messages.success(self.request, "Ro‘yxatdan o‘tish muvaffaqiyatli yakunlandi.")
        return super().form_valid(form)


class StudentLoginView(LoginView):
    template_name = "accounts/login.html"
    authentication_form = EmailAuthenticationForm
    redirect_authenticated_user = True

    def form_invalid(self, form):
        logger.warning("authentication_failure", extra={"email": form.data.get("username")})
        return super().form_invalid(form)


class StudentLogoutView(LogoutView):
    next_page = reverse_lazy("courses:list")


class ProfileView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = ProfileForm
    template_name = "accounts/profile.html"
    success_url = reverse_lazy("accounts:profile")

    def get_object(self, queryset=None):
        return self.request.user

    def form_valid(self, form):
        password_changed = bool(form.cleaned_data.get("new_password1"))
        response = super().form_valid(form)
        if password_changed:
            # Parol o‘zgaganda sessiya uzilmasin
            from django.contrib.auth import update_session_auth_hash

            update_session_auth_hash(self.request, self.object)
            messages.success(self.request, "Profil va parol yangilandi.")
        else:
            messages.success(self.request, "Profil yangilandi.")
        return response


class GoogleOAuthStartView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect("root")
        if not google_oauth_configured():
            return render(request, "accounts/google_setup.html", status=200)
        try:
            return redirect(authorization_url(request))
        except GoogleOAuthError as exc:
            fallback = "accounts:register" if request.GET.get("from") == "register" else "accounts:login"
            messages.error(request, exc.message)
            return redirect(fallback)


class GoogleOAuthCallbackView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect("root")
        if request.GET.get("error"):
            messages.error(request, "Google orqali kirish bekor qilindi.")
            return redirect("accounts:login")
        state = request.GET.get("state")
        code = request.GET.get("code")
        expected = request.session.pop(SESSION_STATE_KEY, None)
        next_url = request.session.pop(SESSION_NEXT_KEY, None)
        if not code or not state or not expected or state != expected:
            logger.warning("google_oauth_invalid_state")
            messages.error(request, "Google orqali kirish xavfsizlik tekshiruvidan o‘tmadi. Qayta urinib ko‘ring.")
            return redirect("accounts:login")
        if not google_oauth_configured():
            messages.error(request, "Google orqali kirish hozircha sozlanmagan.")
            return redirect("accounts:login")
        try:
            profile = fetch_google_profile(code, build_redirect_uri(request))
            _user, created = login_or_register_google(request, profile)
        except GoogleOAuthError as exc:
            messages.error(request, exc.message)
            return redirect("accounts:login")
        except (HTTPError, URLError, TimeoutError, ValueError):
            logger.warning("google_oauth_network_error")
            messages.error(request, "Google bilan bog‘lanib bo‘lmadi. Keyinroq qayta urinib ko‘ring.")
            return redirect("accounts:login")
        if created:
            messages.success(request, "Google hisobi orqali ro‘yxatdan o‘tdingiz.")
        target = safe_next_url(request, next_url)
        if target:
            return redirect(target)
        return redirect(reverse("root"))


class GoogleIdentityTokenView(View):
    def post(self, request):
        if request.user.is_authenticated:
            return redirect("root")
        if not google_signin_enabled():
            messages.error(request, "Google orqali kirish hozircha sozlanmagan.")
            return redirect("accounts:login")
        credential = request.POST.get("credential")
        next_url = request.POST.get("next") or request.GET.get("next") or ""
        try:
            profile = verify_google_id_token(credential)
            _user, created = login_or_register_google(request, profile)
        except GoogleOAuthError as exc:
            messages.error(request, exc.message)
            return redirect("accounts:login")
        if created:
            messages.success(request, "Google hisobi orqali ro‘yxatdan o‘tdingiz.")
        target = safe_next_url(request, next_url)
        if target:
            return redirect(target)
        return redirect(reverse("root"))
