import logging

from rest_framework import permissions
from rest_framework import viewsets

from ava_core.abstract.permissions import IsOwner, IsRetrieveOnly, IsUpdateDenied
from ava_core.evaluate.models import EvaluateResult
from ava_core.evaluate.serializer import EvaluateResultSerializer
from ava_core.report.models import Question, Suspicious
from ava_core.report.serializers import QuestionSerializer, SuspiciousSerializer
from .models import Friend, LearningHistory, ActivityLog, LearningProfile, ScoreCard, LearningQueue, People
from .serializers import FriendSerializer, LearningHistorySerializer, ActivityLogSerializer, \
    LearningProfileSerializer, ScoreCardSerializer, LearningQueueSerializer, PeopleSerializer

log = logging.getLogger(__name__)


class FriendAPI(viewsets.ModelViewSet):
    queryset = Friend.objects.none()  # Required for DjangoModelPermissions
    serializer_class = FriendSerializer
    permission_classes = (permissions.IsAuthenticated,
                          IsOwner,
                          IsUpdateDenied)

    def get_queryset(self):
        return Friend.objects.filter(owner=self.request.user)


class PeopleAPI(viewsets.ModelViewSet):
    queryset = People.objects.none()  # Required for DjangoModelPermissions
    serializer_class = PeopleSerializer
    permission_classes = (permissions.IsAuthenticated,
                          IsOwner,
                          IsUpdateDenied)

    def get_queryset(self):
        return People.objects.filter(owner=self.request.user)


class TestResultsAPI(viewsets.ModelViewSet):
    queryset = EvaluateResult.objects.none()  # Required for DjangoModelPermissions
    serializer_class = EvaluateResultSerializer
    permission_classes = (permissions.IsAuthenticated,
                          IsOwner,
                          IsUpdateDenied)

    def get_queryset(self):
        return EvaluateResult.objects.filter(target_profile__target=self.request.user)


class QuestionsAPI(viewsets.ModelViewSet):
    queryset = Question.objects.none()  # Required for DjangoModelPermissions
    serializer_class = QuestionSerializer
    permission_classes = (permissions.IsAuthenticated,
                          IsOwner,
                          IsUpdateDenied)

    def get_queryset(self):
        return Question.objects.filter(owner=self.request.user)


class SuspiciousAPI(viewsets.ModelViewSet):
    queryset = Suspicious.objects.none()  # Required for DjangoModelPermissions
    serializer_class = SuspiciousSerializer
    permission_classes = (permissions.IsAuthenticated,
                          IsOwner,
                          IsUpdateDenied)

    def get_queryset(self):
        return Suspicious.objects.filter(owner=self.request.user)


class LearningHistoryAPI(viewsets.ModelViewSet):
    queryset = LearningHistory.objects.none()  # Required for DjangoModelPermissions
    serializer_class = LearningHistorySerializer
    permission_classes = (permissions.IsAuthenticated,
                          IsOwner,
                          IsRetrieveOnly)

    def get_queryset(self):
        return LearningHistory.filter(owner=self.request.user)


class LearningQueueAPI(viewsets.ModelViewSet):
    queryset = LearningQueue.objects.none()  # Required for DjangoModelPermissions
    serializer_class = LearningQueueSerializer
    permission_classes = (permissions.IsAuthenticated,
                          IsOwner,
                          IsRetrieveOnly)

    def get_queryset(self):
        return LearningQueue.filter(owner=self.request.user)


class ActivityLogAPI(viewsets.ModelViewSet):
    queryset = ActivityLog.objects.none()  # Required for DjangoModelPermissions
    serializer_class = ActivityLogSerializer
    permission_classes = (permissions.IsAuthenticated,
                          IsOwner,
                          IsRetrieveOnly)

    def get_queryset(self):
        return ActivityLog.filter(owner=self.request.user)


class LearningProfileAPI(viewsets.ModelViewSet):
    queryset = LearningProfile.objects.none()  # Required for DjangoModelPermissions
    serializer_class = LearningProfileSerializer
    permission_classes = (permissions.IsAuthenticated,
                          IsOwner,
                          IsRetrieveOnly)

    def get_queryset(self):
        return LearningProfile.objects.filter(owner=self.request.user)


class ScoreCardAPI(viewsets.ModelViewSet):
    queryset = ScoreCard.objects.none()  # Required for DjangoModelPermissions
    serializer_class = ScoreCardSerializer
    permission_classes = (permissions.IsAuthenticated,
                          IsOwner,
                          IsRetrieveOnly)

    def get_queryset(self):
        return ScoreCard.objects.filter(owner=self.request.user)
