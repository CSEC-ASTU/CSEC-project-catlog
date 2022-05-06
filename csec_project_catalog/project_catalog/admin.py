from django.contrib import admin

from .models import Event, Project

admin.site.register(Project)
admin.site.register(Event)
