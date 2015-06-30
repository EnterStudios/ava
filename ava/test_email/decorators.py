from django.shortcuts import get_object_or_404
from ava.core_project.decorators import project_access_check
from ava.test_email.models import EmailTest


def email_test_access_check(access_level, view_func=None, login_url=None, raise_exception=True):
    def get_project(request):
        test_id = request.resolver_match.kwargs['pk']
        if test_id:
            email_test = get_object_or_404(EmailTest, pk=test_id)
            return email_test.project
        return None

    return project_access_check(get_project=get_project,
                                access_level=access_level,
                                view_func=view_func,
                                login_url=login_url,
                                raise_exception=raise_exception)
