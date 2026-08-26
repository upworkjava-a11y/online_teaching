from django.urls import path

from .views import (
    TeacherAnalyticsView,
    TeacherDashboardView,
    TeacherHomeworkListView,
    TeacherHomeworkReviewView,
    TeacherStudentDetailView,
    TeacherStudentListView,
)

app_name = "analytics"

urlpatterns = [
    path("", TeacherDashboardView.as_view(), name="dashboard"),
    path("students/", TeacherStudentListView.as_view(), name="students"),
    path("students/<int:pk>/", TeacherStudentDetailView.as_view(), name="student_detail"),
    path("homework/", TeacherHomeworkListView.as_view(), name="homework"),
    path("homework/<int:pk>/", TeacherHomeworkReviewView.as_view(), name="homework_review"),
    path("insights/", TeacherAnalyticsView.as_view(), name="insights"),
]
