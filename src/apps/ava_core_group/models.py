from django.db import models
from django.core.urlresolvers import reverse

from apps.ava_core.models import TimeStampedModel, ReferenceModel


class Group(TimeStampedModel):
    AD = 'ACTIVE DIRECTORY'
    SOCIAL = 'SOCIAL GROUP'
    PROJECT = 'PROJECT'
    WORKING = 'WORKING GROUP'
    TEAM = 'TEAM'
    GENERIC = 'GENERIC'
    ORG = 'ORGANISATION'
    DIST = 'DISTRIBUTION LIST'

    GROUP_TYPE_CHOICES = (
        (AD, 'Active Directory'),
        (SOCIAL, 'Social Group'),
        (PROJECT, 'Project'),
        (WORKING, 'Working Group'),
        (TEAM, 'Team'),
        (GENERIC, 'Generic Group'),
        (ORG, 'Organisation'),
        (DIST, 'Distribution List'),
    )

    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    group_type = models.CharField(max_length=20, choices=GROUP_TYPE_CHOICES, default=GENERIC, verbose_name='Group Type')
    parent = models.ForeignKey('Group', null=True, blank=True)

    def __unicode__(self):
        return self.name or u''

    def get_absolute_url(self):
        return reverse('group-detail', kwargs={'pk': self.pk})

    class Meta:
        unique_together = ("name", "group_type")
        ordering = ['name', 'group_type']
