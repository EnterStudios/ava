from django.db import models
from django.contrib.auth.models import User

from apps.ava_core.models import TimeStampedModel,ReferenceModel


class Test(TimeStampedModel):

    NEW = 'NEW'
    COMPLETE = 'COMPLETE'
    ERROR = 'ERROR'
    SCHEDULED = 'SCHEDULED'
    RUNNING = 'RUNNING'

    STATUS_CHOICES = (
        (NEW,       'New'),
        (COMPLETE,  'Complete'),
        (ERROR,     'An error occurred'),
        (SCHEDULED, 'Scheduled'),
        (RUNNING ,  'In progress'),
    )

    name=models.CharField(max_length=100)
    user = models.ForeignKey(User)
    description=models.CharField(max_length=300)
    testtype = models.ForeignKey('TestType', null=False)
    timingtype = models.ForeignKey('TimingType', null=False)
    teststatus = models.CharField(max_length=10,
                                  choices=STATUS_CHOICES,
                                  default=NEW,
                                  verbose_name='Test Status')

    def __unicode__(self):
        return self.name or u''


class TestType (ReferenceModel):
    url= models.TextField(max_length=50, null=False)
    icon= models.CharField(max_length=50, null=True, blank=True)


class TimingType (ReferenceModel):
    icon= models.CharField(max_length=50, null=True, blank=True)


class TestResult (TimeStampedModel):
    token= models.CharField(max_length=8)
    ua = models.TextField()



