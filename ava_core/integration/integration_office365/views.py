import json
import logging
import os

from django.conf import settings
from rest_framework import permissions
from rest_framework import status, viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from ava_core.integration.integration_abstract.utils import store_credential_in_database, \
    store_temporary_flow_data_in_database, retrieve_temporary_flow_data_from_database, \
    remove_temporary_flow_data_from_database
from ava_core.integration.integration_office365.utils import get_token_from_code, get_user_info_from_token, \
    get_signin_url
from .models import Office365IntegrationAdapter
from .serializers import Office365IntegrationSerializer

log = logging.getLogger(__name__)

INTEGRATION_NAME = 'office365_integration'
MODEL_NAME = 'integration_google.Office365IntegrationAdapter'
TEMP_MODEL_NAME = 'integration_google.Office365AuthorizationStore'


# API Declarations

@api_view(['GET'])
# Not sure about this permission set. This function is called by the 3rd party so can't pass any auth checks
# Not considered harmful so ok to allow all on this
@permission_classes([permissions.AllowAny, ])
def callback(request):
    # The web browser has just completed the integration_google auth stuff and has been
    # sent back here for the next step.
    log.debug("CallbackAPI:GET - Reached GET request")

    auth_code = request.GET['code']

    token = get_token_from_code(auth_code)

    access_token = token['access_token']

    user_info = get_user_info_from_token(token['id_token'])

    log.debug("CallbackAPI:GET - Request Code:: " + auth_code)

    log.debug("CallbackAPI:GET - Attempting to store credential in session")

    integration_id = retrieve_temporary_flow_data_from_database(TEMP_MODEL_NAME)

    credential = {}
    credential['access_token'] = access_token
    credential['alias'] = user_info['upn'].split('@')[0]
    credential['emailAddress'] = user_info['upn']
    credential['showSuccess'] = 'false'
    credential['showError'] = 'false'
    credential['pageRefresh'] = 'true'

    json_credential = json.dumps(credential)

    store_credential_in_database(MODEL_NAME, integration_id, json_credential)

    log.debug("CallbackAPI:GET - Access Token ::" + credential.access_token)
    # log.debug("CallbackAPI:GET - Refresh Token ::" + str(credential.refresh_token))

    remove_temporary_flow_data_from_database(TEMP_MODEL_NAME, integration_id)

    # And send the user to the next step, wherever that might be. This URL
    # should be updated for the next step in the process.
    return Response({"message": "Completed callback"}, status=status.HTTP_200_OK)


# This is the route that is the redirect URI of your registered
# Azure application. An authorization code is returned here that
# is swapped for an access token in auth_helper.
@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated, ])
def redirect(request, **kwargs):
    # bypass the integration_google auth flow if using the mock local version
    log.debug("RedirectAPI:GET - Reached GET request")

    if os.environ.get('USE_MOCK_OFFICE365'):

        log.debug("RedirectAPI:GET - USE_MOCK_OFFICE365 found - switching to local import")
        request.session['integration_id'] = None
        return Response({"message": "USE_MOCK_OFFICE365 found. Aborting OAUTH"}, status=status.HTTP_200_OK)
    else:
        log.debug("RedirectAPI:GET - Proceeding with live import")

        pk = kwargs.get('pk')
        log.debug("RedirectAPI:GET - Getting PK from url :: " + pk)

        store_temporary_flow_data_in_database(TEMP_MODEL_NAME, pk)

        sign_in_url = get_signin_url()

        # Build the URI that we send the client browser to.
        log.debug("RedirectAPI:GET - Asking for authorize url")
        authorize_url = sign_in_url
        # Send the client web browser to the authorize_url
        log.debug("RedirectAPI:GET - Returning authorise URL in response :: " + authorize_url)
        return Response({"authorize_url": authorize_url}, status=status.HTTP_200_OK)


class Office365AdapterAPI(viewsets.ModelViewSet):
    queryset = Office365IntegrationAdapter.objects.none()  # Required for DjangoModelPermissions
    serializer_class = Office365IntegrationSerializer

    permission_classes = (permissions.IsAuthenticated,
                          permissions.IsAdminUser,)

    def get_queryset(self):
        return Office365IntegrationAdapter.objects.all()
