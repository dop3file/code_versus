# Generated by Django 4.2.2 on 2023-07-06 09:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tasks', '0004_alter_test_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='test',
            name='task',
        ),
        migrations.RemoveField(
            model_name='test',
            name='user',
        ),
        migrations.AddField(
            model_name='test',
            name='space_complexity',
            field=models.IntegerField(default=0, verbose_name='Предел по памяти выполнения задачи'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='test',
            name='time_complexity',
            field=models.IntegerField(default=0, verbose_name='Временной предел выполнения задачи'),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='TestGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=False, verbose_name='Статус выполнения всех тестов')),
                ('time_create', models.DateTimeField(auto_now_add=True)),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tasks.task')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='test',
            name='task_group',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='tasks.testgroup', verbose_name='Группа тестов'),
            preserve_default=False,
        ),
    ]
