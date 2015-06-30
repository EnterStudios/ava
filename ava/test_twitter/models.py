from django.core.urlresolvers import reverse
from django.db import models

from apps.ava_core.models import TimeStampedModel, ReferenceModel
from apps.ava_test.models import Test, TestResult
from apps.ava_core_identity.models import Identifier, Person


class TwitterTest(Test):
    # twittertesttype = models.ForeignKey('TwitterTestType', null=False)
    tweet = models.ForeignKey('TweetTemplate', null=False, verbose_name='Tweet')
    link = models.ForeignKey('TweetLink', null=False)
    twitteraccount = models.ForeignKey('TwitterAccount', null=False, verbose_name='Send From Twitter Account')

    def __unicode__(self):
        return self.name or ''

    def get_absolute_url(self):
        return reverse('twitter-test-detail', kwargs={'pk': self.pk})


class TwitterTestTarget(TimeStampedModel):
    twittertest = models.ForeignKey('TwitterTest', null=False)
    target = models.ForeignKey('ava_core_identity.Identifier', null=False)

    class Meta:
        unique_together = ("twittertest", "target")

    def __unicode__(self):
        return self.target or ''


class TwitterTestResult(TestResult):
    target = models.ForeignKey('TwitterTestTarget', null=False, related_name='results')


class TweetTemplate(ReferenceModel):
    tweet = models.TextField(max_length=140)


class TwitterAccount(ReferenceModel):
    username = models.CharField(max_length=100, null=False)
    password_enc = models.TextField(null=False)


class TweetLink(ReferenceModel):
    link = models.URLField()
