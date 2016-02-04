from rest_framework import serializers
from rest_framework.fields import ReadOnlyField

from ava_core.gather.gather_office365.models import Office365GatherHistory
from .models import Office365IntegrationAdapter


class Office365GatherHistorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Office365GatherHistory
        fields = (
            'id', 'import_status', 'created', 'message', 'no_people', 'no_groups',
            'no_identifiers',
            'next_scheduled')

class Office365IntegrationSerializer(serializers.ModelSerializer):
    credential = ReadOnlyField()
    office365_integration_history = Office365GatherHistorySerializer(many=True, read_only=True)

    class Meta:
        model = Office365IntegrationAdapter
        fields = ('id', 'name', 'description', 'domain', 'credential', 'office365_integration_history')
