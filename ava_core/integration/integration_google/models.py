import logging

from django.db import models

from ava_core.abstract.models import TimeStampedModel
from ava_core.integration.integration_abstract.models import IntegrationAdapter

log = logging.getLogger(__name__)


class GoogleIntegrationAdapter(IntegrationAdapter):
    domain = models.URLField(unique=True)
    description = models.CharField(max_length=500)

class GoogleAuthorizationStore(models.Model):
    integration_id = models.IntegerField()
