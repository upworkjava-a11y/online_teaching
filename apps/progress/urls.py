from django.urls import path

from .views import (
    CertificateDetailView,
    CertificateListView,
    ClaimCourseCertificateView,
    ClaimModuleCertificateView,
)

app_name = "progress"

urlpatterns = [
    path("sertifikatlar/", CertificateListView.as_view(), name="certificates"),
    path("sertifikat/<str:code>/", CertificateDetailView.as_view(), name="certificate_detail"),
    path("sertifikat/modul/<int:module_id>/olish/", ClaimModuleCertificateView.as_view(), name="claim_module"),
    path("sertifikat/kurs/<int:course_id>/olish/", ClaimCourseCertificateView.as_view(), name="claim_course"),
]
