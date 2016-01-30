import logging

from django.contrib.auth.middleware import get_user
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.utils.functional import SimpleLazyObject
from rest_framework.request import Request
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

log = logging.getLogger(__name__)


class AVARedirectionMiddleware(object):
    """Examine the request to see if the user needs to go somewhere else.

    Depending on various criteria, we may wish to redirect the user to
    somewhere else other than where they were trying to go. This
    middleware examines the request and either lets it fall through
    (by returning None) or it redirects the user to another URL.
    """

    def process_view(self, request, view_func, view_args, view_kwargs):
        # If no users exist: redirect to the create-superuser URL.
        create_first_user_uri = reverse('welcome-first-user')
        if (
                        not request.user.is_authenticated() and
                        not User.objects.exists() and
                    not request.path == create_first_user_uri
        ):
            log.info("No AVA users: redirecting to 'create_first_user_uri'.")
            return HttpResponseRedirect(create_first_user_uri)

        return None


def get_user_jwt(request):
    # log.debug("Authentication Middleware: get_user_jwt")
    user = get_user(request)
    # log.debug("Authentication Middleware: get_user_jwt :: user = " + str(user))
    if user.is_authenticated():
        # log.debug("Authentication Middleware: User is authenticated : returning ::" + str(user))
        return user
    try:
        user_jwt = JSONWebTokenAuthentication().authenticate(Request(request))
        # log.debug("Authentication Middleware: get_user_jwt :: user_jwt = " + str(user_jwt))
        if user_jwt is not None:
            # log.debug("Authentication Middleware: get_user_jwt :: user_jwt is not None")
            return user_jwt[0]
    except:
        pass

    # log.debug("Authentication Middleware: Reached end of get_user)jwt : returning ::" + str(user))
    return user



class AuthenticationMiddlewareJWT(object):
    def process_request(self, request):
        # log.debug("Authentication Middleware: running process_request")
        assert hasattr(request,
                       'session'), "The Django authentication middleware requires session middleware to be installed. Edit your MIDDLEWARE_CLASSES setting to insert 'django.contrib.sessions.middleware.SessionMiddleware'."
        # log.debug("Authentication Middleware: Attempting to set request.user")
        request.user = SimpleLazyObject(lambda: get_user_jwt(request))
        test = request.user.id
        # log.debug("Authentication Middleware :: " + str(request.user))



