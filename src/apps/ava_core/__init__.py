

# Ensure that Celery is initialised when the module is loaded.
from apps.ava_core.celery import task_manager
