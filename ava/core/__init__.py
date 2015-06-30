

# Ensure that Celery is initialised when the module is loaded.
from ava.core.celery import task_manager
