import logging

from rest_framework import serializers

from .models import Question, Suspicious, ReportResponse

log = logging.getLogger(__name__)


class QuestionSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.email')
    is_resolved = serializers.ReadOnlyField()

    class Meta:
        model = Question
        fields = (
            'id', 'created', 'modified', 'owner', 'status_type', 'priority_type', 'description',
            'is_resolved')


class SuspiciousSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.email')
    is_resolved = serializers.ReadOnlyField()

    class Meta:
        model = Suspicious
        fields = (
            'id', 'created', 'modified', 'owner', 'status_type', 'priority_type', 'description',
            'is_resolved', 'url', 'incident_date')


class ReportResponseSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.email')

    class Meta:
        model = ReportResponse
        fields = (
            'id', 'owner', 'message', 'parent_response', 'question')
