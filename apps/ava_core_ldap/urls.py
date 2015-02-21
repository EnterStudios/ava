from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required

from apps.ava_core_ldap import views


urlpatterns = patterns('',
    
    #url(r'^$', login_required(views.ConfigurationIndexView.as_view()), name='index'),
    #url(r'^(?P<pk>\d+)/$', login_required(views.ConfigurationIndexView.as_view()), name='ldap'),
    url(r'^(?P<pk>\d+)/view/$', login_required(views.ConfigurationDetailView.as_view()), name='ldap_view'),
    url(r'^(?P<pk>\d+)/view/users/$', login_required(views.ConfigurationUserView.as_view()), name='ldap_users_view'),
    url(r'^(?P<pk>\d+)/view/groups/$', login_required(views.ConfigurationGroupView.as_view()), name='ldap_groups_view'),
    url(r'^(?P<pk>\d+)/viewitems/$', login_required(views.ConfigurationItemView.as_view()), name='ldap_items_view'),
    url(r'^new/$',login_required(views.ConfigurationCreateView.as_view()),name='ldap_new'),
    url(r'^(?P<pk>\d+)/update/$', login_required(views.ConfigurationUpdateView.as_view()), name='ldap_update'),
    url(r'^(?P<pk>\d+)/delete/$', login_required(views.ConfigurationDeleteView.as_view()), name='ldap_delete'),
    url(r'^(?P<pk>\d+)/getusers/$', login_required(views.ConfigurationGetUsers.as_view()), name='ldap_get_users'),
    url(r'^(?P<pk>\d+)/getgroups/$', login_required(views.ConfigurationGetGroups.as_view()), name='ldap_get_groups'),
    url(r'^(?P<pk>\d+)/getall/$', login_required(views.ConfigurationGetAll.as_view()), name='ldap_get_all'),
    url(r'^user/(?P<pk>\d+)/delete/$', login_required(views.ConfigurationDeleteUser.as_view()), name='ldap_delete_user'),
    url(r'^group/(?P<pk>\d+)/delete/$', login_required(views.ConfigurationDeleteGroup.as_view()), name='ldap_delete_group'),
)
