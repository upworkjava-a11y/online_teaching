from django.urls import path

from .views import CompleteLectureView, LectureDetailView, RunPythonLectureView

app_name = "learning"

urlpatterns = [
    path("<int:pk>/", LectureDetailView.as_view(), name="lecture"),
    path("<int:pk>/complete/", CompleteLectureView.as_view(), name="complete"),
    path("<int:pk>/run-python/", RunPythonLectureView.as_view(), name="run_python"),
]
