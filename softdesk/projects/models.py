from django.conf import settings
from django.db import models


TYPES = (
    ('BACK-END', 'Back-end'),
    ('FRONT-END', 'Front-end'),
    ('ANDROID', 'Android'),
    ('IOS', 'iOS'),
)

class Project(models.Model):
    """Model defining a project"""
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=1024)
    type = models.CharField(max_length=16, choices=TYPES, blank=True)
    #author_user_id = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    # Pour test
    author_user_id = 'user_test'

    def __str__(self):
        return self.title