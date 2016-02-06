import logging

from rest_framework import serializers

from .models import Question, Suspicious, ReportResponse

log = logging.getLogger(__name__)


class QuestionSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.email')
    is_resolved = serializers.ReadOnlyField()

    class Meta:
        model = Question
        fields = (
            'url', 'id', 'created', 'modified', 'owner', 'status_type', 'priority_type', 'description',
            'is_resolved')


class SuspiciousSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.email')
    is_resolved = serializers.ReadOnlyField()

    class Meta:
        model = Suspicious
        fields = (
            'url','id', 'created', 'modified', 'owner', 'status_type', 'priority_type', 'description',
            'is_resolved', 'suspicious_url', 'incident_date')


class ReportResponseSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.email')

    class Meta:
        model = ReportResponse
        fields = (
            'url','id', 'owner', 'message', 'parent_response', 'question')
