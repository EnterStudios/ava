# Rest Imports
from rest_framework import permissions, status, viewsets
from rest_framework.decorators import permission_classes
from rest_framework.response import Response
from rest_framework.views import APIView
# Python Imports
from logging import getLogger
# Local Imports
from ava_core.abstract.permissions import IsAdminOrOwner, IsDeleteDenied, IsRetrieveOnly
from ava_core.evaluate.models import EvaluateController, EvaluateSender, EvaluateResult, EvaluateTest, \
    EvaluateTemplate
from ava_core.evaluate.serializers import EvaluateControllerSerializer, EvaluateResultSerializer, \
    EvaluateSenderSerializer, EvaluateTestSerializer, EvaluateTemplateSerializer, \
    EvaluateSimpleTargetSerializer
# Logging
from ava_core.organize.models import Person

logger = getLogger(__name__)


# Implementation
class EvaluateControllerAPI(viewsets.ModelViewSet):
    queryset = EvaluateController.objects.all()
    serializer_class = EvaluateControllerSerializer
    permission_classes = (permissions.IsAuthenticated,
                          permissions.IsAdminUser,
                          IsDeleteDenied)


class EvaluateResultAPI(viewsets.ModelViewSet):
    queryset = EvaluateResult.objects.all()
    serializer_class = EvaluateResultSerializer
    permission_classes = (permissions.IsAuthenticated,
                          IsAdminOrOwner,
                          IsRetrieveOnly)


class EvaluateSenderAPI(viewsets.ModelViewSet):
    queryset = EvaluateSender.objects.none()
    serializer_class = EvaluateSenderSerializer
    permission_classes = (permissions.IsAuthenticated,
                          permissions.IsAdminUser,
                          IsDeleteDenied)

    def get_queryset(self):
        return EvaluateSender.objects.filter(hidden=False)


class EvaluateTestAPI(viewsets.ModelViewSet):
    queryset = EvaluateTest.objects.all()
    serializer_class = EvaluateTestSerializer
    permission_classes = (permissions.IsAuthenticated,
                          permissions.IsAdminUser,
                          IsRetrieveOnly)


class EvaluateTemplateAPI(viewsets.ModelViewSet):
    queryset = EvaluateTemplate.objects.none()
    serializer_class = EvaluateTemplateSerializer
    permission_classes = (permissions.IsAuthenticated,
                          permissions.IsAdminUser,
                          IsDeleteDenied )

    def get_queryset(self):
        return EvaluateTemplate.objects.filter(hidden=False)


class EvaluateReturnAPI(viewsets.ViewSet):
    permission_classes = (permissions.AllowAny,)

    def list(self, request):
        logger.debug('Function called'
                     ' - EvaluateReturnAPI::list')
        return_status = status.HTTP_400_BAD_REQUEST

        token = request.query_params.get('token', None)
        if token is not None:
            target_profile = EvaluateTest.objects.get(token__exact=token)
            if target_profile is not None:
                if target_profile.controller.status == EvaluateController.ACTIVE:
                    EvaluateResult.objects.create(target_profile=target_profile, result=EvaluateResult.FAIL)
                    return_status = status.HTTP_200_OK

        return Response(return_status)


class EvaluateControllerFormDataAPI(APIView):

    @permission_classes([permissions.IsAuthenticated, ])
    def get(self, request):
        template_queryset = EvaluateTemplate.objects.all()
        templates = EvaluateTemplateSerializer(template_queryset, many=True, context={'request': request}).data

        sender_queryset = EvaluateSender.objects.all()
        senders = EvaluateSenderSerializer(sender_queryset, many=True, context={'request': request}).data

        expiry_options = EvaluateController.TYPE_EXPIRY
        status_options = EvaluateController.TYPE_STATUS
        schedule_options = EvaluateController.TYPE_SCHEDULE

        # TODO THIS IS HORRIBLE AND WILL NOT SCALE.
        people_queryset = Person.objects.all()
        people = EvaluateSimpleTargetSerializer(people_queryset, many=True, context={'request': request}).data

        form_data = {'form_data': {
            'templates': templates,
            'senders': senders,
            'targets': people,
            'expiry_types': expiry_options,
            'status_types': status_options,
            'schedule_types': schedule_options,
        }}

        return Response(form_data, status=status.HTTP_200_OK)
