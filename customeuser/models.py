from django.db import models
from .managers import CustomUserManager
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    """
    Class for create model of users
    """
    first_name = models.CharField(max_length=30, null=False, blank=False)
    last_name = models.CharField(max_length=30, null=False, blank=False)
    phone_no = models.CharField(max_length=20, null=True, blank=False)
    email = models.EmailField(unique=True, null=False, blank=False)

    REQUIRED_FIELDS = ["first_name", "last_name"]
    USERNAME_FIELD = "email"
    objects = CustomUserManager()

    def __str__(self):

        return self.email


