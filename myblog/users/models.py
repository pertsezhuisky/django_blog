import django.db.models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone


class User(AbstractUser):
    date_birth = django.db.models.DateField(
        name="date_birth",
        verbose_name="Date_Birth",
        help_text="Date of birth",
        blank=True,
        null=True,
    )
    date_joined = django.db.models.DateField(
        name="date_joined",
        verbose_name="Date_Joined",
        help_text="When he/she became our member",
        default=timezone.now,
    )
    bio = django.db.models.TextField(
        name="bio",
        verbose_name="BIO",
        max_length=200,
        help_text="Everyone wants to know it",
        null=True,
        blank=True,
    )
    avatar = django.db.models.ImageField(
        name="avatar",
        upload_to="users_avatars/",
        verbose_name="User_avatar",
        default="users_avatars/avatar128.jpg",
        null=True,
        blank=True,
    )
