from django.urls import path

from . import views

urlpatterns = [
    path("", views.CompaniesListView.as_view(), name="companies-list"),
    path("<int:pk>/", views.CompanyDetailView.as_view(), name="company-detail"),
    path("<int:pk>/delete/", views.CompanyDeleteView.as_view(), name="company-delete"),
    path("create/", views.CreateView.as_view(), name="company-create"),
]
