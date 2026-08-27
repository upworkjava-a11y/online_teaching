from django.urls import path

from .views import CourseDetailView, CourseListView, CoursePremiumOfferView

app_name = "courses"

urlpatterns = [
    path("", CourseListView.as_view(), name="list"),
    path("<slug:slug>/premium/", CoursePremiumOfferView.as_view(), name="premium"),
    path("<slug:slug>/", CourseDetailView.as_view(), name="detail"),
]
