from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required

from ava.test_twitter import views
from ava.test.decorators import create_test_access_check
from ava.test_twitter.decorators import twitter_test_access_check
from ava.core_project.models import ProjectAccess

urlpatterns = patterns('',

                       url(r'^$', login_required(views.TwitterTestIndex.as_view()), name='twitter-test-index'),
                       url(r'^new/(?P<proj>\d+)/$', create_test_access_check('proj', ProjectAccess.RUN_TEST,
                                                                             views.TwitterTestCreate.as_view()),
                           name='twitter-test-create'),
                       url(r'^(?P<pk>\d+)/$',
                           twitter_test_access_check(ProjectAccess.VIEW, views.TwitterTestDetail.as_view()),
                           name="twitter-test-detail"),
                       url(r'^(?P<pk>\d+)/update/$',
                           twitter_test_access_check(ProjectAccess.RUN_TEST, views.TwitterTestUpdate.as_view()),
                           name='twitter-test-update'),
                       url(r'^(?P<pk>\d+)/delete/$',
                           twitter_test_access_check(ProjectAccess.RUN_TEST, views.TwitterTestDelete.as_view()),
                           name='twitter-test-delete'),
                       # url(r'^send/(?P<pk>\d+)/$', twitter_test_access_check(ProjectAccess.RUN_TEST,
                       # views.EmailSendEmail.as_view()), name='twitter-test-send'),

                       )
