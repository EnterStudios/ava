import logging

from rest_framework import permissions, status
from rest_framework import viewsets
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import permission_classes
from rest_framework.views import APIView

from ava_core.abstract.permissions import IsAdminOrOwner, IsUpdateDenied, IsFish, IsOwner, IsAdminOrUpdateDenied, \
    IsAdminOrDeleteDenied
from .models import Question, Suspicious, ReportResponse
from .serializers import QuestionSerializer, SuspiciousSerializer, ReportResponseSerializer

log = logging.getLogger(__name__)


class QuestionAPI(viewsets.ModelViewSet):
    queryset = Question.objects.none()  # Required for DjangoModelPermissions
    serializer_class = QuestionSerializer
    permission_classes = (permissions.IsAuthenticated,IsAdminOrUpdateDenied, IsAdminOrDeleteDenied)

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Question.objects.all()
        elif self.request.user.is_authenticated():
            return Question.objects.filter(owner=self.request.user)
        else:
            return Question.objects.none()

    def get_object(self):
        obj = get_object_or_404(self.get_queryset())
        self.check_object_permissions(self.request, obj)
        return obj

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class SuspiciousAPI(viewsets.ModelViewSet):
    queryset = Suspicious.objects.none()  # Required for DjangoModelPermissions
    serializer_class = SuspiciousSerializer
    permission_classes = (permissions.IsAuthenticated,IsAdminOrUpdateDenied, IsAdminOrDeleteDenied)

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Suspicious.objects.all()
        elif self.request.user.is_authenticated():
            return Suspicious.objects.filter(owner=self.request.user)
        else:
            return Suspicious.objects.none()

    def get_object(self):
        obj = get_object_or_404(self.get_queryset())
        self.check_object_permissions(self.request, obj)
        return obj

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ReportResponseAPI(viewsets.ModelViewSet):
    queryset = ReportResponse.objects.none()  # Required for DjangoModelPermissions
    serializer_class = ReportResponseSerializer
    permission_classes = (permissions.IsAuthenticated,IsAdminOrUpdateDenied, IsAdminOrDeleteDenied)

    def get_queryset(self):
        if self.request.user.is_superuser:
            return ReportResponse.objects.all()
        elif self.request.user.is_authenticated():
            return ReportResponse.objects.filter(owner=self.request.user)
        else:
            return ReportResponse.objects.none()

    def get_object(self):
        obj = get_object_or_404(self.get_queryset())
        self.check_object_permissions(self.request, obj)
        return obj


    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ReportFormDataAPI(APIView):
    @permission_classes([permissions.IsAuthenticated, ])
    def get(self, request):
        priority_options = Question.TYPE_PRIORITY

        form_data = {'form_data': {
            'priority_types': priority_options,
        }}

        return Response(form_data, status=status.HTTP_200_OK)
