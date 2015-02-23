from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

from apps.ava_core.models import TimeStampedModel,ReferenceModel
from apps.ava_core_identity.models import Person, Identifier
from apps.ava_core_project.models import Project


class Industry (ReferenceModel):
    pass

class OrganisationUnitType (ReferenceModel):
    pass

class OrganisationSize (ReferenceModel):
    pass

class Organisation (TimeStampedModel):
    name = models.CharField(max_length=100)
    industry = models.ForeignKey('Industry', null=False)
    size= models.ForeignKey('OrganisationSize', null=False)
    user = models.ForeignKey(User)
    project = models.ForeignKey('ava_core_project.Project')

    def __unicode__(self):
        return self.name or u''

    def get_absolute_url(self):
	    return reverse('org-detail',kwargs={'pk': self.pk})

class OrganisationGroup (TimeStampedModel):

    AD = 'AD'
    SOCIAL = 'SO'
    PROJECT = 'PR'
    WORKING = 'WG'
    TEAM = 'TE'

    GROUP_TYPE_CHOICES = (
        (AD,  'Active Directory'),
        (SOCIAL,  'Social Group'),
        (PROJECT,  'Project'),
        (WORKING, 'Working Group'),
        (TEAM, 'Team'),

    )

    name = models.CharField(max_length=100)
    grouptype = models.CharField(max_length=7,
                            choices=GROUP_TYPE_CHOICES, default=AD,
                                verbose_name='Group Type')
    organisation = models.ForeignKey('Organisation', null=False)

    def __unicode__(self):
        return self.name or u''

    def get_absolute_url(self):
	    return reverse('org-group-detail',kwargs={'pk': self.pk})

class GroupIdentifier(TimeStampedModel):
    group = models.ForeignKey(OrganisationGroup,null=False)
    identifier = models.ForeignKey(Identifier, null=False)

    def __unicode__(self):
        return self.group.name +" -> " + self.identifier.identifier

    def get_absolute_url(self):
	    return reverse('group-detail',kwargs={'pk': self.pk})

    class Meta:
        unique_together = ("identifier", "group")

