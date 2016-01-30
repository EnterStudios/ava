import logging

from rest_framework import serializers

from .models import Achievement

log = logging.getLogger(__name__)


class AchievementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Achievement
        fields = ('id', 'name', 'description', 'score', 'icon_url')
