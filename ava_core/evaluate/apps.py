# Django imports
from django.apps import AppConfig


# Implementation
class EvaluateConfig(AppConfig):
    name = 'ava_core.evaluate'
    verbose_name = 'Evaluate Application'

    def ready(self):
        import ava_core.evaluate.signals