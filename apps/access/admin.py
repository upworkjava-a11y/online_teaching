from django import forms
from django.contrib import admin, messages
from django.shortcuts import redirect, render
from django.urls import path

from apps.accounts.models import User
from apps.courses.models import Course

from .models import UserContentAccess
from .services import access_service


class GrantCoursePremiumForm(forms.Form):
    """To‘lovdan keyin faqat tanlangan kursni ochish."""

    user = forms.ModelChoiceField(
        queryset=User.objects.filter(role=User.Role.STUDENT, is_active=True).order_by("email"),
        label="Talaba",
        help_text="To‘lov qilgan talaba (email).",
    )
    course = forms.ModelChoiceField(
        queryset=Course.objects.filter(is_published=True).order_by("order", "title"),
        label="Kurs",
        help_text="Qaysi kurs uchun to‘lov qilindi — faqat shu kurs ochiladi.",
    )
    reason = forms.CharField(
        required=False,
        label="Izoh",
        widget=forms.TextInput(attrs={"placeholder": "Masalan: chek @just_585, 50 000 so‘m"}),
    )


@admin.register(UserContentAccess)
class UserContentAccessAdmin(admin.ModelAdmin):
    list_display = ("user", "course_or_object", "status", "reason_short", "created_by", "updated_at")
    list_filter = ("status", "content_type")
    search_fields = ("user__email", "user__first_name", "user__last_name", "reason")
    autocomplete_fields = ("user", "created_by")
    readonly_fields = ("created_at", "updated_at")
    change_list_template = "admin/access/usercontentaccess/change_list.html"

    def course_or_object(self, obj):
        target = obj.content_object
        if target is None:
            return f"#{obj.object_id}"
        if isinstance(target, Course):
            return f"Kurs: {target.title}"
        return str(target)

    course_or_object.short_description = "Kontent"

    def reason_short(self, obj):
        return (obj.reason or "")[:60]

    reason_short.short_description = "Izoh"

    def get_urls(self):
        urls = super().get_urls()
        custom = [
            path(
                "grant-course/",
                self.admin_site.admin_view(self.grant_course_view),
                name="access_usercontentaccess_grant_course",
            ),
        ]
        return custom + urls

    def grant_course_view(self, request):
        if not request.user.is_staff:
            messages.error(request, "Ruxsat yo‘q.")
            return redirect("admin:index")
        form = GrantCoursePremiumForm(request.POST or None)
        if request.method == "POST" and form.is_valid():
            user = form.cleaned_data["user"]
            course = form.cleaned_data["course"]
            reason = form.cleaned_data["reason"]
            access_service.grant_course_access(
                user,
                course,
                created_by=request.user,
                reason=reason or f"To‘lov: {course.title}",
            )
            messages.success(
                request,
                f"Ochildi: {user.get_full_name() or user.email} → {course.title} (faqat shu kurs).",
            )
            return redirect("admin:access_usercontentaccess_changelist")
        context = {
            **self.admin_site.each_context(request),
            "title": "To‘lov bo‘yicha kursni ochish",
            "form": form,
            "opts": self.model._meta,
        }
        return render(request, "admin/access/grant_course_premium.html", context)
