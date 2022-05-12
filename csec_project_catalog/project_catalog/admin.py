from django.contrib import admin

from .models import Event, Image, Project, Rating

admin.site.register(Image)
admin.site.register(Project)
admin.site.register(Event)
admin.site.register(Rating)
