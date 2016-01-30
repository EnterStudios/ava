import logging

from ava_core.abstract.models import TimeStampedModel
from ava_core.game.models import Achievement
from ava_core.learn.models import Role, Module
from django.conf import settings
from django.db import models

from ava_core.organize.models import Person

log = logging.getLogger(__name__)


class LearningHistory(TimeStampedModel):
    owner = models.ForeignKey(to=settings.USER_MODEL, null=False)
    module = models.ForeignKey(to=Module, null=False, related_name='history_module')
    score = models.IntegerField()
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.owner + " : " + self.module.name
    
class People(TimeStampedModel):
    owner = models.ForeignKey(to=settings.USER_MODEL, null=False)
    person = models.ForeignKey(to=Person, null=False)

    def __str__(self):
        return self.owner + " : " + self.person


class LearningQueue(TimeStampedModel):
    owner = models.ForeignKey(to=settings.USER_MODEL, null=False)
    module = models.ForeignKey(to=Module, null=False, related_name='queue_module')

    def __str__(self):
        return self.owner


class Friend(TimeStampedModel):
    owner = models.ForeignKey(to=settings.USER_MODEL, null=False, related_name='friend_owner')
    friend = models.ManyToManyField(to=settings.USER_MODEL, related_name='friend')

    def __str__(self):
        return self.owner + " : " + self.friend.email


class ActivityLog(TimeStampedModel):
    owner = models.ForeignKey(to=settings.USER_MODEL, null=False)
    log_entry = models.CharField(max_length=400)

    def __str__(self):
        return self.owner + " : " + self.log_entry


class ScoreCard(TimeStampedModel):
    owner = models.ForeignKey(to=settings.USER_MODEL, null=False)
    achievement = models.ForeignKey(to=Achievement, null=False, related_name='user_achievements')

    def __str__(self):
        return self.owner + " : " + self.achievement


class LearningProfile(TimeStampedModel):
    owner = models.ForeignKey(to=settings.USER_MODEL, null=False)
    role = models.ForeignKey(to=Role, null=False, related_name='profile_role')
    learning_history = models.ForeignKey(to=LearningHistory, related_name='profile_history')
    learning_queue = models.ForeignKey(to=LearningQueue, related_name='profile_queue')

    def __str__(self):
        return self.owner + " : " + self.role
