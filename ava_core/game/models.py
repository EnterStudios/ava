import logging

from ava_core.abstract.models import ReferenceModel

from django.db import models

log = logging.getLogger(__name__)


class Achievement(ReferenceModel):
    score = models.IntegerField()
    icon_url = models.URLField()

    def __str__(self):
        return self.name





