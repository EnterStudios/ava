# Rest Imports
import json

from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from rest_framework import permissions, viewsets, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
# Local Imports
from rest_framework_jwt.authentication import BaseJSONWebTokenAuthentication
from .serializers import RegisterSerializer, PasswordResetSerializer, \
    PasswordResetConfirmSerializer, PasswordChangeSerializer, UserSerializer
from logging import getLogger

log = getLogger(__name__)


# Implementation
class PasswordResetView(GenericAPIView):
    """
    Calls Django Auth PasswordResetForm save method.

    Accepts the following POST parameters: email
    Returns the success/fail message.
    """

    serializer_class = PasswordResetSerializer
    permission_classes = (permissions.AllowAny,)

    @csrf_exempt
    def post(self, request, *args, **kwargs):
        try:
            log.debug("POST on PasswordResetView")
            # Create a serializer with request.data
            serializer = self.get_serializer(data=request.data)
            try:
                serializer.is_valid(raise_exception=True)
            except Exception as e:
                log.debug("Exception raised when sending email :: " + str(e))
                return Response(
                    {"error": "An error has occurred :: " + str(e)},
                    status=status.HTTP_400_BAD_REQUEST
                )

            serializer.save()
        except Exception as e:
            log.debug("Exception raised when sending email :: " + str(e))
            return Response(
                {"error": "An error has occurred :: " + str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
        # Return the success message with OK HTTP status
        return Response(
            {"success": "Password reset e-mail has been sent"},
            status=status.HTTP_200_OK
        )


class PasswordResetConfirmView(GenericAPIView):
    """
    Password reset e-mail link is confirmed, therefore this resets the user's password.

    Accepts the following POST parameters: new_password1, new_password2
    Accepts the following Django URL arguments: token, uidb64
    Returns the success/fail message.
    """

    serializer_class = PasswordResetConfirmSerializer
    permission_classes = (permissions.AllowAny,)

    def post(self, request, **kwargs):

        uidb64 = kwargs.get('uidb64')
        token = kwargs.get('token')

        # log.debug("Request data :: " + str(request.data))

        serializer_data = {'uidb64': uidb64, 'token': token, 'new_password1': request.data['new_password1'],
                           'new_password2': request.data['new_password2']}

        # log.debug("Serializer data :: " + str(serializer_data))

        serializer = PasswordResetConfirmSerializer(data=serializer_data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"success": "Password has been reset with the new password."})


class PasswordChangeView(GenericAPIView):
    """
    Calls Django Auth SetPasswordForm save method.

    Accepts the following POST parameters: new_password1, new_password2
    Returns the success/fail message.
    """

    serializer_class = PasswordChangeSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"success": "New password has been saved."})


class RegisterView(GenericAPIView):
    """
    Accepts the credentials and creates a new user
    if user does not exist already
    """

    serializer_class = RegisterSerializer
    permission_classes = (permissions.AllowAny,)

    # TODO add signal to this that will send the verification email.....
    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        instance = serializer.save()

        # Set the password as the serializer save doesn't handle passwords
        instance.set_password(request.data['password'])

        # TODO might prefer to piggy back off the reset password functionality at the same time as email verification
        # instance.is_active = False
        instance.save()

        return Response({"success": "Registration successful, verification email has been sent"})


class JSONWebTokenAuthenticationPost(BaseJSONWebTokenAuthentication):
    def get_jwt_value(self, request):
        return request.POST.get('token')


@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated, ])
def get_user_from_token(request, **kwargs):
    log.debug("get_user_from_token :: entered")
    log.debug("get_user_from_token :: token = " + str(request.POST.get('token')))
    user = None
    try:
        user_jwt = JSONWebTokenAuthenticationPost().authenticate(request)
        log.debug("get_user_from_token :: user_jwt = " + str(user_jwt))
        if user_jwt is not None:
            log.debug("get_user_from_token :: user_jwt is not None")
            user = user_jwt[0]
    except User.DoesNotExist as e:
        pass

    user = UserSerializer(user, many=False, context={'request': request}).data

    user_json = json.dumps(user)

    log.debug("user_json = " + str(user_json))

    form_data = {'user': user_json}

    return Response(form_data, status=status.HTTP_200_OK)
