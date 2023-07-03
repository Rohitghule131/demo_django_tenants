from django.db import models
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    """
    Class for create model of users
    """
    phone_no = models.CharField(max_length=20, null=True, blank=False)
    email = models.EmailField(unique=True, null=False, blank=False)

    REQUIRED_FIELDS = ["first_name", "last_name"]
    USERNAME_FIELD = "email"


class CustomToken(Token):
    """
    Class for create custom token model.
    """
    email = models.EmailField(null=True, blank=True)

