from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required

from apps.ava_test_twitter import views


urlpatterns = patterns('',
    
    url(r'^$', login_required(views.TwitterTestIndex.as_view()), name='index'),
    url(r'^(?P<pk>\d+)/$', login_required(views.TwitterTestIndex.as_view()), name='twittertest'),
    url(r'^(?P<pk>\d+)/view/$', login_required(views.TwitterTestDetail.as_view()), name='twittertest_view'),
    url(r'^new/$',login_required(views.TwitterTestCreate.as_view()),name='twittertest_new'),
    url(r'^(?P<pk>\d+)/update/$', login_required(views.TwitterTestUpdate.as_view()), name='twittertest_update'),
    url(r'^(?P<pk>\d+)/delete/$', login_required(views.TwitterTestDelete.as_view()), name='twittertest_delete'),
    url(r'^send/$', login_required(views.TwitterTestSendTweet.as_view()), name='twittersend'),

    )
