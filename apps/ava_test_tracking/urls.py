from django.conf.urls import patterns, url
from apps.ava_test_tracking import views


urlpatterns = patterns('',
    url(r'^e/(?P<token>[^/]+)/$', views.RecordEmailTestResultView.as_view(), name='email-test-tracking'),
    url(r'^t/(?P<token>[^/]+)/$', views.RecordEmailTestResultView.as_view(), name='twitter-test-tracking'),
)