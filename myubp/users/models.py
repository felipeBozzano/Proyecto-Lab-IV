from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager


class UserProfileManager(BaseUserManager):
    """
    Manage de ABM of users
    """

    def get_user_id(self):
        return self.id

    def create_user(self, email, name, password=None):
        """
        Creates a normal user
        """

        if not email:
            raise ValueError('Usuario debe tener un email')

        email = self.normalize_email(email)
        user = self.model(email=email, name=name,)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password):
        """
        Creates a super user
        """

        user = self.create_user(email, name, password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """
    Custom user profile model
    """

    email = models.EmailField(max_length=255, unique=True)
    name = models.TextField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_name(self):
        """
        Returns the name of the user
        """

        return self.name

    def __str__(self):
        """
        Overloads the print function for user
        """

        return self.email
