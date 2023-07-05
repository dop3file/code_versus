from django.db import models
from django.contrib.auth.models import User


class TaskLevel(models.Model):
    level = models.CharField(verbose_name="Уровень задачи(ex Easy, Medium, Hard)")

    def __str__(self):
        return self.level


class Task(models.Model):
    title = models.CharField(
        max_length=256,
        verbose_name="Заголовок задачи",
        null=False,
        blank=False
    )
    description = models.TextField(
        verbose_name="Описание задачи",
        null=True
    )
    level = models.ForeignKey(TaskLevel, on_delete=models.DO_NOTHING)
    time_complexity = models.IntegerField(
        verbose_name="Временной предел выполнения задачи",
        null=False,
        blank=False
    )
    space_complexity = models.IntegerField(
        verbose_name="Предел по памяти выполнения задачи",
        null=False,
        blank=False
    )
    time_create = models.DateTimeField(auto_now_add=True)

    def __repr__(self):
        return f"<Task {self.pk} {self.title}>"


class Test(models.Model):
    status = models.BooleanField(null=False, blank=False, verbose_name="Статус(выполнен ли тест)")
    test_service_id = models.UUIDField(verbose_name="Айди для микросервиса с тестами")
    details = models.CharField(default="success", verbose_name="Описание выполнения теста")
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь который выполнил тест")


