from django.contrib import admin

from .models import Course, CourseEnrollment, Lecture, Module


class ModuleInline(admin.TabularInline):
    model = Module
    extra = 0
    fields = ("title", "slug", "order", "is_published")
    show_change_link = True


class LectureInline(admin.TabularInline):
    model = Lecture
    extra = 0
    fields = ("title", "slug", "order", "is_published")
    show_change_link = True


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "premium_price", "order", "is_published", "is_visible")
    list_filter = ("is_published", "is_visible")
    search_fields = ("title", "slug", "description")
    list_editable = ("premium_price", "order", "is_published", "is_visible")
    prepopulated_fields = {"slug": ("title",)}
    fieldsets = (
        (None, {"fields": ("title", "slug", "description", "order")}),
        (
            "Premium narx",
            {
                "fields": ("premium_price",),
                "description": "Talabaga ko‘rsatiladigan to‘lov summasi (so‘m).",
            },
        ),
        ("Holat", {"fields": ("is_published", "is_visible")}),
    )
    inlines = [ModuleInline]


@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):
    list_display = ("title", "course", "order", "is_published")
    list_filter = ("is_published", "course")
    search_fields = ("title", "slug", "description")
    list_editable = ("order", "is_published")
    autocomplete_fields = ("course",)
    prepopulated_fields = {"slug": ("title",)}
    inlines = [LectureInline]


@admin.register(Lecture)
class LectureAdmin(admin.ModelAdmin):
    list_display = ("title", "module", "order", "is_published")
    list_filter = ("is_published", "module__course", "module")
    search_fields = ("title", "slug", "content")
    list_editable = ("order", "is_published")
    autocomplete_fields = ("module",)
    prepopulated_fields = {"slug": ("title",)}
    fieldsets = (
        (None, {"fields": ("module", "title", "slug", "order", "is_published")}),
        ("Mazmun", {"fields": ("content", "sql_examples")}),
    )


@admin.register(CourseEnrollment)
class CourseEnrollmentAdmin(admin.ModelAdmin):
    list_display = ("student", "course", "created_at")
    list_filter = ("course",)
    search_fields = ("student__email", "student__first_name", "student__last_name")
    autocomplete_fields = ("student", "course")
