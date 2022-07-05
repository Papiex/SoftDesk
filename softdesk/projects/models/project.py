from django.db import models

from authentication.models import User

from .. import enums


class Project(models.Model):
    """Model defining a project"""

    title = models.CharField(max_length=255)
    description = models.CharField(max_length=1024)
    type = models.CharField(
        max_length=16,
        choices=[(types.name, types.value) for types in enums.Types],
        blank=True,
    )
    author_user_id = models.ForeignKey(to=User, on_delete=models.CASCADE)
    contributors = models.ManyToManyField(
        to=User, through="Contributor", related_name="contributors"
    )

    def __str__(self):
        return self.title
