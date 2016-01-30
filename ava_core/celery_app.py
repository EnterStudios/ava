# Ensure no clash with future
from __future__ import absolute_import
# Celery Import
from celery import Celery
# Django Imports
from django.conf import settings

app = Celery('ava')
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
