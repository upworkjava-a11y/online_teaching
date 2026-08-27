from django.urls import path

from .views import ExerciseDetailView, PracticeCatalogView, SkillTestListView

app_name = "exercises"

urlpatterns = [
    path("", PracticeCatalogView.as_view(), name="catalog"),
    path("bilim-testi/<int:module_id>/", SkillTestListView.as_view(), name="skill_tests"),
    path("<int:pk>/", ExerciseDetailView.as_view(), name="detail"),
]
