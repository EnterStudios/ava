import logging

from rest_framework import permissions, status
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import permission_classes
from rest_framework.views import APIView

from ava_core.abstract.permissions import IsAdminOrOwner, IsAdminOrDeleteDenied, IsUpdateDenied
from .models import Question, Suspicious, ReportResponse
from .serializers import QuestionSerializer, SuspiciousSerializer, ReportResponseSerializer

log = logging.getLogger(__name__)


class QuestionAPI(viewsets.ModelViewSet):
    queryset = Question.objects.none()  # Required for DjangoModelPermissions
    serializer_class = QuestionSerializer
    permissions = (permissions.IsAuthenticated,
                   IsAdminOrOwner,
                   IsAdminOrDeleteDenied,
                   IsUpdateDenied)

    def get_queryset(self):
        return Question.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class SuspiciousAPI(viewsets.ModelViewSet):
    queryset = Suspicious.objects.none()  # Required for DjangoModelPermissions
    serializer_class = SuspiciousSerializer
    permissions = (permissions.IsAuthenticated,
                   IsAdminOrOwner,
                   IsAdminOrDeleteDenied,
                   IsUpdateDenied)

    def get_queryset(self):
        return Suspicious.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ReportResponseAPI(viewsets.ModelViewSet):
    queryset = ReportResponse.objects.none()  # Required for DjangoModelPermissions
    serializer_class = ReportResponseSerializer
    permissions = (permissions.IsAuthenticated,
                   IsAdminOrOwner,
                   IsAdminOrDeleteDenied,
                   IsUpdateDenied)

    def get_queryset(self):
        return ReportResponse.objects.all()

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
