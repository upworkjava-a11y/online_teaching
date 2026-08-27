from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from django.contrib.auth.forms import UserCreationForm

from .models import GoogleAccount, StudentProfile, TeacherProfile, User, TelegramAccount, Announcement, DirectMessage, SupportTicket


class PlatformUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("email", "username", "first_name", "last_name", "role", "is_premium")


@admin.register(User)
class UserAdmin(DjangoUserAdmin):
    add_form = PlatformUserCreationForm
    list_display = ("email", "first_name", "last_name", "role", "is_premium", "is_active", "is_blocked", "last_activity_at")
    list_filter = ("role", "is_premium", "is_active", "is_blocked", "is_staff")
    search_fields = ("email", "first_name", "last_name", "username")
    ordering = ("email",)
    filter_horizontal = ("groups", "user_permissions")
    autocomplete_fields = ()
    fieldsets = (
        (None, {"fields": ("email", "username", "password")}),
        ("Shaxsiy ma’lumot", {"fields": ("first_name", "last_name")}),
        ("Rol va holat", {
            "fields": ("role", "is_premium", "is_active", "is_blocked", "is_staff", "is_superuser"),
            "description": (
                "is_premium = barcha kurslar (VIP). "
                "Oddiy to‘lov: Access → «To‘lov: kursni ochish» — faqat tanlangan kurs."
            ),
        }),
        ("Guruhlar", {"fields": ("groups",), "description": "Premium guruh = barcha kurslar. Bitta kurs uchun Access ishlating."}),
        ("Ruxsatlar", {"fields": ("user_permissions",)}),
        ("Sanalar", {"fields": ("last_login", "last_activity_at", "date_joined")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "username",
                    "first_name",
                    "last_name",
                    "role",
                    "is_premium",
                    "password1",
                    "password2",
                ),
            },
        ),
    )
    readonly_fields = ("last_login", "last_activity_at", "date_joined")

    def get_changeform_initial_data(self, request):
        return {"is_premium": False}


@admin.register(StudentProfile)
class StudentProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "created_at")
    search_fields = ("user__email", "user__first_name", "user__last_name")
    autocomplete_fields = ("user",)


@admin.register(TeacherProfile)
class TeacherProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "created_at")
    search_fields = ("user__email", "user__first_name", "user__last_name")
    autocomplete_fields = ("user",)
    filter_horizontal = ("assigned_courses",)


@admin.register(GoogleAccount)
class GoogleAccountAdmin(admin.ModelAdmin):
    list_display = ("email", "user", "google_sub", "created_at")
    search_fields = ("email", "google_sub", "user__email", "user__first_name", "user__last_name")
    autocomplete_fields = ("user",)
    readonly_fields = ("google_sub", "email", "created_at", "updated_at")


@admin.register(TelegramAccount)
class TelegramAccountAdmin(admin.ModelAdmin):
    list_display = ("telegram_id", "user", "telegram_username", "notify_enabled", "created_at")
    search_fields = ("telegram_username", "user__email", "user__first_name")
    autocomplete_fields = ("user",)


@admin.register(Announcement)
class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "is_published", "created_at")
    list_filter = ("is_published",)
    search_fields = ("title", "body")
    autocomplete_fields = ("author",)


@admin.register(DirectMessage)
class DirectMessageAdmin(admin.ModelAdmin):
    list_display = ("sender", "recipient", "created_at", "read_at")
    search_fields = ("body", "sender__email", "recipient__email")
    autocomplete_fields = ("sender", "recipient")


@admin.register(SupportTicket)
class SupportTicketAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "is_resolved", "created_at")
    list_filter = ("is_resolved",)
    search_fields = ("message", "reply", "user__email")
    autocomplete_fields = ("user",)
