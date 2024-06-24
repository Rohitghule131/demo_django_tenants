from django.contrib.auth.models import BaseUserManager


class CustomUserManager(BaseUserManager):
    """
    Class for creating custom manager for managing custom user.
    """
    def create_user(self, email=None, name=None, password=None, **extra_fields):
        """
        Function for creating user w.r.t custom user.
        """
        user = self.model(
            email=self.normalize_email(email)
        )
        user.name = name
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, name, email, password):
        """
        Function for creating superuser.
        """
        user = self.create_user(
            email,
            name,
            password,
        )
        user.is_superuser = True
        user.is_active = True
        user.is_staff = True
        user.save(using=self._db)
        return user
