import logging

from rest_framework import permissions, viewsets

from .models import LDAPIntegrationAdapter
from .serializers import LDAPIntegrationSerializer

log = logging.getLogger(__name__)

INTEGRATION_NAME = 'ldap_integration'
MODEL_NAME = 'integration_ldap.LDAPIntegrationAdapter'


class LDAPAdapterAPI(viewsets.ModelViewSet):
    queryset = LDAPIntegrationAdapter.objects.none()  # Required for DjangoModelPermissions
    serializer_class = LDAPIntegrationSerializer

    permission_classes = (permissions.IsAuthenticated,
                          permissions.IsAdminUser,)

    def get_queryset(self):
        return LDAPIntegrationAdapter.objects.all()

