from django.contrib import admin

from .models import Project, Image, Event

admin.site.register(Image)
admin.site.register(Project)
admin.site.register(Event)
