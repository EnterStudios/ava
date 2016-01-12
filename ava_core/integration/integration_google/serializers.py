from rest_framework import serializers
from rest_framework.fields import ReadOnlyField

from ava_core.gather.gather_google.models import GoogleGatherHistory
from .models import GoogleIntegrationAdapter


class GoogleGatherHistorySerializer(serializers.ModelSerializer):

    class Meta:
        model = GoogleGatherHistory
        fields = (
            'id', 'import_status', 'created', 'message', 'no_people', 'no_groups',
            'no_identifiers',
            'next_scheduled')

class GoogleIntegrationSerializer(serializers.ModelSerializer):
    credential = ReadOnlyField()
    google_integration_history = GoogleGatherHistorySerializer(many=True, read_only=True)

    class Meta:
        model = GoogleIntegrationAdapter
        fields = ('id', 'name', 'description', 'domain', 'credential', 'google_integration_history')
