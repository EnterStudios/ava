from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required

from apps.ava_core_google_apps import views


urlpatterns = patterns('',
    
    url(r'^$', login_required(views.GoogleConfigurationIndex.as_view()), name='google-configuration-index'),
    url(r'^new/$',login_required(views.GoogleConfigurationCreate.as_view()),name='google-configuration-create'),
    url(r'^(?P<pk>\d+)/view/$', login_required(views.GoogleConfigurationDetail.as_view()), name='google-configuration-detail'),
    url(r'^(?P<pk>\d+)/update/$', login_required(views.GoogleConfigurationUpdate.as_view()), name='google-configuration-update'),
    url(r'^(?P<pk>\d+)/delete/$', login_required(views.GoogleConfigurationDelete.as_view()), name='google-configuration-delete'),

    url(r'^(?P<pk>\d+)/aduser/$', login_required(views.GoogleDirectoryUserIndex.as_view()), name='google-user-index'),
    url(r'^(?P<pk>\d+)/aduser/new/$',login_required(views.GoogleDirectoryUserCreate.as_view()),name='google-user-create'),
    url(r'^aduser/(?P<pk>\d+)/view/$', login_required(views.GoogleDirectoryUserDetail.as_view()), name='google-user-detail'),
    url(r'^aduser/(?P<pk>\d+)/update/$', login_required(views.GoogleDirectoryUserUpdate.as_view()), name='google-user-update'),
    url(r'^aduser/(?P<pk>\d+)/delete/$', login_required(views.GoogleDirectoryUserDelete.as_view()), name='google-user-delete'),
    
    url(r'^(?P<pk>\d+)/adgroup/$', login_required(views.GoogleDirectoryGroupIndex.as_view()), name='google-group-index'),
    url(r'^(?P<pk>\d+)/adgroup/new/$',login_required(views.GoogleDirectoryGroupCreate.as_view()),name='google-group-create'),
    url(r'^adgroup/(?P<pk>\d+)/view/$', login_required(views.GoogleDirectoryGroupDetail.as_view()), name='google-group-detail'),
    url(r'^adgroup/(?P<pk>\d+)/update/$', login_required(views.GoogleDirectoryGroupUpdate.as_view()), name='google-group-update'),
    url(r'^adgroup/(?P<pk>\d+)/delete/$', login_required(views.GoogleDirectoryGroupDelete.as_view()), name='google-group-delete'),
    
  
    url(r'^(?P<pk>\d+)/getusers/$', login_required(views.GoogleConfigurationGetUsers.as_view()), name='google-get-users'),
    url(r'^(?P<pk>\d+)/getgroups/$', login_required(views.GoogleConfigurationGetGroups.as_view()), name='google-get-groups'),
    
   
)
