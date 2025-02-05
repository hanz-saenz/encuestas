from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

#configuracion de celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'encuestas.settings')

app = Celery('encuestas')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()