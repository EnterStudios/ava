from django.conf.urls import patterns, url
from ava.test_tracking import views

urlpatterns = patterns('',
                       url(r'^e/(?P<token>[^/]+)/(?P<extra>.*)?$', views.RecordEmailTestResultView.as_view(),
                           name='email-test-tracking'),
                       url(r'^t/(?P<token>[^/]+)/(?P<extra>.*)?$', views.RecordEmailTestResultView.as_view(),
                           name='twitter-test-tracking'),
                       )
