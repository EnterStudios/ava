import logging

from ava_core.abstract.permissions import IsRetrieveOnly
from rest_framework import permissions
from rest_framework import viewsets

from .models import Achievement
from .serializers import AchievementSerializer

log = logging.getLogger(__name__)


class AchievementAPI(viewsets.ModelViewSet):
    queryset = Achievement.objects.none()  # Required for DjangoModelPermissions
    serializer_class = AchievementSerializer
    permission_classes = (permissions.IsAuthenticated,
                          permissions.IsAdminUser,
                          IsRetrieveOnly)

    def get_queryset(self):
        return Achievement.objects.all()
