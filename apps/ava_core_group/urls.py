from django.conf.urls import include, patterns, url
from django.contrib.auth.decorators import login_required

from apps.ava_core_group import views


urlpatterns = patterns('',

    url(r'^$', login_required(views.GroupIndex.as_view()), name='group-index'),
    url(r'^(?P<pk>\d+)/view/$', login_required(views.GroupDetail.as_view()), name='group-detail'),
    url(r'^new/$',login_required(views.GroupCreate.as_view()),name='group-create'),
    url(r'^search/', login_required(include('haystack.urls'))),
    url(r'^(?P<pk>\d+)/update/$', login_required(views.GroupUpdate.as_view()), name='group-update'),
    url(r'^(?P<pk>\d+)/delete/$', login_required(views.GroupDelete.as_view()), name='group-delete'),


    url(r'^type$', login_required(views.GroupTypeIndex.as_view()), name='group-type-index'),
    url(r'^type/(?P<pk>\d+)/view/$', login_required(views.GroupTypeDetail.as_view()), name='group-type-detail'),
    url(r'^type/new/$',login_required(views.GroupTypeCreate.as_view()),name='group-type-create'),
    url(r'^type/(?P<pk>\d+)/update/$', login_required(views.GroupTypeUpdate.as_view()), name='group-type-update'),
    url(r'^type/(?P<pk>\d+)/delete/$', login_required(views.GroupTypeDelete.as_view()), name='group-type-delete'),
)
