from django.db import models
from django.conf import settings

from .issue import Issue


class Comment(models.Model):
    """Model defining a comment"""

    issue = models.ForeignKey(to=Issue, related_name="comments", on_delete=models.CASCADE)
    description = models.CharField(max_length=1024)
    author_user_id = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True)