from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True, default="Addis Ababa")
    country = models.CharField(max_length=50, blank=True, null=True, default="Ethiopia")
    email = models.EmailField(blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    logo = models.ImageField(upload_to="companies/logos/", blank=True, null=True)

    # Social media links
    facebook = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)
    youtube = models.URLField(blank=True, null=True)
    github = models.URLField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(blank=True, null=True)
    deleted_by = models.ForeignKey(
        "authentication.User",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="companies_deleted",
    )
    created_by = models.ForeignKey(
        "authentication.User",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="companies_created",
    )
    updated_by = models.ForeignKey(
        "authentication.User",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="companies_updated",
    )

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-updated_at", "-created_at"]
