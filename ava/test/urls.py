from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required

from apps.ava_test import views


urlpatterns = patterns('',
    
    url(r'^$', login_required(views.TestDashboardView.as_view()), name='test-dashboard'),
    url(r'^(?P<pk>\d+)/$', login_required(views.TestProjectDashboardView.as_view()), name='test-project-dashboard'),

)
