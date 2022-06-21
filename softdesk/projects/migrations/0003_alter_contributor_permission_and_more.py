# Generated by Django 4.0.4 on 2022-06-19 12:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_project_contributors'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contributor',
            name='permission',
            field=models.CharField(choices=[('AUTHOR', 'Author'), ('MANAGER', 'Manager'), ('CREATOR', 'Creator')], default='Author', max_length=16),
        ),
        migrations.AlterField(
            model_name='contributor',
            name='project',
            field=models.ForeignKey(blank=True, default='All', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='project', to='projects.project'),
        ),
    ]