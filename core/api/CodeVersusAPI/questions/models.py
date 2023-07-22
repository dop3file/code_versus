from django.db import models


class Question(models.Model):
    title = models.CharField(
        max_length=4096,
        verbose_name="Заголовок вопроса"
    )


class Answer(models.Model):
    title = models.CharField(
        max_length=4096,
        verbose_name="Заголовок ответа"
    )
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

