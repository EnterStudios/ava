import logging

from rest_framework import serializers

from .models import NotificationEmail

log = logging.getLogger(__name__)


class NotificationEmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = NotificationEmail
        fields = ('id', 'name', 'notification_type', 'subject', 'body')
