"""
    csec_project_catalog URL Configuration

"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView

urlpatterns = [
    path("", TemplateView.as_view(template_name="index.html"), name="index"),
    path("admin/", admin.site.urls),
    path("auth/", include("authentication.urls"), name="authentication"),
    path("project/", include("project_catalog.urls"), name="project"),
    path("companies/", include("companies.urls"), name="companies"),
]

# For Development only
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = "csec_project_catalog.views.error_404"
