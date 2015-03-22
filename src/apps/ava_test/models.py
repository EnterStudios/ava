from django.db import models
from django.contrib.auth.models import User

from apps.ava_core.models import TimeStampedModel,ReferenceModel


class Test(TimeStampedModel):

    EMAIL = 'EMAIL'
    TWITTER = 'TWITTER'

    TEST_TYPE_CHOICES = (
        (EMAIL,    'Email'),
        (TWITTER,  'Twitter'),
    )

    TEST_TYPE_ICONS = (
        (EMAIL,    'envelope'),
        (TWITTER,  'twitter'),
    )

    NEW = 'NEW'
    COMPLETE = 'COMPLETE'
    ERROR = 'ERROR'
    SCHEDULED = 'SCHEDULED'
    RUNNING = 'RUNNING'

    TEST_STATUS_CHOICES = (
        (NEW,       'New'),
        (COMPLETE,  'Complete'),
        (ERROR,     'An error occurred'),
        (SCHEDULED, 'Scheduled'),
        (RUNNING ,  'In progress'),
    )

    name=models.CharField(max_length=100)
    user = models.ForeignKey(User)
    description=models.CharField(max_length=300)

    testtype = models.CharField(max_length=7,
                                  choices=TEST_TYPE_CHOICES,
                                  default=EMAIL,
                                  verbose_name='Test Type')

    teststatus = models.CharField(max_length=10,
                                  choices=TEST_STATUS_CHOICES,
                                  default=NEW,
                                  verbose_name='Test Status')

    def __unicode__(self):
        return self.name or u''


class TestResult (TimeStampedModel):
    class Meta:
        abstract = True
    
    ipaddress = models.CharField(max_length=50)
    method = models.CharField(max_length=10)            # GET/POST/etc
    host = models.CharField(max_length=260)             # host name:port
    path = models.TextField(null=True, blank=True)      # /path/to/page/
    contentlength = models.CharField(max_length=10, null=True, blank=True)
    contenttype = models.CharField(max_length=100, null=True, blank=True)
    ua = models.TextField(null=True, blank=True)        # User-Agent
    referrer = models.TextField(null=True, blank=True)  # Referer
    via = models.TextField(null=True, blank=True)       # Via

    def __unicode__(self):
        return unicode(self.created)

