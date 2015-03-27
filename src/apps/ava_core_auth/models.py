from django.db import models
from django.contrib.auth.models import User
from apps.ava_core.models import ReferenceModel


class UserRights(models.Model):
    class Meta:
        verbose_name = 'User Rights'
        verbose_name_plural = verbose_name
    
    user = models.OneToOneField(User, related_name='rights')
    is_admin = models.BooleanField(default=False)
    
    def __unicode__(self):
        return unicode(self.user)
    
    @classmethod
    def get(cls, user):
        rights, created = UserRights.objects.get_or_create(user=user)
        if created:
            rights.is_admin = user.is_superuser
            rights.save()
        return rights


class Team(ReferenceModel):
    users = models.ManyToManyField(User, related_name='teams')

