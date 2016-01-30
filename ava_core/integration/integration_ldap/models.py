import logging

from django.db import models

from ava_core.integration.integration_abstract.models import IntegrationAdapter

log = logging.getLogger(__name__)


class LDAPIntegrationAdapter(IntegrationAdapter):
    # dump_dn = "dc=ava,dc=test,dc=domain"
    # server = 'gather_ldap://dc.ava.test.domain'

    dump_dn = models.CharField(max_length=100, verbose_name='Domain')
    server = models.CharField(max_length=100, verbose_name='Server')
    salt = models.CharField(max_length=100)
    ldap_password = models.CharField(max_length=100)
    ldap_user = models.CharField(max_length=100)
