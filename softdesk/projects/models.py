from django.db import models


class Project(models.Model):
    """Model defining a project"""
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=1024)

    def __str__(self):
        return self.title