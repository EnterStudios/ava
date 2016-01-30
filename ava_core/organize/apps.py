# Django Imports
from django.apps import AppConfig


# Implementation
class OrganizeConfig(AppConfig):
    name = 'ava_core.organize'
    verbose_name = 'Organize Application'

    def ready(self):
        import ava_core.organize.signals