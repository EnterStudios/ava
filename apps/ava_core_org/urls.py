from django.conf.urls import include, patterns, url
from django.contrib.auth.decorators import login_required

from apps.ava_core_org import views

urlpatterns = patterns('',
    
    url(r'^(?P<pk>\d+)/view/$', login_required(views.OrganisationDetail.as_view()), name='org-detail'),
    url(r'^new/$',login_required(views.OrganisationCreate.as_view()),name='org_new'),
    url(r'^search/', login_required(include('haystack.urls'))),
    url(r'^(?P<pk>\d+)/update/$', login_required(views.OrganisationUpdate.as_view()), name='org_update'),
    url(r'^(?P<pk>\d+)/delete/$', login_required(views.OrganisationDelete.as_view()), name='org_delete'),
)
