from django.urls import path

from . import views

urlpatterns = [
    path("", views.DashboardView.as_view(), name="dashboard-index"),
    path("projects/", views.ProjectListView.as_view(), name="project-list"),
    path("admin-projects/", views.AdminProjectView.as_view(), name="admin-projects"),
    path("projects/create", views.CreateProjectView.as_view(), name="project-create"),
    path("projects/my", views.MyProjectListView.as_view(), name="my-project-list"),
    path(
        "projects/image/create",
        views.ProjectImageUpload.as_view(),
        name="project-image",
    ),
    path("projects/<int:pk>", views.ProjectDetails.as_view(), name="project-details"),
    path(
        "projects/<int:pk>/delete", views.DeleteProject.as_view(), name="project-delete"
    ),
    path("projects/<int:pk>/rate", views.ProjectRating.as_view(), name="project-rate"),
    # path("edit/<str:pk>/", views.edit_project, name="edit-project"),
    path("events", views.event_list, name="event-list"),
    path("event/create/", views.create_event, name="create-event"),
    path("event/edit/<str:pk>/", views.edit_event, name="edit-event"),
    path("event/delete/<str:pk>/", views.delete_event, name="delete-event"),
]
