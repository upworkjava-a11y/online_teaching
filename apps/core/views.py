from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import connection
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.views import View


class HealthCheckView(View):
    def get(self, request):
        db_ok = False
        try:
            with connection.cursor() as cursor:
                cursor.execute("SELECT 1")
                db_ok = cursor.fetchone()[0] == 1
        except Exception:
            db_ok = False

        status = 200 if db_ok else 503
        return JsonResponse(
            {"status": "ok" if db_ok else "unhealthy", "database": db_ok},
            status=status,
        )


class RootRedirectView(View):
    def get(self, request):
        user = request.user
        if not user.is_authenticated:
            return redirect("courses:list")
        if user.is_admin:
            return redirect("admin:index")
        if user.is_teacher:
            return redirect("analytics:dashboard")
        return redirect("dashboard:home")


class RoleRequiredMixin(LoginRequiredMixin):
    """Kirish talab qilinadi. Mehmon uchun chiroyli o‘zbekcha sahifa."""

    allowed_roles: tuple[str, ...] = ()
    auth_gate_title = "Davom etish uchun hisob kerak"
    auth_gate_message = (
        "Mashq, test yoki uy vazifasini bajarish uchun tizimga kiring yoki ro‘yxatdan o‘ting."
    )

    def get_auth_gate_next(self) -> str:
        """GET uchun shu sahifa; POST uchun xavfsiz GET manzil (405 oldini olish)."""
        from apps.accounts.redirects import safe_next_url

        request = self.request
        if request.method in ("GET", "HEAD"):
            return request.get_full_path()
        referer = request.META.get("HTTP_REFERER", "")
        return safe_next_url(request, referer, fallback="/courses/") or "/courses/"

    def handle_no_permission(self):
        from apps.core.i18n.service import t

        if self.request.user.is_authenticated:
            return redirect("root")
        return render(
            self.request,
            "accounts/auth_gate.html",
            {
                "next": self.get_auth_gate_next(),
                "gate_title": t(self.auth_gate_title),
                "gate_message": t(self.auth_gate_message),
            },
            status=200,
        )

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return self.handle_no_permission()
        if self.allowed_roles and request.user.role not in self.allowed_roles:
            if request.user.is_admin:
                return redirect("admin:index")
            if request.user.is_teacher:
                return redirect("analytics:dashboard")
            return redirect("dashboard:home")
        return super().dispatch(request, *args, **kwargs)


class GuestBrowseMixin:
    """Mehmon ham ko‘ra oladi; login bo‘lsa rol tekshiriladi."""

    allowed_roles: tuple[str, ...] = ()

    def dispatch(self, request, *args, **kwargs):
        user = request.user
        if user.is_authenticated and self.allowed_roles and user.role not in self.allowed_roles:
            if user.is_admin:
                return redirect("admin:index")
            if user.is_teacher:
                return redirect("analytics:dashboard")
            return redirect("dashboard:home")
        return super().dispatch(request, *args, **kwargs)
