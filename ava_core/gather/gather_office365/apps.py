# Django Imports
from django.apps import AppConfig


# Implementation
class MyConfig(AppConfig):
    name = 'ava.gather.office365'
    label = 'ava_gather_office365'
    verbose_name = 'Gather : Office365'

    def ready(self):
        import ava.gather_office365.signals
