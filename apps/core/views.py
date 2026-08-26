from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import connection
from django.http import JsonResponse
from django.shortcuts import redirect
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
            return redirect("accounts:login")
        if user.is_admin:
            return redirect("admin:index")
        if user.is_teacher:
            return redirect("analytics:dashboard")
        return redirect("dashboard:home")


class RoleRequiredMixin(LoginRequiredMixin):
    allowed_roles: tuple[str, ...] = ()

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
