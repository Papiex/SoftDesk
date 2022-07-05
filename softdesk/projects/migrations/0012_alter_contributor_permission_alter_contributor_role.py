# Generated by Django 4.0.4 on 2022-06-19 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("projects", "0011_project_contributors_alter_contributor_role"),
    ]

    operations = [
        migrations.AlterField(
            model_name="contributor",
            name="permission",
            field=models.CharField(
                choices=[("Read", "Read"), ("All", "All")], default="All", max_length=16
            ),
        ),
        migrations.AlterField(
            model_name="contributor",
            name="role",
            field=models.CharField(
                choices=[
                    ("Author", "Author"),
                    ("Manager", "Manager"),
                    ("Creator", "Creator"),
                ],
                default="Author",
                max_length=16,
            ),
        ),
    ]
