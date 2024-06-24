import uuid
from django.db import models
from .managers import CustomUserManager
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    """
    Class for create model of users
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=30, null=False, blank=False)
    email = models.EmailField(unique=True, null=False, blank=False)

    REQUIRED_FIELDS = ["name"]
    USERNAME_FIELD = "email"
    objects = CustomUserManager()

    def __str__(self):

        return self.email



