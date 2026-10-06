from django.contrib import admin

from .models import Block, Conversation, ConversationParticipant, Follow, Message, SocialProfile, UserActivity


@admin.register(SocialProfile)
class SocialProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "avatar_preset", "has_upload", "updated_at")
    search_fields = ("user__username", "user__email", "user__first_name")
    raw_id_fields = ("user",)

    @admin.display(boolean=True, description="Upload")
    def has_upload(self, obj):
        return bool(obj.avatar_image)


class MessageInline(admin.TabularInline):
    model = Message
    extra = 0
    raw_id_fields = ("sender",)
    readonly_fields = ("sender", "text", "created_at", "read_at")
    can_delete = False
    max_num = 20

    def has_add_permission(self, request, obj=None):
        return False


class ParticipantInline(admin.TabularInline):
    model = ConversationParticipant
    extra = 0
    raw_id_fields = ("user",)
    readonly_fields = ("user", "last_read_at", "joined_at")


@admin.register(Conversation)
class ConversationAdmin(admin.ModelAdmin):
    list_display = ("id", "pair_key", "updated_at", "created_at")
    search_fields = ("pair_key",)
    inlines = [ParticipantInline, MessageInline]


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ("id", "conversation", "sender", "short_text", "created_at", "read_at")
    list_filter = ("created_at",)
    search_fields = ("sender__username", "sender__email", "text")
    raw_id_fields = ("conversation", "sender")
    readonly_fields = ("created_at",)

    @admin.display(description="Text")
    def short_text(self, obj):
        t = obj.text or ""
        return t if len(t) <= 60 else t[:57] + "…"


@admin.register(Follow)
class FollowAdmin(admin.ModelAdmin):
    list_display = ("follower", "following", "created_at")
    search_fields = ("follower__username", "following__username")
    raw_id_fields = ("follower", "following")


@admin.register(Block)
class BlockAdmin(admin.ModelAdmin):
    list_display = ("blocker", "blocked", "created_at")
    search_fields = ("blocker__username", "blocked__username")
    raw_id_fields = ("blocker", "blocked")


@admin.register(UserActivity)
class UserActivityAdmin(admin.ModelAdmin):
    list_display = ("user", "date", "activity_type", "count")
    list_filter = ("activity_type", "date")
    search_fields = ("user__username", "user__email")
    raw_id_fields = ("user",)
