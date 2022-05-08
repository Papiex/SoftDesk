from django.db import models

from enum import Enum


class Types(Enum):
    """Enum of supports types"""
    BACK_END = "Back-end"
    FRONT_END = "Front-end"
    ANDROID = "Android"
    IOS = "iOS"


class Project(models.Model):
    """Model defining a project"""
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=1024)
    type = models.CharField(max_length=16, choices=[(types.name, types.value) for types in Types], blank=True)
    #author_user_id = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    # Pour test
    author_user_id = 'user_test'

    def __str__(self):
        return self.title