# Django Imports
from django.conf import settings
from django.db import models
# Python Imports
import logging
# Local Imports
from ava_core.abstract.models import TimeStampedModel

# Loggers
log = logging.getLogger(__name__)


class Question(TimeStampedModel):
    NEW = 0
    OPEN = 1
    CLOSED_RESOLVED = 2
    CLOSED_UNRESOLVED = 3
    AWAITING_INFO = 4

    TYPE_STATUS = (
        (NEW, 'New'),
        (CLOSED_RESOLVED, 'Closed (Resolved)'),
        (CLOSED_UNRESOLVED, 'Closed (Unresolved)'),
        (AWAITING_INFO, 'Awaiting information'),
    )

    LOW = 0
    MEDIUM = 1
    HIGH = 2
    CRITICAL = 3

    TYPE_PRIORITY = (
        (LOW, 'Low'),
        (MEDIUM, 'Medium'),
        (HIGH, 'High'),
        (CRITICAL, 'Critical'),
    )

    owner = models.ForeignKey(to=settings.USER_MODEL, null=False)
    status_type = models.IntegerField(choices=TYPE_STATUS, default=NEW)
    priority_type = models.IntegerField(choices=TYPE_PRIORITY, default=LOW)
    description = models.TextField(max_length=1000, blank=True, null=True)
    is_resolved = models.BooleanField(default=False)

    def delete(self, using=None, keep_parents=False):
        self.is_resolved = True
        self.save()

    @staticmethod
    def get_display_status_type(self, lookup):
        return self.TYPE_STATUS[lookup]

    @staticmethod
    def get_display_priority_type(self, lookup):
        return self.TYPE_PRIORITY[lookup]


class Suspicious(Question):
    url = models.URLField()
    incident_date = models.DateTimeField()


class ReportResponse(TimeStampedModel):
    owner = models.ForeignKey(to=settings.USER_MODEL, null=False)
    message = models.TextField(max_length=1000, blank=True, null=True)
    parent_response = models.ForeignKey(to='ReportResponse', null=True, blank=True)
    question = models.ForeignKey(to=Question, null=False, blank=False, related_name="question_responses")
