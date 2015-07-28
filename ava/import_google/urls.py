from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required

from ava.import_google import views

urlpatterns = patterns(
    '',
    url(r'^$', login_required(views.GoogleConfigurationIndex.as_view()), name='google-configuration-index'),
    url(r'^new/$', login_required(views.GoogleConfigurationCreate.as_view()),
        name='google-configuration-create'),
    url(r'^(?P<pk>\d+)/view/$', login_required(views.GoogleConfigurationDetail.as_view()),
        name='google-configuration-detail'),
    url(r'^(?P<pk>\d+)/update/$', login_required(views.GoogleConfigurationUpdate.as_view()),
        name='google-configuration-update'),
    url(r'^(?P<pk>\d+)/delete/$', login_required(views.GoogleConfigurationDelete.as_view()),
        name='google-configuration-delete'),
    
    url(r'^import/$', login_required(views.GoogleDirectoryImport.as_view()),
        name='google-import'),

    url(r'^users/$', login_required(views.GoogleDirectoryUserIndex.as_view()),
        name='google-user-index'),
    url(r'^users/(?P<pk>\d+)/view/$', login_required(views.GoogleDirectoryUserDetail.as_view()),
        name='google-user-detail'),
    url(r'^users/(?P<pk>\d+)/delete/$', login_required(views.GoogleDirectoryUserDelete.as_view()),
        name='google-user-delete'),

    url(r'^groups/$', login_required(views.GoogleDirectoryGroupIndex.as_view()),
        name='google-group-index'),
    url(r'^groups/(?P<pk>\d+)/view/$', login_required(views.GoogleDirectoryGroupDetail.as_view()),
        name='google-group-detail'),
    url(r'^groups/(?P<pk>\d+)/delete/$', login_required(views.GoogleDirectoryGroupDelete.as_view()),
        name='google-group-delete'),
)
