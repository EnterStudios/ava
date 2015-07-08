from django.conf.urls import patterns, url

from . import views


urlpatterns = patterns(
    '',
    url('^first-user/$', views.CreateFirstUser.as_view(), name='first-user'),
)
