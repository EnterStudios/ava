from django.core.urlresolvers import reverse
from django.db import models
from django.db.models import Model

from apps.ava_core.models import TimeStampedModel, ReferenceModel
from apps.ava_test.models import Test
from apps.ava_test_email.helpers import generate_hex_token


class EmailTest(Test):
    emailtesttype = models.ForeignKey('EmailTestType', null=False)
    fromaddr = models.EmailField(null=False)
    subject = models.TextField(max_length=200, null=False)
    body = models.TextField(max_length=2000, null=False)
    messagetype = models.ForeignKey('EmailMessageType', null=False)

    def __unicode__(self):
        return self.name or u''

    def get_absolute_url(self):
        return reverse('email-test-detail',kwargs={'pk': self.pk})


class EmailTestType(ReferenceModel):
    pass


class EmailMessageType(ReferenceModel):
    pass


class EmailTestTarget(TimeStampedModel):
    emailtest = models.ForeignKey('EmailTest', null=False, related_name='targets')
    target = models.ForeignKey('ava_core_identity.Identifier', null=False)
    token = models.CharField(max_length=100, null=False, unique=True, default=generate_hex_token)

    class Meta:
        unique_together = ("emailtest", "target", "token")

    def __unicode__(self):
        return self.target or u''

    def get_absolute_url(self):
        return reverse('email-test-target-detail',kwargs={'pk': self.pk})


class EmailTemplate(Model):
    subject = models.TextField()
    message = models.TextField()

    def __unicode__(self):
        return self.subject or u''

    def get_absolute_url(self):
        return reverse('email-template-detail',kwargs={'pk': self.pk})
