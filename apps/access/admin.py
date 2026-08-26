from django.contrib import admin

from .models import UserContentAccess


@admin.register(UserContentAccess)
class UserContentAccessAdmin(admin.ModelAdmin):
    list_display = ("user", "content_type", "object_id", "status", "created_by", "updated_at")
    list_filter = ("status", "content_type")
    search_fields = ("user__email", "user__first_name", "user__last_name", "reason")
    autocomplete_fields = ("user", "created_by")
    readonly_fields = ("created_at", "updated_at")
