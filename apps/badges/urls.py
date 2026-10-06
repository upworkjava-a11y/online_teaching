from django.urls import path

from . import views

app_name = "badges"

urlpatterns = [
    path("users/<str:username>/achievements/", views.AchievementsView.as_view(), name="achievements"),
    path(
        "users/<str:username>/achievements/<slug:slug>/",
        views.BadgeDetailPartialView.as_view(),
        name="badge_detail",
    ),
    path("badges/toasts/", views.BadgeToastPopView.as_view(), name="toasts"),
]
