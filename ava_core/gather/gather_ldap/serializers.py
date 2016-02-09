from rest_framework import serializers

from .models import LDAPGatherHistory


class LDAPGatherHistorySerializer(serializers.ModelSerializer):
    created = serializers.ReadOnlyField()
    next_scheduled = serializers.ReadOnlyField()


    class Meta:
        model = LDAPGatherHistory
        fields = (
            'id', 'import_status', 'created', 'message', 'no_people', 'no_groups',
            'no_identifiers', 'integration',
            'next_scheduled')
