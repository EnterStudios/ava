from django.db import models

from ava_core.abstract.models import TimeStampedModel
from ava_core.integration.integration_google.models import GoogleIntegrationAdapter
from ava_core.gather.gather_abstract.models import GatherHistory


class GoogleGatherHistory(GatherHistory):
    integration = models.ForeignKey(to=GoogleIntegrationAdapter, null=False, related_name='google_integration_history')
