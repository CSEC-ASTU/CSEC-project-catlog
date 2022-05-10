from django.urls import path

from . import views

urlpatterns = [
    path("", views.DashboardView.as_view(), name="dashboard-index"),
    path("projects/", views.project_list, name="project-list"),
    path("projects/my", views.MyProjectListView.as_view(), name="my-project-list"),
    path("projects/<int:pk>", views.ProjectDetails.as_view(), name="project-details"),
    path("projects/<int:pk>/delete", views.DeleteProject.as_view(), name="project-delete"),
    path("create/", views.create_project, name="create-project"),
    # path("edit/<str:pk>/", views.edit_project, name="edit-project"),
    path("events", views.event_list, name="event-list"),
    path("event/create/", views.create_event, name="create-event"),
    path("event/edit/<str:pk>/", views.edit_event, name="edit-event"),
    path("event/delete/<str:pk>/", views.delete_event, name="delete-event"),
]
