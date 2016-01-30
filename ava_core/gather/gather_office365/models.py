from django.db import models

from ava_core.gather.gather_abstract.models import GatherHistory
from ava_core.integration.integration_office365.models import Office365IntegrationAdapter


class Office365GatherHistory(GatherHistory):
    integration = models.ForeignKey(to=Office365IntegrationAdapter, null=False,
                                    related_name='office365_integration_history')
