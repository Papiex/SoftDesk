from django.db import models

from . import enums


class Project(models.Model):
    """Model defining a project"""
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=1024)
    type = models.CharField(max_length=16, choices=[(types.name, types.value) for types in enums.Types], blank=True)
    #author_user_id = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    # Pour test
    author_user_id = 'user_test'

    def __str__(self):
        return self.title


class Issue(models.Model):
    """Model defining an issue"""

    project = models.ForeignKey(to=Project, related_name="issues" , on_delete=models.CASCADE)

    title = models.CharField(max_length=255)
    description = models.CharField(max_length=1024)
    tag = models.CharField(max_length=16, choices=[(tag.name, tag.value) for tag in enums.Tags])
    priority = models.CharField(max_length=16, choices=[(priority.name, priority.value) for priority in enums.Priorities])
    status = models.CharField(max_length=16, choices=[(status.name, status.value) for status in enums.Status])
    author_user_id = "user_test"
    assignee_user_id = "user_test"
    created_time = models.DateTimeField(auto_now_add=True)