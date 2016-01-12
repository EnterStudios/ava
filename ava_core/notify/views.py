import logging

from rest_framework import permissions
from rest_framework import viewsets

from ava_core.abstract.permissions import IsAdminOrReadOnly
from .models import NotificationEmail
from .serializers import NotificationEmailSerializer

log = logging.getLogger(__name__)


class NotificationEmailAPI(viewsets.ModelViewSet):
    queryset = NotificationEmail.objects.none()  # Required for DjangoModelPermissions
    serializer_class = NotificationEmailSerializer
    permission_classes = (permissions.IsAuthenticated,
                          permissions.IsAdminUser)

    def get_queryset(self):
        return NotificationEmail.objects.all()
