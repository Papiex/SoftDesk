from django.db import models

from authentication.models import User

from .. import enums
from .project import Project


class Contributor(models.Model):
    """Model defining a contributor"""

    user = models.ForeignKey(to=User, on_delete=models.CASCADE, blank=True, null=True)
    project = models.ForeignKey(
        to=Project,
        related_name="project_contributor",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    permission = models.CharField(
        max_length=16,
        choices=[
            (permission.name, permission.value)
            for permission in enums.ProjectPermission
        ],
        default="ALL",
    )
    role = models.CharField(
        max_length=16,
        choices=[(role.name, role.value) for role in enums.ProjectRole],
        default="AUTHOR",
    )

    def __str__(self) -> str:
        return f"Contributor: {str(self.user)}"
