from django.conf.urls import include, patterns, url
from django.contrib.auth.decorators import login_required

from apps.ava_core_people import views


urlpatterns = patterns('',
    
    url(r'^$', login_required(views.PersonIndex.as_view()), name='index'),
    #url(r'^(?P<pk>\d+)/$', login_required(views.PersonIndexView.as_view()), name='people'),
    url(r'^(?P<pk>\d+)/view/$', login_required(views.PersonDetail.as_view()), name='person-detail'),
    url(r'^new/$',login_required(views.PersonCreate.as_view()),name='people_new'),
    url(r'^search/', login_required(include('haystack.urls'))),
    url(r'^(?P<pk>\d+)/update/$', login_required(views.PersonUpdate.as_view()), name='people_update'),
    url(r'^(?P<pk>\d+)/id/update/$', login_required(views.IdentifierUpdate.as_view()), name='identifier_update'),
    url(r'^(?P<pk>\d+)/id/delete/$', login_required(views.IdentifierDelete.as_view()), name='identifier_delete'),
    url(r'^(?P<pk>\d+)/delete/$', login_required(views.PersonDelete.as_view()), name='people_delete'),
)
