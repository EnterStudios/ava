from django.core.exceptions import PermissionDenied
from django.http.response import Http404
from django.shortcuts import get_object_or_404
from apps.ava_core.decorators import access_check
from apps.ava_core_project.models import Project


def project_access_check(get_project, access_level, view_func=None, login_url=None, raise_exception=True):
    
    def check_project_access(request):
        # Get the project.
        project = get_project(request)
        if not project:
            raise Http404
        # Check if the user has been authenticated.
        if not request.user.is_authenticated():
            return False
        # Check if the user has the requested access to the project.
        if project.user_has_access(request.user, access_level):
            return True
        # Check if an exception should be raised.
        if raise_exception:
            raise PermissionDenied
        # User doesn't have the correct rights.
        return False
    
    return access_check(test_func=check_project_access,
                        view_func=view_func,
                        login_url=login_url)


def project_access_required(access_level, view_func=None, login_url=None, raise_exception=True):
    
    def get_project(request):
        project_id = request.resolver_match.kwargs['pk']
        if project_id:
            return get_object_or_404(Project, pk=project_id)
        return None
    
    return project_access_check(get_project=get_project,
                                access_level=access_level,
                                view_func=view_func,
                                login_url=login_url,
                                raise_exception=raise_exception)
