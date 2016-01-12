import logging
import os

import django.core.exceptions
import django.http
import django.views.generic
import oauth2client.client
from django.conf import settings
from rest_framework import permissions
from rest_framework import status, viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from ava_core.integration.integration_abstract.utils import store_credential_in_database, \
    store_temporary_flow_data_in_database, retrieve_temporary_flow_data_from_database, \
    remove_temporary_flow_data_from_database
from .models import GoogleIntegrationAdapter
from .serializers import GoogleIntegrationSerializer

log = logging.getLogger(__name__)

INTEGRATION_NAME = 'google_integration'
MODEL_NAME = 'integration_google.GoogleIntegrationAdapter'
TEMP_MODEL_NAME = 'integration_google.GoogleAuthorizationStore'


def build_flow():
    """Build and return a OAuth2WebServerFlow object."""
    if settings.GOOGLE_OAUTH2_CLIENT_ID is None or settings.GOOGLE_OAUTH2_CLIENT_SECRET is None:
        raise django.core.exceptions.ImproperlyConfigured(
            'Google OAuth2 Credentials have not been configured.'
        )
    flow = oauth2client.client.OAuth2WebServerFlow(
        client_id=settings.GOOGLE_OAUTH2_CLIENT_ID,
        client_secret=settings.GOOGLE_OAUTH2_CLIENT_SECRET,
        scope=settings.GOOGLE_OAUTH2_SCOPE,
        user_agent='ava/0.1',

        redirect_uri=settings.GOOGLE_OAUTH2_REDIRECT_URL,

    )
    return flow


# API Declarations

@api_view(['GET'])
# Not sure about this permission set. This function is called by the 3rd party so can't pass any auth checks
# Not considered harmful so ok to allow all on this
@permission_classes([permissions.AllowAny, ])
def callback(request):
    # The web browser has just completed the integration_google auth stuff and has been
    # sent back here for the next step.
    log.debug("CallbackAPI:GET - Reached GET request")
    # First: rebuild the flow object.
    flow = build_flow()
    log.debug("CallbackAPI:GET - Flow client id:: " + flow.client_id)
    # now we (the AVA app server) sends a web request directly to Google asking
    # for OAuth2Credentials.
    log.debug("CallbackAPI:GET - Attempting credential exchange")
    code = request.query_params['code']
    log.debug("CallbackAPI:GET - Request Code:: " + code)
    credential = flow.step2_exchange(code)
    # One we have them, we store them in the session, since we don't need to keep
    # them very long.
    log.debug("CallbackAPI:GET - Attempting to store credential in session")

    integration_id = retrieve_temporary_flow_data_from_database(TEMP_MODEL_NAME)

    store_credential_in_database(MODEL_NAME, integration_id, credential)

    log.debug("CallbackAPI:GET - Access Token ::" + credential.access_token)
    log.debug("CallbackAPI:GET - Refresh Token ::" + str(credential.refresh_token))

    remove_temporary_flow_data_from_database(TEMP_MODEL_NAME, integration_id)

    # And send the user to the next step, wherever that might be. This URL
    # should be updated for the next step in the process.
    return Response({"message": "Completed callback"}, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated, ])
def redirect(request, **kwargs):
    # bypass the integration_google auth flow if using the mock local version
    log.debug("RedirectAPI:GET - Reached GET request")

    if os.environ.get('USE_MOCK_GOOGLE'):

        log.debug("RedirectAPI:GET - USE_MOCK_GOOGLE found - switching to local import")
        request.session['integration_id'] = None
        return Response({"message": "USE_MOCK_GOOGLE found. Aborting OAUTH"}, status=status.HTTP_200_OK)
    else:
        log.debug("RedirectAPI:GET - Proceeding with live import")

        pk = kwargs.get('pk')
        log.debug("RedirectAPI:GET - Getting PK from url :: " + pk)

        store_temporary_flow_data_in_database(TEMP_MODEL_NAME, pk)

        flow = build_flow()
        # Build the URI that we send the client browser to.
        log.debug("RedirectAPI:GET - Asking for authorize url")
        authorize_url = flow.step1_get_authorize_url()
        # Send the client web browser to the authorize_url
        log.debug("RedirectAPI:GET - Returning authorise URL in response :: " + authorize_url)
        return Response({"authorize_url": authorize_url}, status=status.HTTP_200_OK)


class GoogleAdapterAPI(viewsets.ModelViewSet):
    queryset = GoogleIntegrationAdapter.objects.none()  # Required for DjangoModelPermissions
    serializer_class = GoogleIntegrationSerializer

    permission_classes = (permissions.IsAuthenticated,
                          permissions.IsAdminUser,)

    def get_queryset(self):
        return GoogleIntegrationAdapter.objects.all()

