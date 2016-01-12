# Django Imports
from django.apps import AppConfig


# Implementation
class MyConfig(AppConfig):
    name = 'ava.integration_ldap'
    label = 'ava_oauth_ldap'
    verbose_name = 'integration_ldap'

    def ready(self):
        import ava.oauth_ldap.signals
