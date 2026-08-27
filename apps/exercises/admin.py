from django.contrib import admin

from .models import Dataset, Exercise, ExerciseAttempt, ExerciseComment, ExerciseDataset, ExerciseExpectedResult


class ExerciseDatasetInline(admin.TabularInline):
    model = ExerciseDataset
    extra = 0
    autocomplete_fields = ("dataset",)


class ExerciseExpectedResultInline(admin.StackedInline):
    model = ExerciseExpectedResult
    extra = 0


@admin.register(Dataset)
class DatasetAdmin(admin.ModelAdmin):
    list_display = ("name", "updated_at")
    search_fields = ("name", "description")


@admin.register(Exercise)
class ExerciseAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "module",
        "kind",
        "difficulty",
        "is_skill_test",
        "lecture",
        "order",
        "is_published",
        "max_score",
    )
    list_filter = ("is_published", "kind", "difficulty", "is_skill_test", "module__course", "module")
    search_fields = ("title", "task", "description")
    autocomplete_fields = ("module", "lecture")
    list_editable = ("order", "is_published", "difficulty", "is_skill_test")
    inlines = [ExerciseDatasetInline, ExerciseExpectedResultInline]
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "module",
                    "lecture",
                    "title",
                    "slug",
                    "kind",
                    "difficulty",
                    "is_skill_test",
                    "order",
                    "is_published",
                    "max_score",
                )
            },
        ),
        ("Mazmun", {"fields": ("description", "task", "hints", "editorial", "quiz_options")}),
        ("Tekshiruv", {"fields": ("require_row_order", "require_column_order")}),
    )


@admin.register(ExerciseAttempt)
class ExerciseAttemptAdmin(admin.ModelAdmin):
    list_display = ("student", "exercise", "is_correct", "score", "created_at")
    list_filter = ("is_correct", "exercise__module__course")
    search_fields = ("student__email", "student__first_name", "exercise__title")
    autocomplete_fields = ("student", "exercise")
    readonly_fields = ("sql_query", "result_preview", "error_message", "execution_ms", "created_at", "updated_at")


@admin.register(ExerciseComment)
class ExerciseCommentAdmin(admin.ModelAdmin):
    list_display = ("exercise", "author", "is_hidden", "created_at")
    list_filter = ("is_hidden",)
    search_fields = ("body", "author__email", "exercise__title")
    autocomplete_fields = ("exercise", "author")
