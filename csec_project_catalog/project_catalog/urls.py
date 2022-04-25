from django.urls import path

from . import views

urlpatterns = [
    path("", views.project_list, name="project-list"),
    path("create/", views.create_project, name="create-project"),
    path("edit/<str:pk>/", views.edit_project, name="edit-project"),
    path("delete/<str:pk>/", views.delete_project, name="delete-project"),

    path("", views.event_list, name="event-list"),
    path("event/create/", views.create_event, name="create-event"),
    path("event/edit/<str:pk>/", views.edit_event, name="edit-event"),
    path("event/delete/<str:pk>/", views.delete_event , name="delete-event"),

]
