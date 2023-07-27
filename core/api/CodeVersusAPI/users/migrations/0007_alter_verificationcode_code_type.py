# Generated by Django 4.2.2 on 2023-07-23 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_alter_customuser_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='verificationcode',
            name='code_type',
            field=models.CharField(choices=[('REGISTRATION', 'registartion'), ('RESET', 'reset')], default='registartion', max_length=256),
        ),
    ]
