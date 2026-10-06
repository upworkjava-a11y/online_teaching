from django.urls import path
from django.views.generic import RedirectView

from . import views

app_name = "social"

urlpatterns = [
    # Canonical unified profile
    path("profile/", views.OwnProfileRedirectView.as_view(), name="own_profile"),
    path("profile/edit/", views.ProfileSettingsView.as_view(), name="settings"),
    path("profile/<str:username>/", views.PublicProfileView.as_view(), name="profile"),
    path("profile/<str:username>/follow/", views.FollowToggleView.as_view(), name="follow"),
    path("profile/<str:username>/block/", views.BlockToggleView.as_view(), name="block"),
    path("profile/<str:username>/message/", views.StartChatView.as_view(), name="start_chat"),
    path("profile/<str:username>/followers/", views.FollowersListView.as_view(), name="followers"),
    path(
        "profile/<str:username>/activity/month/",
        views.ActivityMonthView.as_view(),
        name="activity_month",
    ),
    path(
        "profile/<str:username>/activity/day/",
        views.ActivityDayView.as_view(),
        name="activity_day",
    ),
    path("profile/<str:username>/presence/", views.PresenceStatusView.as_view(), name="presence"),
    # Chat (unchanged)
    path("messages/", views.ConversationListView.as_view(), name="inbox"),
    path("messages/<int:pk>/", views.ConversationDetailView.as_view(), name="chat_detail"),
    path("messages/<int:pk>/history/", views.ChatHistoryView.as_view(), name="chat_history"),
    path("presence/heartbeat/", views.HeartbeatView.as_view(), name="heartbeat"),
    # Legacy redirects → canonical /profile/
    path(
        "users/<str:username>/",
        RedirectView.as_view(pattern_name="social:profile", permanent=False),
        name="legacy_profile",
    ),
    path(
        "users/<str:username>/follow/",
        RedirectView.as_view(pattern_name="social:follow", permanent=False),
    ),
    path(
        "users/<str:username>/block/",
        RedirectView.as_view(pattern_name="social:block", permanent=False),
    ),
    path(
        "users/<str:username>/message/",
        RedirectView.as_view(pattern_name="social:start_chat", permanent=False),
    ),
    path(
        "users/<str:username>/followers/",
        RedirectView.as_view(pattern_name="social:followers", permanent=False),
    ),
    path(
        "users/<str:username>/activity/month/",
        RedirectView.as_view(pattern_name="social:activity_month", permanent=False),
    ),
    path(
        "users/<str:username>/activity/day/",
        RedirectView.as_view(pattern_name="social:activity_day", permanent=False),
    ),
    path(
        "users/<str:username>/presence/",
        RedirectView.as_view(pattern_name="social:presence", permanent=False),
    ),
    path(
        "me/social/",
        RedirectView.as_view(pattern_name="social:settings", permanent=False),
        name="legacy_settings",
    ),
]
