# Generated by Django 4.0.4 on 2022-06-06 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("authentication", "0003_alter_user_is_active"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="first_name",
            field=models.CharField(max_length=32),
        ),
        migrations.AlterField(
            model_name="user",
            name="last_name",
            field=models.CharField(max_length=32),
        ),
    ]
