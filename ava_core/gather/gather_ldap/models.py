from django.db import models

from ava_core.abstract.models import TimeStampedModel
from ava_core.integration.integration_ldap.models import LDAPIntegrationAdapter
from ava_core.gather.gather_abstract.models import GatherHistory


class LDAPGatherHistory(GatherHistory):
    integration = models.ForeignKey(to=LDAPIntegrationAdapter, null=False, related_name='ldap_integration_history')
