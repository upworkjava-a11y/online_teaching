from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.views import View

from apps.core.i18n.service import t
from apps.core.views import RoleRequiredMixin
from apps.courses.models import Course, Module
from apps.progress.certificates import issue_course_certificate, issue_module_certificate, module_completion
from apps.progress.models import Certificate
from apps.progress.streak import get_streak


class CertificateListView(RoleRequiredMixin, View):
    allowed_roles = ("student",)
    auth_gate_title = "Sertifikatlar uchun hisob kerak"
    auth_gate_message = (
        "Sertifikatlaringizni ko‘rish uchun tizimga kiring yoki ro‘yxatdan o‘ting."
    )

    def get(self, request):
        certificates = Certificate.objects.filter(student=request.user).select_related("module", "course")
        streak = get_streak(request.user)
        return render(
            request,
            "progress/certificates.html",
            {"certificates": certificates, "streak": streak},
        )


class CertificateDetailView(RoleRequiredMixin, View):
    allowed_roles = ("student", "teacher", "admin")

    def get(self, request, code):
        cert = get_object_or_404(Certificate.objects.select_related("student", "module", "course"), code=code)
        if request.user.is_student and cert.student_id != request.user.pk:
            return render(request, "core/blocked.html", {"reason": "Bu sertifikat sizniki emas."}, status=403)
        return render(request, "progress/certificate_detail.html", {"cert": cert})


class ClaimModuleCertificateView(RoleRequiredMixin, View):
    allowed_roles = ("student",)

    def post(self, request, module_id):
        module = get_object_or_404(Module.objects.select_related("course"), pk=module_id)
        status = module_completion(request.user, module)
        if not status["ready"]:
            messages.error(
                request,
                t("Modul hali tugallanmagan. Barcha darslar, mashqlar va bilim testini yakunlang."),
            )
            return redirect("courses:detail", slug=module.course.slug)
        cert = issue_module_certificate(request.user, module)
        messages.success(request, t("Sertifikat tayyor!"))
        return redirect("progress:certificate_detail", code=cert.code)


class ClaimCourseCertificateView(RoleRequiredMixin, View):
    allowed_roles = ("student",)

    def post(self, request, course_id):
        course = get_object_or_404(Course, pk=course_id)
        cert = issue_course_certificate(request.user, course)
        if not cert:
            messages.error(request, t("Kurs hali to‘liq tugallanmagan."))
            return redirect("courses:detail", slug=course.slug)
        messages.success(request, t("Kurs sertifikati tayyor!"))
        return redirect("progress:certificate_detail", code=cert.code)
