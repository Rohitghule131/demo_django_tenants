from django.contrib.auth.models import BaseUserManager


class CustomUserManager(BaseUserManager):
    """
    Class for creating custom manager for managing custom user.
    """
    def create_user(self, email=None, first_name=None, last_name=None, password=None, **extra_fields):
        """
        Function for creating user w.r.t custom user.
        """
        user = self.model(
            email=self.normalize_email(email)
        )
        user.first_name = first_name
        user.last_name = last_name
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, first_name, email, password, last_name):
        """
        Function for creating superuser.
        """
        user = self.create_user(
            email,
            first_name,
            last_name,
            password,
        )
        user.is_superuser = True
        user.is_active = True
        user.is_staff = True
        user.save(using=self._db)
        return user
