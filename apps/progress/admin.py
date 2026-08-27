from django.contrib import admin

from .models import Certificate, CourseProgress, LectureProgress, StudentStreak


@admin.register(LectureProgress)
class LectureProgressAdmin(admin.ModelAdmin):
    list_display = ("student", "lecture", "completed", "completed_at", "last_viewed_at")
    list_filter = ("completed", "lecture__module__course")
    search_fields = ("student__email", "student__first_name", "lecture__title")
    autocomplete_fields = ("student", "lecture")
    readonly_fields = ("created_at", "updated_at")


@admin.register(CourseProgress)
class CourseProgressAdmin(admin.ModelAdmin):
    list_display = ("student", "course", "last_lecture", "last_activity_at")
    list_filter = ("course",)
    search_fields = ("student__email", "student__first_name")
    autocomplete_fields = ("student", "course", "last_lecture")
    readonly_fields = ("created_at", "updated_at")


@admin.register(StudentStreak)
class StudentStreakAdmin(admin.ModelAdmin):
    list_display = ("student", "current_streak", "longest_streak", "last_solved_date")
    search_fields = ("student__email", "student__first_name")
    autocomplete_fields = ("student",)


@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = ("code", "title", "student", "kind", "issued_at")
    list_filter = ("kind",)
    search_fields = ("code", "title", "student__email")
    autocomplete_fields = ("student", "module", "course")
    readonly_fields = ("code", "issued_at", "created_at", "updated_at")
