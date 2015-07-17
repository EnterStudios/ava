import logging
import os

import django.views.generic
import django.core.exceptions
import django.http
from django.conf import settings
from django.core.urlresolvers import reverse

import oauth2client.client

log = logging.getLogger(__name__)


def build_flow():
    """Build and return a OAuth2WebServerFlow object."""
    if settings.GOOGLE_OAUTH2_CLIENT_ID is None or settings.GOOGLE_OAUTH2_CLIENT_SECRET is None:
        raise django.core.exceptions.ImproperlyConfigured(
            'Google OAuth2 Credentials have not been configured.'
        )
    flow = oauth2client.client.OAuth2WebServerFlow(
        client_id=settings.GOOGLE_OAUTH2_CLIENT_ID,
        client_secret=settings.GOOGLE_OAUTH2_CLIENT_SECRET,
        scope=[
            'https://www.googleapis.com/auth/admin.directory.user.readonly',
            'https://www.googleapis.com/auth/admin.directory.group.readonly',
            'https://www.googleapis.com/auth/admin.directory.group.member.readonly',
            'https://www.googleapis.com/auth/admin.directory.orgunit.readonly',
            'https://www.googleapis.com/auth/admin.directory.user.alias.readonly'
        ],
        user_agent='ava/0.1',

        redirect_uri=settings.GOOGLE_OAUTH2_REDIRECT_URL,

    )
    return flow


def store_credential_in_session(request, credential):
    request.session['google_oauth2_credential'] = credential.to_json()


def retrieve_credential_from_session(request):
    credential_json = request.session.get('google_oauth2_credential')
    if credential_json is None:
        return None
    credential = oauth2client.client.OAuth2Credentials.from_json(credential_json)
    return credential


class RedirectToGoogleLogin(django.views.generic.View):
    def get(self, request):

        # bypass the google auth flow if using the mock local version

        if os.environ.get('USE_MOCK_GOOGLE'):
            return django.http.HttpResponseRedirect(reverse('google-import'))
        else:
            flow = build_flow()
            # Build the URI that we send the client browser to.
            authorize_url = flow.step1_get_authorize_url()
            # Send the client web browser to the authorize_url
            return django.http.HttpResponseRedirect(authorize_url)


class GoogleOAuth2Callback(django.views.generic.View):
    def get(self, request):
        # The web browser has just completed the google auth stuff and has been
        # sent back here for the next step.

        # First: rebuild the flow object.
        flow = build_flow()
        # now we (the AVA app server) sends a web request directly to Google asking
        # for OAuth2Credentials.
        credential = flow.step2_exchange(request.REQUEST)
        # One we have them, we store them in the session, since we don't need to keep
        # them very long.
        store_credential_in_session(request, credential)
        # And send the user to the next step, wherever that might be. This URL
        # should be updated for the next step in the process.
        return django.http.HttpResponseRedirect(reverse('google-import'))


class Main(django.views.generic.TemplateView):
    template_name = 'google_auth/main.html'
