"""
This file contains Database table definition in python
class with Django ORM installed.
"""
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.exceptions import ValidationError
from phonenumber_field.modelfields import PhoneNumberField


def validate_phone_number(value):
    """
    Validate phone number
    """
    if len(value) != 10:
        raise ValidationError("Phone number must be 10 digits")
    
    if not value.isdigit():
        raise ValidationError("Phone number must be numeric")
    
     

# class Link(models.Model):
#     """Model for storing social links

#     Returns:
#         Link Object
#     """

#     url = models.URLField(max_length=200)
#     is_deleted = models.BooleanField(default=False)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     deleted_at = models.DateTimeField(null=True, blank=True)
#     deleted_by = models.ForeignKey(
#         "User", on_delete=models.SET_NULL, null=True, blank=True
#     )

#     def __str__(self):
#         return f"{self.url}"


class User(AbstractUser):
    """User model that extends the default django user and add
    additional information's.

    Returns:
        User Object
    """

    email = models.EmailField("email address", unique=True)
    gender = models.CharField(max_length=10, choices=(
        ('male', 'male'), ('female', 'female')), null=True, blank=True)
    phone_number = models.CharField(max_length=15, validators=[validate_phone_number])
    birthdate = models.DateField(null=True, blank=True)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    deleted_by = models.ForeignKey(
        "self", on_delete=models.SET_NULL, null=True, blank=True, related_name="deleter"
    )
    approved_by = models.ForeignKey(
        "self",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="approver",
    )
    approved_at = models.DateTimeField(null=True, blank=True)
    approved_status = models.BooleanField(default=False)
    last_login_ip = models.GenericIPAddressField(null=True, blank=True)
    website = models.URLField(null=True, blank=True)
    linkedin = models.URLField(null=True, blank=True)
    instagram = models.URLField(null=True, blank=True)
    facebook = models.URLField(null=True, blank=True)
    github = models.URLField(null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"
    
    @property
    def dob(self):
        return self.birthdate.strftime("%Y-%m-%d") if self.birthdate else None
