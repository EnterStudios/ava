from django.core.exceptions import PermissionDenied
from ava.core.decorators import access_check
from ava.core_auth.models import UserRights


def system_admin_required(view_func=None, login_url=None, raise_exception=True):
    """
    Checks that the user has been authenticated and is a system administrator.
    :param login_url: A login URL that the user should be redirected to if they
                are not logged in or are not a system administrator.
    :param raise_exception: If set to True, a 403 error will be raised when the
                user is logged in but not a system administrator.
    """

    def check_user(request):
        # Check if the user has been authenticated.
        if not request.user.is_authenticated():
            return False
        # Check if the user is an administrator.
        if UserRights.get(request.user).is_admin:
            return True
        # Check if an exception should be raised.
        if raise_exception:
            raise PermissionDenied
        # User doesn't have the correct rights.
        return False

    return access_check(test_func=check_user,
                        view_func=view_func,
                        login_url=login_url)
