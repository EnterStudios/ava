import logging

from rest_framework import permissions
from rest_framework import viewsets

from ava_core.abstract.permissions import IsAdminOrReadOnly
from .models import Achievement
from .serializers import AchievementSerializer

log = logging.getLogger(__name__)


class AchievementAPI(viewsets.ModelViewSet):
    queryset = Achievement.objects.none()  # Required for DjangoModelPermissions
    serializer_class = AchievementSerializer
    permission_classes = (permissions.IsAuthenticated,
                          IsAdminOrReadOnly,
                          )

    def get_queryset(self):
        return Achievement.objects.all()
