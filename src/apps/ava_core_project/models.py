from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

from apps.ava_core.models import TimeStampedModel
from apps.ava_core_auth.models import UserRights


class Project(TimeStampedModel):
    # General properties
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    owner = models.ForeignKey(User)
    justification = models.TextField()
    startdate = models.DateField(auto_now_add=True, verbose_name='Start Date')
    enddate = models.DateField(verbose_name='End Date',null=True, blank=True,)
    authorisedby = models.CharField(max_length=100, null=True, blank=True, verbose_name='Authorised By')
    # Test targets
    groups = models.ManyToManyField('ava_core_group.Group', null=True, blank=True)
    identities = models.ManyToManyField('ava_core_identity.Identity', null=True, blank=True)
    identifiers = models.ManyToManyField('ava_core_identity.Identifier', null=True, blank=True)

    def __unicode__(self):
        return self.name or u''

    def get_absolute_url(self):
        return reverse('project-detail', kwargs={'pk':self.pk})
    
    def user_has_access(self, user, accesslevel):
        # If the user is the project owner, they automatically get access.
        if user == self.owner:
            return True
        # If the user is a system admin, they automatically get access.
        if UserRights.get(user).is_admin:
            return True
        # Otherwise, check the teams to see if the user is in a team that's
        # been given access.
        for team in self.teams.all():
            if team.has_access(accesslevel) and team.contains_user(user):
                return True
        # Fail to no access.
        return False

    class Meta:
        unique_together = ("name", "owner")
        ordering = ['name', 'owner']


class ProjectAccess(object):
    '''
    Constants that represent the level of access a team can have to project.
    '''
    MODIFY = 3
    RUN_TEST = 2
    VIEW = 1


class ProjectTeam(TimeStampedModel):
    
    ACCESS_LEVEL_CHOICES = (
        (ProjectAccess.MODIFY,   'Modify project and run tests'),
        (ProjectAccess.RUN_TEST, 'View project and run tests'),
        (ProjectAccess.VIEW,     'View project'),
    )
    
    project = models.ForeignKey(Project, related_name='teams')
    team = models.ForeignKey('ava_core_auth.Team', related_name='projects')
    accesslevel = models.IntegerField(choices=ACCESS_LEVEL_CHOICES,
                                      default=ProjectAccess.VIEW,
                                      verbose_name = 'Access Level')

    def has_access(self, accesslevel):
        return self.accesslevel >= accesslevel

    def contains_user(self, user):
        return self.team.users.filter(pk = user.id).count() > 0
    
    def __unicode__(self):
        return unicode(self.project) + u' // ' + unicode(self.team)
    
    class Meta:
        unique_together = ('project', 'team')
