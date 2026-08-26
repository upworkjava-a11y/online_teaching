from django.urls import path

from .views import StudentDashboardView, StudentLeaderboardView, StudentProgressView

app_name = "dashboard"

urlpatterns = [
    path("", StudentDashboardView.as_view(), name="home"),
    path("progress/", StudentProgressView.as_view(), name="progress"),
    path("leaderboard/", StudentLeaderboardView.as_view(), name="leaderboard"),
]
