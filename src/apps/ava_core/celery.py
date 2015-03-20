from __future__ import absolute_import

import os
from celery import Celery
from django.conf import settings

# set the Django settings module for the 'celery' program
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')

task_manager = Celery('AVA')

# Using a string here means the worker will not have to
# pickle the object when using Windows.
task_manager.config_from_object('django.conf:settings')
# Pick up all tasks in AVA apps
task_manager.autodiscover_tasks(lambda: settings.LOCAL_APPS)
