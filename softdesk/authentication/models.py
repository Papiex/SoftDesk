from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """model who define a user"""

    first_name = models.CharField(max_length=32, blank=False)
    last_name = models.CharField(max_length=32, blank=False)
