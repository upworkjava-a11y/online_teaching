from django.urls import path

from .views import CompleteLectureView, LectureDetailView

app_name = "learning"

urlpatterns = [
    path("<int:pk>/", LectureDetailView.as_view(), name="lecture"),
    path("<int:pk>/complete/", CompleteLectureView.as_view(), name="complete"),
]
