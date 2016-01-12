import logging

from rest_framework import serializers

from .models import IntegrationAdapter

log = logging.getLogger(__name__)


class IntegrationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = IntegrationAdapter
        fields = ('url', 'credential')

