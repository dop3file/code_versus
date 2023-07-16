import uuid

from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    rating = models.IntegerField(default=0, verbose_name="Рейтинг пользователя(mmr)")
    count_submit_task = models.IntegerField(default=0, verbose_name="Количество выполненных заданий")
    is_activate = models.BooleanField(default=False)


class VerificationCode(models.Model):
    """
    Код для потдвержения регистрации
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)