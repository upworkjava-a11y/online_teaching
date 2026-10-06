from django.contrib import admin

from .models import Badge, UserBadge, UserRankPeak


@admin.register(Badge)
class BadgeAdmin(admin.ModelAdmin):
    list_display = ("sort_order", "name", "slug", "category", "rarity", "icon_path", "requirement_type", "requirement_value", "is_active")
    list_filter = ("category", "rarity", "requirement_type", "is_active")
    search_fields = ("name", "slug", "description")
    list_editable = ("is_active",)
    ordering = ("sort_order",)


@admin.register(UserBadge)
class UserBadgeAdmin(admin.ModelAdmin):
    list_display = ("user", "badge", "earned_at")
    list_filter = ("badge__category", "badge")
    search_fields = ("user__username", "user__email", "badge__slug")
    raw_id_fields = ("user", "badge")
    readonly_fields = ("earned_at",)


@admin.register(UserRankPeak)
class UserRankPeakAdmin(admin.ModelAdmin):
    list_display = ("user", "best_rank", "achieved_at")
    search_fields = ("user__username", "user__email")
    raw_id_fields = ("user",)
