from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    rating = models.IntegerField(default=0, verbose_name="Рейтинг пользователя(mmr)")
    count_submit_task = models.IntegerField(default=0, verbose_name="Количество выполненных заданий")

