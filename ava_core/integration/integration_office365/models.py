import logging

from django.db import models

from ava_core.integration.integration_abstract.models import IntegrationAdapter

log = logging.getLogger(__name__)


class Office365IntegrationAdapter(IntegrationAdapter):
    domain = models.URLField(unique=True)
    description = models.CharField(max_length=500)


class Office365AuthorizationStore(models.Model):
    integration_id = models.IntegerField()
