from django.shortcuts import get_object_or_404
from apps.ava_core_project.decorators import project_access_check
from apps.ava_test_twitter.models import TwitterTest


def twitter_test_access_check(access_level, view_func=None, login_url=None, raise_exception=True):
    
    def get_project(request):
        test_id = request.resolver_match.kwargs['pk']
        if test_id:
            twitter_test = get_object_or_404(TwitterTest, pk=test_id)
            return twitter_test.project
        return None
    
    return project_access_check(get_project=get_project,
                                access_level=access_level,
                                view_func=view_func,
                                login_url=login_url,
                                raise_exception=raise_exception)
