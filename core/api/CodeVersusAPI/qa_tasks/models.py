from django.db import models


class Question(models.Model):
    title = models.CharField(
        max_length=2056,
        verbose_name="Заголовок вопроса"
    )


class Answer(models.Model):
    title = models.CharField(
        max_length=1024,
        verbose_name="Заголовок ответа"
    )
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    is_multiply = models.BooleanField(default=False)





