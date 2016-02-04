from rest_framework import serializers

from .models import Office365GatherHistory


class Office365GatherHistorySerializer(serializers.ModelSerializer):
    created = serializers.ReadOnlyField()
    next_scheduled = serializers.ReadOnlyField()

    class Meta:
        model = Office365GatherHistory
        fields = (
            'id', 'import_status', 'created', 'message', 'no_people', 'no_groups',
            'no_identifiers',
            'next_scheduled')
