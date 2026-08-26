from django.urls import path

from .views import (
    HomeworkDeleteView,
    HomeworkDownloadView,
    HomeworkListView,
    HomeworkSubmitView,
)

app_name = "homework"

urlpatterns = [
    path("", HomeworkListView.as_view(), name="list"),
    path("<int:pk>/submit/", HomeworkSubmitView.as_view(), name="submit"),
    path("submissions/<int:pk>/download/", HomeworkDownloadView.as_view(), name="download"),
    path("submissions/<int:pk>/delete/", HomeworkDeleteView.as_view(), name="delete"),
]
