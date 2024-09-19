from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models
from django.contrib.auth.models import BaseUserManager


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name="Адрес электронной почты")
    phone = models.CharField(
        max_length=35, verbose_name="Номер телефона", blank=True, null=True
    )
    tg_name = models.CharField(
        max_length=50, verbose_name="Имя в Телеграм", blank=True, null=True
    )
    country = models.CharField(
        max_length=50, verbose_name="Country", blank=True, null=True
    )
    avatar = models.ImageField(
        upload_to="users/avatars/",
        verbose_name="Фотография профиля",
        blank=True,
        null=True,
    )
    token = models.CharField(
        max_length=100, verbose_name="Token", blank=True, null=True
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()  # Указываем кастомный менеджер

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.email
