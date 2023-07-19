from django.db import models
from .managers import CustomUserManager
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin
)
from django.utils.translation import gettext_lazy as _


class CustomUser(AbstractBaseUser, PermissionsMixin):
    """
    Class for create model of users
    """
    first_name = models.CharField(max_length=30, null=False, blank=False)
    last_name = models.CharField(max_length=30, null=False, blank=False)
    phone_no = models.CharField(max_length=20, null=True, blank=False)
    email = models.EmailField(_('email address'), unique=True, error_messages={"unique": "This email address is already associated with another account."})

    REQUIRED_FIELDS = ["first_name", "last_name"]
    USERNAME_FIELD = "email"
    objects = CustomUserManager()

    def __str__(self):

        return self.email


