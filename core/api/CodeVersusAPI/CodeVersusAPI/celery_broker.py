from __future__ import absolute_import
import os
from celery import Celery

from CodeVersusAPI.settings import CELERY_BROKER_URL


# this code copied from manage.py
# set the default Django settings module for the 'celery' app.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'CodeVersusAPI.settings')
app = Celery("CodeVersusAPI")
# read config from Django settings, the CELERY namespace would make celery
# config keys has `CELERY` prefix
app.config_from_object('django.conf:settings')
app.conf.broker_url = CELERY_BROKER_URL
# load tasks.py in django apps
app.autodiscover_tasks()