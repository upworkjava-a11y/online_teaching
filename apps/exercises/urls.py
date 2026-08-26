from django.urls import path

from .views import ExerciseDetailView

app_name = "exercises"

urlpatterns = [
    path("<int:pk>/", ExerciseDetailView.as_view(), name="detail"),
]
