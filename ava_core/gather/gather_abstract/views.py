# flake8: noqa
import logging

from django.conf import settings
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from ava_core.integration.integration_abstract.utils import retrieve_credential_from_database

log = logging.getLogger(__name__)


class GatherImportAPI(APIView):
    MODEL_NAME = ''
    DIRECTORY_INTERFACE = None
    PERSON_MODEL = 'organize.PersonIdentifier'
    GROUP_MODEL = 'organize.GroupIdentifier'
    IMPORT_DATA = {}

    def get(self, request, **kwargs):
        log.debug(str(self.__class__) + "::POST - Entered post ")

        if settings.GATHER_USE_LOCAL:
            credential = None
        else:

            pk = self.kwargs.get('pk')

            credential = retrieve_credential_from_database(self.MODEL_NAME, pk)

        log.debug(str(self.__class__) + "::POST -  Attempting data import")

        self.IMPORT_DATA = self.DIRECTORY_INTERFACE.import_directory(credential)

        # parse and store the users
        log.debug(str(self.__class__) + "::POST - Attempting user import")
        self.import_users_from_json(self.IMPORT_DATA['users'])

        log.debug(str(self.__class__) + "::POST - Attempting group import")
        self.import_groups_from_json(self.IMPORT_DATA['groups'])

        return Response({'message': "Import complete"}, status=status.HTTP_200_OK)

    def import_users_from_json(self, users):
        log.debug(str(self.__class__) + "::import_users_from_json - Entered method")
        pass

    def import_groups_from_json(self, groups):
        log.debug(str(self.__class__) + "::import_groups_from_json -  Entered method")
        pass


