from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from apps.core.i18n.views import SetLanguageView
from apps.core.views import HealthCheckView, RootRedirectView

admin.site.site_header = "Data Analytics ta'lim platformasi"
admin.site.site_title = "Admin"
admin.site.index_title = "Boshqaruv paneli"

urlpatterns = [
    path("", RootRedirectView.as_view(), name="root"),
    path("health/", HealthCheckView.as_view(), name="health"),
    path("i18n/setlang/", SetLanguageView.as_view(), name="set_language"),
    path("admin/", admin.site.urls),
    path("accounts/", include("apps.accounts.urls")),
    path("dashboard/", include("apps.dashboard.urls")),
    path("courses/", include("apps.courses.urls")),
    path("learn/", include("apps.learning.urls")),
    path("exercises/", include("apps.exercises.urls")),
    path("homework/", include("apps.homework.urls")),
    path("teacher/", include("apps.analytics.urls")),
    path("musobaqalar/", include("apps.contests.urls")),
    path("progress/", include("apps.progress.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
elif getattr(settings, "SERVE_MEDIA", False):
    # PythonAnywhere: map /media/ in the Web tab, or let Django serve small homework files
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
