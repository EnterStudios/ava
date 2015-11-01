from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required
from ava.core_auth.decorators import system_admin_required

from ava.core_identity import views

urlpatterns = patterns(
    '',
    url(r'^$', login_required(views.IdentityIndex.as_view()), name='identity-dashboard'),

    url(r'^identity/$', login_required(views.IdentityIndex.as_view()), name='identity-index'),
    url(r'^identity/new/$', system_admin_required(views.IdentityCreate.as_view()), name='identity-create'),
    url(r'^identity/(?P<pk>\d+)/$', login_required(views.IdentityDetail.as_view()), name='identity-detail'),
    url(r'^identity/(?P<pk>\d+)/update/$', system_admin_required(views.IdentityUpdate.as_view()),
        name='identity-update'),
    url(r'^identity/(?P<pk>\d+)/delete/$', system_admin_required(views.IdentityDelete.as_view()),
        name='identity-delete'),

    url(r'^person/$', login_required(views.PersonIndex.as_view()), name='person-index'),
    url(r'^person/new/$', login_required(views.PersonCreate.as_view()), name='person-create'),
    url(r'^person/(?P<pk>\d+)/$', login_required(views.PersonDetail.as_view()), name='person-detail'),
    url(r'^person/(?P<pk>\d+)/update/$', login_required(views.PersonUpdate.as_view()), name='person-update'),
    url(r'^person/(?P<pk>\d+)/delete/$', login_required(views.PersonDelete.as_view()), name='person-delete'),

    # Note: The value below is <identity> not <pk> because it refers to the parent identity, not an identifier.
    url(r'^identity/(?P<identity>\d+)/new-identifier/$', login_required(views.IdentifierCreate.as_view()),
        name='identifier-create'),
    url(r'^identifier/(?P<pk>\d+)/update/$', login_required(views.IdentifierUpdate.as_view()),
        name='identifier-update'),
    url(r'^identifier/(?P<pk>\d+)/delete/$', login_required(views.IdentifierDelete.as_view()),
        name='identifier-delete'),
)
