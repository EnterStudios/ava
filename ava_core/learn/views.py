import logging

from rest_framework import permissions
from rest_framework import viewsets, status
from rest_framework.decorators import permission_classes
from rest_framework.response import Response
from rest_framework.views import APIView

from ava_core.abstract.permissions import IsAdminOrReadOnly
from .models import Role, Path, Module
from .serializers import RoleSerializer, PathSerializer, ModuleSerializer

log = logging.getLogger(__name__)


class RoleAPI(viewsets.ModelViewSet):
    queryset = Role.objects.none()  # Required for DjangoModelPermissions
    serializer_class = RoleSerializer
    permission_classes = (permissions.IsAuthenticated,
                          permissions.IsAdminUser)

    def get_queryset(self):
        return Role.objects.all()


class PathAPI(viewsets.ModelViewSet):
    queryset = Path.objects.none()  # Required for DjangoModelPermissions
    serializer_class = PathSerializer
    permission_classes = (permissions.IsAuthenticated,
                          permissions.IsAdminUser)

    def get_queryset(self):
        return Path.objects.all()


class ModuleAPI(viewsets.ModelViewSet):
    queryset = Module.objects.none()  # Required for DjangoModelPermissions
    serializer_class = ModuleSerializer
    permission_classes = (permissions.IsAuthenticated,
                          permissions.IsAdminUser)

    def get_queryset(self):
        return Module.objects.all()


class PathFormDataAPI(APIView):

    @permission_classes([permissions.IsAuthenticated, ])
    def get(self, request):
        module_queryset = Module.objects.all()
        modules = ModuleSerializer(module_queryset, many=True, context={'request': request}).data
        path_queryset = Path.objects.all()
        paths = PathSerializer(path_queryset, many=True, context={'request': request}).data
        role_queryset = Role.objects.all()
        roles = RoleSerializer(role_queryset, many=True, context={'request': request}).data

        form_data = {'form_data': {'modules': modules, 'paths': paths, 'roles': roles}}

        return Response(form_data, status=status.HTTP_200_OK)
