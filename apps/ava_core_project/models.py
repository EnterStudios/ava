from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

from apps.ava_core.models import TimeStampedModel, ReferenceModel

'''
TODO this needs to also allow for idenities, identifiers and people
'''
class Project(TimeStampedModel):
    name=models.CharField(max_length=100)
    user = models.ForeignKey(User)
    description=models.CharField(max_length=300)
    group = models.ManyToManyField('ava_core_group.Group', null=True, blank=True)

    def __unicode__(self):
        return self.name or u''

    def get_absolute_url(self):
	    return reverse('project-detail',kwargs={'pk': self.pk})
    
    class Meta:
        unique_together = ("name", "user")
