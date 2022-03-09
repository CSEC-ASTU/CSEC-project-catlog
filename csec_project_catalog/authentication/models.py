from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField


class Link(models.Model):
    url = models.URLField(max_length=200)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    deleted_by = models.ForeignKey(
        'User', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.url[:50]


class User(AbstractUser):
    """User model that extends the default django user and add
    additional information's.
    """
    phone_number = PhoneNumberField()
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    deleted_by = models.ForeignKey(
        'self', on_delete=models.SET_NULL, null=True, blank=True)
    approved_by = models.ForeignKey(
        'self', on_delete=models.SET_NULL, null=True, blank=True)
    approved_at = models.DateTimeField(null=True, blank=True)
    approved_status = models.BooleanField(default=False)
    last_login_ip = models.GenericIPAddressField(null=True, blank=True)
    links = models.ManyToManyField(Link, blank=True)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"
