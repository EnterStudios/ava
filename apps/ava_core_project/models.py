from django.db import models
from django.contrib.auth.models import User

from apps.ava_core.models import TimeStampedModel, ReferenceModel


class Project(TimeStampedModel):
    name=models.CharField(max_length=100)
    user = models.ForeignKey(User)
    description=models.CharField(max_length=300)

    def __unicode__(self):
        return self.name or u''

    def get_absolute_url(self):
	    return reverse('project-detail',kwargs={'pk': self.pk})
    

