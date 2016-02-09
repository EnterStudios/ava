from rest_framework import serializers

from .models import GoogleGatherHistory


class GoogleGatherHistorySerializer(serializers.ModelSerializer):
    created = serializers.ReadOnlyField()
    next_scheduled = serializers.ReadOnlyField()

    class Meta:
        model = GoogleGatherHistory
        fields = (
            'id', 'import_status', 'created', 'message', 'no_people', 'no_groups',
            'no_identifiers', 'integration',
            'next_scheduled')
