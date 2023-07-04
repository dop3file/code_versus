from django.db import models


class TaskLevel(models.Model):
    level = models.CharField(verbose_name="Уровень задачи(ex Easy, Medium, Hard)")


class Task(models.Model):
    title = models.CharField(
        max_length=256,
        verbose_name="Заголовок задачи"
    )
    description = models.TextField(
        verbose_name="Описание задачи"
    )
    level = models.ForeignKey(TaskLevel, on_delete=models.DO_NOTHING)
    time_complexity = models.IntegerField(
        verbose_name="Временной предел выполнения задачи"
    )
    space_complexity = models.IntegerField(
        verbose_name="Предел по памяти выполнения задачи"
    )
    time_create = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title