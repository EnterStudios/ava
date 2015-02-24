from django.conf.urls import include, patterns, url
from django.contrib.auth.decorators import login_required

from apps.ava_core_identity import views


urlpatterns = patterns('',
    
    url(r'^$', login_required(views.IdentityIndex.as_view()), name='index'),
    url(r'^search/', login_required(include('haystack.urls'))),

    url(r'^identity/$', login_required(views.IdentityIndex.as_view()), name='identity-index'),
    url(r'^identity/new/$', login_required(views.IdentityCreate.as_view()), name='identity-create'),
    url(r'^identity/(?P<pk>\d+)/$', login_required(views.IdentityDetail.as_view()), name='identity-detail'),
    url(r'^identity/(?P<pk>\d+)/update/$', login_required(views.IdentityUpdate.as_view()), name='identity-update'),
    url(r'^identity/(?P<pk>\d+)/delete/$', login_required(views.IdentityDelete.as_view()), name='identity-delete'),
    
     url(r'^person/$', login_required(views.PersonIndex.as_view()), name='person-index'),
    url(r'^person/new/$', login_required(views.PersonCreate.as_view()), name='person-create'),
    url(r'^person/(?P<pk>\d+)/$', login_required(views.PersonDetail.as_view()), name='person-detail'),
    url(r'^person/(?P<pk>\d+)/update/$', login_required(views.PersonUpdate.as_view()), name='person-update'),
    url(r'^person/(?P<pk>\d+)/delete/$', login_required(views.PersonDelete.as_view()), name='person-delete'),
    
    url(r'^identifier/(?P<pk>\d+)/update/$', login_required(views.IdentifierUpdate.as_view()), name='identifier-update'),
    url(r'^identifier/(?P<pk>\d+)/delete/$', login_required(views.IdentifierDelete.as_view()), name='identifier-delete'),
)
