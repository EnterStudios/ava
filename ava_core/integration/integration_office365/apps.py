# Django Imports
from django.apps import AppConfig


# Implementation
class MyConfig(AppConfig):
    name = 'ava.integration_office365'
    label = 'ava_oauth_office365'
    verbose_name = 'integration_office365'

    def ready(self):
        import ava.oauth_office365.signals
