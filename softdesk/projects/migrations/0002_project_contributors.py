# Generated by Django 4.0.4 on 2022-06-19 12:26

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("authentication", "0004_alter_user_first_name_alter_user_last_name"),
        ("projects", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="project",
            name="contributors",
            field=models.ManyToManyField(
                related_name="contributors",
                through="projects.Contributor",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
