from django.conf import settings
from django.db import models

from .. import enums
from .project import Project


class Issue(models.Model):
    """Model defining an issue"""

    project = models.ForeignKey(
        to=Project, related_name="issues", on_delete=models.CASCADE
    )

    title = models.CharField(max_length=255)
    description = models.CharField(max_length=1024)
    tag = models.CharField(
        max_length=16, choices=[(tag.name, tag.value) for tag in enums.Tags]
    )
    priority = models.CharField(
        max_length=16,
        choices=[(priority.name, priority.value) for priority in enums.Priorities],
    )
    status = models.CharField(
        max_length=16, choices=[(status.name, status.value) for status in enums.Status]
    )
    author_user_id = models.ForeignKey(
        to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE
    )
    assignee_user_id = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="assignee_user",
    )
    created_time = models.DateTimeField(auto_now_add=True)
