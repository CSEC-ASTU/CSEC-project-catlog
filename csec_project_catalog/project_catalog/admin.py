from django.contrib import admin

from .models import Project, Event


class EventAdmin(admin.ModelAdmin):
    fields = ("user", "description")


admin.site.register(Event, EventAdmin)


class ProjectAdmin(admin.ModelAdmin):
    fields = (
        "user",
        "title",
        "description",
        "project_link",
        "github_link",
        "approved_status",
    )
    list_display = (
        "user",
        "title",
        "description",
        "project_link",
        "github_link",
        "approved_status",
    )
    list_filter = ("approved_status",)
    ordering = ("-created_at",)
admin.site.register(Project, ProjectAdmin)
