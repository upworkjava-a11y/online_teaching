from django.contrib import admin

from .models import Contest, ContestExercise, ContestScore


class ContestExerciseInline(admin.TabularInline):
    model = ContestExercise
    extra = 0
    autocomplete_fields = ("exercise",)


@admin.register(Contest)
class ContestAdmin(admin.ModelAdmin):
    list_display = ("title", "starts_at", "ends_at", "is_published")
    list_filter = ("is_published",)
    search_fields = ("title", "slug")
    prepopulated_fields = {"slug": ("title",)}
    inlines = [ContestExerciseInline]


@admin.register(ContestScore)
class ContestScoreAdmin(admin.ModelAdmin):
    list_display = ("contest", "student", "points", "solved_count", "last_solved_at")
    list_filter = ("contest",)
    search_fields = ("student__email", "student__first_name")
    autocomplete_fields = ("contest", "student")
