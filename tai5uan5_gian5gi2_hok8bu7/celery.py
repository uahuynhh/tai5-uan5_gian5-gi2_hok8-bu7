from __future__ import absolute_import, unicode_literals

import os

from celery import Celery
from django.conf import settings


# set the default Django settings module for the 'celery' program.
os.environ.setdefault(
    'DJANGO_SETTINGS_MODULE', 'tai5uan5_gian5gi2_hok8bu7.settings')

try:
    rabbitmq = 'amqp://ti1a2:gau5tsa2@{}:5672/hok8_bu7'.format(
        settings.RABBIT_MQ_TSU2_KI1
    )
except AttributeError:
    rabbitmq = None

app = Celery('tai5uan5_gian5gi2_hok8bu7', broker=rabbitmq)

# Using a string here means the worker don't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()
