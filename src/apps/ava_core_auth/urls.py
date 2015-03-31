from django.conf.urls import patterns, url, include
from apps.ava_core_auth import views
from apps.ava_core_auth.decorators import system_admin_required


urlpatterns = patterns('',
    # Standard authentication functions
    url(
        '^login/',
        'django.contrib.auth.views.login',
        {'template_name': 'auth/login.html'},
        name='login'
    ),
    url(
        '^logout/',
        'django.contrib.auth.views.logout',
        {'template_name': 'auth/logout.html'},
        name='logout'
    ),
    url(
        '^password_change/',
        'django.contrib.auth.views.password_change',
        {'template_name': 'auth/password-change.html'},
        name='password_change'
    ),
    
    url(
        '^password_change/done/',
        'django.contrib.auth.views.password_change_done',
        {'template_name': 'auth/password-change-done.html'},
        name='password_change_done'
    ),
    url(
        '^password_reset/$',
        'django.contrib.auth.views.password_reset',
        {'template_name': 'auth/password-reset.html'},
        name='password_reset'
    ),
    url(
        '^password_reset/done/$',
        'django.contrib.auth.views.password_reset_done',
        {'template_name': 'auth/password-reset-done.html', 'post_reset_redirect': '/'},
        name='password_reset_done'
    ),
    url(
        '^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        'django.contrib.auth.views.password_reset_confirm',
        {'template_name': 'auth/password-reset-confirm.html'},
        name='password_reset_confirm'
    ),
    url(
        '^reset/done/',
        'django.contrib.auth.views.password_reset_complete',
        {'template_name': 'auth/password-reset-complete.html'},
        name='password_reset_complete'
    ),
    
    # AVA user management
    url('^user/$', system_admin_required(views.UserIndex.as_view()), name='user-index'),
    url('^user/new/$', system_admin_required(views.UserCreate.as_view()), name='user-create'),
    url('^user/(?P<pk>\d+)/$', system_admin_required(views.UserDetail.as_view()), name='user-detail'),
    url('^user/(?P<pk>\d+)/update/$', system_admin_required(views.UserUpdate.as_view()), name='user-update'),
    url('^user/(?P<pk>\d+)/delete/$', system_admin_required(views.UserDelete.as_view()), name='user-delete'),
    
    # AVA team management
    url('^team/$', system_admin_required(views.TeamIndex.as_view()), name='team-index'),
    url('^team/new/$', system_admin_required(views.TeamCreate.as_view()), name='team-create'),
    url('^team/(?P<pk>\d+)/$', system_admin_required(views.TeamDetail.as_view()), name='team-detail'),
    url('^team/(?P<pk>\d+)/update/$', system_admin_required(views.TeamUpdate.as_view()), name='team-update'),
    url('^team/(?P<pk>\d+)/delete/$', system_admin_required(views.TeamDelete.as_view()), name='team-delete'),
    url('^team/(?P<pk>\d+)/add/$', system_admin_required(views.TeamAddMembers.as_view()), name='team-add-members'),
    url('^team/(?P<pk>\d+)/remove/(?:(?P<user>\d+)/)?$', system_admin_required(views.TeamRemoveMembers.as_view()), name='team-remove-members'),
)
