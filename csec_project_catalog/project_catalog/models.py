# pylint: disable=too-few-public-methods
from uuid import uuid4

from authentication.models import User
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models


class Rating(models.Model):
    """Model for Rating

    this model is used to store the rating of a project
    """

    id = models.AutoField(primary_key=True)
    emoji = models.TextField(max_length=2048, blank=False, null=False)
    is_deleted = models.BooleanField(default=False, null=True, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="r_creator",
    )
    updated_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(auto_now_add=True)
    deleted_by = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True, related_name="r_deleter"
    )

    def __str__(self) -> str:
        return self.emoji


def get_image_filepath(self, filename):
    """Method for getting image file path

    Args:
        filename (str): the image file name

    Returns:
        str: address for the image to be saved in the direcotry
    """
    filename = f"{uuid4()}-{filename}"
    return "images/" + str(self.pk) + "/{filename}"


class Image(models.Model):
    """Model for Image Object

    this models is used to save the image uploaded by the user
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
        related_name="i_creator",
    )
    deleted_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="i_deleter",
    )
    deleted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.image.url


class Project(models.Model):
    """Model for Project object

    this model is used to store the project details
    """

    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True
    )
    title = models.TextField(max_length=200, blank=True)
    description = models.TextField(max_length=2048, blank=True)
    project_link = models.URLField(max_length=200)
    github_link = models.URLField(max_length=200)
    is_deleted = models.BooleanField(default=False, null=True, blank=False)
    updated_at = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="p_creator",
    )
    deleted_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="p_deleter",
    )
    deleted_at = models.DateTimeField(auto_now_add=True)
    approved_at = models.DateTimeField(auto_now_add=True)
    approved_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="p_approver",
    )
    approved_status = models.BooleanField(default=False)
    rating = models.ManyToManyField(Rating, blank=True, related_name="p_ratingss")
    images = models.ManyToManyField(Image, blank=True, related_name="p_image")

    def __str__(self) -> str:
        return self.title
