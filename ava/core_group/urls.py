from django.conf.urls import include, patterns, url
from django.contrib.auth.decorators import login_required

from ava.core_group import views


urlpatterns = patterns(
    '',
    url(r'^$', login_required(views.GroupIndex.as_view()), name='group-index'),
    url(r'^(?P<pk>\d+)/view/$', login_required(views.GroupDetail.as_view()), name='group-detail'),
    url(r'^new/$', login_required(views.GroupCreate.as_view()), name='group-create'),
    url(r'^search/', login_required(include('haystack.urls'))),
    url(r'^(?P<pk>\d+)/update/$', login_required(views.GroupUpdate.as_view()), name='group-update'),
    url(r'^(?P<pk>\d+)/delete/$', login_required(views.GroupDelete.as_view()), name='group-delete'),

)
