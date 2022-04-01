# Generated by Django 4.0.3 on 2022-03-28 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("authentication", "0003_alter_user_email"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="user",
            name="links",
        ),
        migrations.AddField(
            model_name="user",
            name="facebook",
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="user",
            name="github",
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="user",
            name="instagram",
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="user",
            name="linkedin",
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="user",
            name="website",
            field=models.URLField(blank=True, null=True),
        ),
        migrations.DeleteModel(
            name="Link",
        ),
    ]
