"""
This models file contains all the models used for project_catalog apps.
"""
import uuid
from email.policy import default
from statistics import mode

from authentication.models import User
from django.conf import settings
from django.db import models


# pylint: disable=too-few-public-methods
class Rating(models.Model):
    """
    Rating model for storing rating of the project list
    """

    id = models.AutoField(primary_key=True)
    emoji = models.TextField(max_length=2048, blank=True)
    is_deleted = models.BooleanField(default=False, null=True, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="rcreator",
    )
    updated_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(auto_now_add=True)
    deleted_by = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True, related_name="rdeleter"
    )

    def __str__(self):
        return str(self.emoji)


def get_image_filepath(instance, filename):
    """Generate image path for the file

    Args:
        filename (str): file name of the image

    Returns:
        str: path of the image
    """
    filename = filename + uuid.uuid4().hex[:10]
    return f"images/{filename}.png"


# pylint: disable=too-few-public-methods
class Image(models.Model):
    """Image model for storing images

    returns:
        Image object
    """

    id = models.AutoField(primary_key=True)
    image = models.ImageField(
        max_length=255, upload_to=get_image_filepath, null=True, blank=True
    )
    is_deleted = models.BooleanField(default=False, null=True, blank=False)
    updated_at = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="icreator",
    )
    deleted_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="ideleter",
    )
    deleted_at = models.DateTimeField(auto_now_add=True)


class Project(models.Model):
    """Project model class for project table.

    return:
        Project object
    """

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True
    )
    title = models.CharField(max_length=200, blank=True)
    description = models.TextField(max_length=2048, blank=True)
    project_link = models.URLField(max_length=200)
    github_link = models.URLField(max_length=200)

    is_deleted = models.BooleanField(default=False, null=True, blank=False)
    is_approved = models.BooleanField(default=False, null=True, blank=False)
    updated_at = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="pcreator",
    )
    deleted_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="pdeleter",
    )
    deleted_at = models.DateTimeField(auto_now_add=True)
    approved_at = models.DateTimeField(auto_now_add=True)
    approved_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="papprover",
    )
    rating = models.ManyToManyField(Rating, blank=True, related_name="ratingss")
    images = models.ManyToManyField(Image, blank=True, related_name="imagep")
    posted_on_tg = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    
    @property
    def get_cover_image(self):
        """Get the cover image of the project.

        Returns:
            Image: cover image of the project
        """
        return self.images.first() if self.images.exists() else None
    
    @property
    def get_short_description(self):
        """Get the short description of the project.

        Returns:
            str: short description of the project
        """
        return self.description[:100] if self.description else None
    
    @property
    def get_human_redable_date(self):
        """Get the human readable date of the project.

        Returns:
            str: human readable date of the project
        """
        return self.created_at.strftime("%d %b %Y")


class Event(models.Model):
    """Event model class for event table.
    return:
        Event object
    """

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True
    )
    description = models.TextField(max_length=200, blank=True)
    is_read = models.BooleanField(default=False, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user
