"""
    csec_project_catalog URL Configuration

"""
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("auth/", include("authentication.urls"), name="authentication"),
    path("project/", include("project_catalog.urls"), name="project"),
    path("companies/", include("companies.urls"), name="companies"),
]
