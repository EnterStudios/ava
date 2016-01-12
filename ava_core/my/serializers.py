import logging

from rest_framework import serializers

from ava_core.game.serializers import AchievementSerializer
from ava_core.learn.serializers import RoleSerializer
from .models import LearningHistory, Friend, ActivityLog, ScoreCard, LearningProfile, LearningQueue

log = logging.getLogger(__name__)


class LearningHistorySerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.email')

    class Meta:
        model = LearningHistory
        fields = ('id', 'owner', 'created', 'modified', 'score', 'module', 'completed')


class LearningQueueSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.email')

    class Meta:
        model = LearningQueue
        fields = ('id', 'owner', 'module')


class PeopleSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.email')
    person = serializers.PrimaryKeyRelatedField(read_only=True, many=True)

    class Meta:
        model = LearningQueue
        fields = ('id', 'owner', 'person')


class LearningProfileSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.email')
    role = RoleSerializer(read_only=True, many=True)
    profile_history = LearningHistorySerializer(read_only=True, many=True)
    profile_queue = LearningQueueSerializer(read_only=True, many=True)

    class Meta:
        model = LearningProfile
        fields = ('id', 'owner', 'role')


class FriendSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.email')

    class Meta:
        model = Friend
        fields = ('id', 'owner', 'created', 'modified', 'friend')


class ActivityLogSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.email')

    class Meta:
        model = ActivityLog
        fields = ('id', 'owner', 'created', 'modified', 'log_entry')


class ScoreCardSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.email')
    achievement = AchievementSerializer(read_only=True, many=True)

    class Meta:
        model = ScoreCard
        fields = ('id', 'owner', 'created', 'modified', 'achievement')
