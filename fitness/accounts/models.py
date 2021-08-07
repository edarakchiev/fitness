from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from fitness.accounts.managers import FitnessUserManager


class FitnessUser(AbstractBaseUser, PermissionsMixin):
    is_staff = models.BooleanField(
        default=False,
    )
    email = models.EmailField(
        unique=True,
    )
    USERNAME_FIELD = 'email'
    objects = FitnessUserManager()


class Profile(models.Model):
    first_name = models.CharField(
        max_length=15,
    )
    last_name = models.CharField(
        max_length=15,
    )
    profile_image = models.ImageField(
        upload_to='profiles',
        blank=True,
    )
    user = models.OneToOneField(
        FitnessUser,
        on_delete=models.CASCADE,
        primary_key=True,
    )


from .signals import *
