from django.urls import path

from . import views

urlpatterns = [
    path("", views.DashboardView.as_view(), name="dashboard-index"),
    path("projects/", views.project_list, name="project-list"),
    path("projects/my", views.MyProjectListView.as_view(), name="my-project-list"),
    path("projects/<int:id>", views.project_list, name="project-detail"),
    path("create/", views.create_project, name="create-project"),
    path("edit/<str:pk>/", views.edit_project, name="edit-project"),
    path("delete/<str:pk>/", views.delete_project, name="delete-project"),
]
