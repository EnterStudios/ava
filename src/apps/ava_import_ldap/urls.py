from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required

from apps.ava_import_ldap import views


urlpatterns = patterns(
    '',
    url(r'^$', login_required(views.LDAPConfigurationIndex.as_view()), name='ldap-configuration-index'),
    url(r'^new/$', login_required(views.LDAPConfigurationCreate.as_view()),
        name='ldap-configuration-create'),
    url(r'^(?P<pk>\d+)/view/$', login_required(views.LDAPConfigurationDetail.as_view()),
        name='ldap-configuration-detail'),
    url(r'^(?P<pk>\d+)/update/$', login_required(views.LDAPConfigurationUpdate.as_view()),
        name='ldap-configuration-update'),
    url(r'^(?P<pk>\d+)/delete/$', login_required(views.LDAPConfigurationDelete.as_view()),
        name='ldap-configuration-delete'),

    url(r'^(?P<pk>\d+)/aduser/$', login_required(views.ActiveDirectoryUserIndex.as_view()), name='ad-user-index'),
    url(r'^(?P<pk>\d+)/aduser/new/$', login_required(views.ActiveDirectoryUserCreate.as_view()), name='ad-user-create'),
    url(r'^aduser/(?P<pk>\d+)/view/$', login_required(views.ActiveDirectoryUserDetail.as_view()),
        name='ad-user-detail'),
    url(r'^aduser/(?P<pk>\d+)/update/$', login_required(views.ActiveDirectoryUserUpdate.as_view()),
        name='ad-user-update'),
    url(r'^aduser/(?P<pk>\d+)/delete/$', login_required(views.ActiveDirectoryUserDelete.as_view()),
        name='ad-user-delete'),
    
    url(r'^(?P<pk>\d+)/adgroup/$', login_required(views.ActiveDirectoryGroupIndex.as_view()), name='ad-group-index'),
    url(r'^(?P<pk>\d+)/adgroup/new/$', login_required(views.ActiveDirectoryGroupCreate.as_view()),
        name='ad-group-create'),
    url(r'^adgroup/(?P<pk>\d+)/view/$', login_required(views.ActiveDirectoryGroupDetail.as_view()),
        name='ad-group-detail'),
    url(r'^adgroup/(?P<pk>\d+)/update/$', login_required(views.ActiveDirectoryGroupUpdate.as_view()),
        name='ad-group-update'),
    url(r'^adgroup/(?P<pk>\d+)/delete/$', login_required(views.ActiveDirectoryGroupDelete.as_view()),
        name='ad-group-delete'),

    url(r'^(?P<pk>\d+)/import/$', login_required(views.LDAPConfigurationImport.as_view()), name='ldap-import-all'),
    """
    url(r'^(?P<pk>\d+)/getusers/$', login_required(views.LDAPConfigurationGetUsers.as_view()), name='ldap-get-users'),
    url(r'^(?P<pk>\d+)/getgroups/$', login_required(views.LDAPConfigurationGetGroups.as_view()),
    name='ldap-get-groups'),
    """

   
)
