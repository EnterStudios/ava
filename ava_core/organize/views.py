import logging

from rest_framework import permissions
from rest_framework import viewsets

from ava_core.abstract.permissions import IsAdminOrOwner, IsAdminOrDeleteDenied, IsRetrieveOnly, IsAccessDenied, \
    IsCreateDenied, IsUpdateDenied, IsDeleteDenied
from .models import PersonIdentifier, Person, Group, GroupIdentifier, PersonAttribute, PersonIdentifierAttribute, \
    GroupIdentifierAttribute, PersonIdentifierReport, GroupReport
from .serializers import PersonSerializer, PersonIdentifierSerializer, GroupSerializer, GroupIdentifierSerializer, \
    PersonAttributeSerializer, PersonIdentifierAttributeSerializer, GroupIdentifierAttributeSerializer, \
    PersonIdentifierReportSerializer, GroupReportSerializer

log = logging.getLogger(__name__)


class PersonAPI(viewsets.ModelViewSet):
    queryset = Person.objects.none()  # Required for DjangoModelPermissions
    serializer_class = PersonSerializer
    permission_classes = (permissions.IsAuthenticated,
                          IsAdminOrOwner,
                          IsRetrieveOnly)

    def get_queryset(self):
        return Person.objects.all()


class PersonIdentifierAPI(viewsets.ModelViewSet):
    queryset = PersonIdentifier.objects.none()  # Required for DjangoModelPermissions
    serializer_class = PersonIdentifierSerializer

    permission_classes = (IsAccessDenied,)

    def get_queryset(self):
        return PersonIdentifier.objects.all()


class GroupAPI(viewsets.ModelViewSet):
    queryset = Group.objects.none()  # Required for DjangoModelPermissions
    serializer_class = GroupSerializer
    permission_classes = (permissions.IsAuthenticated,
                          permissions.IsAdminUser,
                          IsRetrieveOnly)

    def get_queryset(self):
        return Group.objects.all()


class GroupIdentifierAPI(viewsets.ModelViewSet):
    queryset = GroupIdentifier.objects.none()  # Required for DjangoModelPermissions
    serializer_class = GroupIdentifierSerializer
    permission_classes = (IsAccessDenied,)

    def get_queryset(self):
        return GroupIdentifier.objects.all()


class PersonAttributeAPI(viewsets.ModelViewSet):
    queryset = PersonAttribute.objects.none()  # Required for DjangoModelPermissions
    serializer_class = PersonAttributeSerializer
    permissions = (permissions.IsAuthenticated,
                   permissions.IsAdminUser,
                   IsCreateDenied,
                   IsDeleteDenied)

    def get_queryset(self):
        return PersonAttribute.objects.all()


class PersonIdentifierAttributeAPI(viewsets.ModelViewSet):
    queryset = PersonIdentifierAttribute.objects.none()  # Required for DjangoModelPermissions
    serializer_class = PersonIdentifierAttributeSerializer
    permission_classes = (permissions.IsAuthenticated,
                          permissions.IsAdminUser,
                          IsCreateDenied,
                          IsDeleteDenied)

    def get_queryset(self):
        return PersonIdentifierAttribute.objects.all()


class GroupIdentifierAttributeAPI(viewsets.ModelViewSet):
    queryset = GroupIdentifierAttribute.objects.none()  # Required for DjangoModelPermissions
    serializer_class = GroupIdentifierAttributeSerializer
    permission_classes = (permissions.IsAuthenticated,
                          permissions.IsAdminUser,
                          IsCreateDenied,
                          IsDeleteDenied)

    def get_queryset(self):
        return GroupIdentifierAttribute.objects.all()


class PersonIdentifierReportAPI(viewsets.ModelViewSet):
    queryset = PersonIdentifierReport.objects.none()  # Required for DjangoModelPermissions
    serializer_class = PersonIdentifierReportSerializer
    permissions = (permissions.IsAuthenticated,
                   IsAdminOrOwner,
                   IsAdminOrDeleteDenied,
                   IsUpdateDenied)

    def get_queryset(self):
        return PersonIdentifierReport.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class GroupReportAPI(viewsets.ModelViewSet):
    queryset = GroupReport.objects.none()  # Required for DjangoModelPermissions
    serializer_class = GroupReportSerializer
    permissions = (permissions.IsAuthenticated,
                   IsAdminOrOwner,
                   IsAdminOrDeleteDenied,
                   IsUpdateDenied)

    def get_queryset(self):
        return GroupReport.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
