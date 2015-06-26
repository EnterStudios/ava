from django.shortcuts import get_object_or_404
from apps.ava_core_project.decorators import project_access_check
from apps.ava_core_project.models import Project


def create_test_access_check(url_token, access_level, view_func=None, login_url=None, raise_exception=True):
    def get_project(request):
        project_id = request.resolver_match.kwargs[url_token]
        if project_id:
            return get_object_or_404(Project, pk=project_id)
        return None

    return project_access_check(get_project=get_project,
                                access_level=access_level,
                                view_func=view_func,
                                login_url=login_url,
                                raise_exception=raise_exception)
