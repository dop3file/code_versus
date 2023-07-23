import uuid
from enum import Enum

from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    rating = models.IntegerField(default=0, verbose_name="Рейтинг пользователя(mmr)")
    count_submit_task = models.IntegerField(default=0, verbose_name="Количество выполненных заданий")
    email = models.EmailField(unique=True)
    is_activate = models.BooleanField(default=False)


class VerificationCodeType(Enum):
    REGISTRATION = "registartion"
    RESET = "reset"

    @classmethod
    def choices(cls):
        return tuple((field.name, field.value) for field in cls)


class VerificationCode(models.Model):
    """
    Код для потдвержения регистрации
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    code_type = models.CharField(max_length=256, default=VerificationCodeType.REGISTRATION.value, choices=VerificationCodeType.choices())