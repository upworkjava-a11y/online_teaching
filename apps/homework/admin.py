from django.contrib import admin

from .models import HomeworkAssignment, HomeworkReview, HomeworkSubmission, NotificationHook


class HomeworkReviewInline(admin.StackedInline):
    model = HomeworkReview
    extra = 0
    autocomplete_fields = ("reviewer",)
    readonly_fields = ("created_at", "updated_at")


@admin.register(HomeworkAssignment)
class HomeworkAssignmentAdmin(admin.ModelAdmin):
    list_display = ("title", "lecture", "max_score", "is_published")
    list_filter = ("is_published", "lecture__module__course")
    search_fields = ("title", "instructions")
    autocomplete_fields = ("lecture",)


@admin.register(HomeworkSubmission)
class HomeworkSubmissionAdmin(admin.ModelAdmin):
    list_display = ("student", "assignment", "status", "original_filename", "created_at")
    list_filter = ("status", "assignment__lecture__module__course")
    search_fields = ("student__email", "student__first_name", "assignment__title", "original_filename")
    autocomplete_fields = ("student", "assignment")
    readonly_fields = ("original_filename", "created_at", "updated_at")
    inlines = [HomeworkReviewInline]


@admin.register(HomeworkReview)
class HomeworkReviewAdmin(admin.ModelAdmin):
    list_display = ("submission", "reviewer", "score", "status", "created_at")
    list_filter = ("status",)
    search_fields = ("submission__student__email", "feedback")
    autocomplete_fields = ("submission", "reviewer")


@admin.register(NotificationHook)
class NotificationHookAdmin(admin.ModelAdmin):
    list_display = ("event", "processed", "created_at")
    list_filter = ("event", "processed")
    readonly_fields = ("event", "payload", "created_at", "updated_at")
