from django.contrib.auth.models import AbstractUser
from rest_framework.validators import UniqueValidator

from django.db import models


class User(AbstractUser):

    first_name = models.CharField(max_length=32, blank=False)
    last_name = models.CharField(max_length=32, blank=False)
