# Generated by Django 4.0.3 on 2022-03-15 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_catalog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='emoji',
            field=models.TextField(max_length=2048),
        ),
    ]
