from django.db import models
from django.core.urlresolvers import reverse

from apps.ava_core.models import TimeStampedModel, ReferenceModel

class GroupType(ReferenceModel):
    pass

    def get_absolute_url(self):
        return reverse('group-type-detail',kwargs={'pk': self.pk})

class Group (TimeStampedModel):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    group_type = models.ForeignKey('GroupType', null=False)
    parent = models.ForeignKey('Group', null=True, blank=True)

    def __unicode__(self):
        return self.name or u''

    def get_absolute_url(self):
        return reverse('group-detail',kwargs={'pk': self.pk})

    class Meta:
        unique_together = ("name", "group_type")