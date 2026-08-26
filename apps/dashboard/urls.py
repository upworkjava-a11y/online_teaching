from django.urls import path

from .views import StudentDashboardView, StudentProgressView

app_name = "dashboard"

urlpatterns = [
    path("", StudentDashboardView.as_view(), name="home"),
    path("progress/", StudentProgressView.as_view(), name="progress"),
]
