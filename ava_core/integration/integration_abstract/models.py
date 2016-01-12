import logging

from django.contrib.postgres.fields import JSONField

from ava_core.abstract.models import ReferenceModel, TimeStampedModel
from django.db import models

log = logging.getLogger(__name__)


class IntegrationAdapter(TimeStampedModel):
    name = models.CharField(max_length=100, verbose_name='Name', unique=True)
    credential = JSONField(null=True)

    def __str__(self):
        return self.name

    class Meta:
       pass
