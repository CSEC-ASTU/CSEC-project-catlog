from django.contrib import admin

from .models import Project, Image

admin.site.register(Image)
admin.site.register(Project)
