from rest_framework import serializers

from ava_core.gather.gather_ldap.models import LDAPGatherHistory
from ava_core.integration.integration_ldap.models import LDAPIntegrationAdapter


class LDAPGatherHistorySerializer(serializers.ModelSerializer):
    created = serializers.ReadOnlyField()
    next_scheduled = serializers.ReadOnlyField()

    class Meta:
        model = LDAPGatherHistory
        fields = (
            'id', 'import_status', 'created', 'message', 'no_people', 'no_groups',
            'no_identifiers', 'next_scheduled')


class LDAPIntegrationSerializer(serializers.ModelSerializer):
    ldap_integration_history = LDAPGatherHistorySerializer(read_only=True, many=True)

    class Meta:
        model = LDAPIntegrationAdapter
        fields = ('id', 'name', 'dump_dn', 'server', 'ldap_password', 'ldap_user', 'ldap_integration_history')
