# Generated by Django 4.0.4 on 2022-05-18 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("project_catalog", "0002_alter_image_image"),
    ]

    operations = [
        migrations.AddField(
            model_name="project",
            name="status",
            field=models.CharField(
                choices=[
                    ("approved", "approved"),
                    ("pending", "pending"),
                    ("rejected", "rejected"),
                ],
                default="pending",
                max_length=10,
            ),
        ),
    ]
