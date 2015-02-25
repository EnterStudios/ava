from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required

from apps.ava_test import views


urlpatterns = patterns('',
    
    url(r'^$', login_required(views.TestIndexView.as_view()), name='index'),
    url(r'^(?P<pk>\d+)/$', login_required(views.TestIndexView.as_view()), name='test'),
    url(r'^(?P<pk>\d+)/view/$', login_required(views.TestDetailView.as_view()), name='test_view'),
    url(r'^new/$',login_required(views.TestCreateView.as_view()),name='test_new'),
    url(r'^(?P<pk>\d+)/update/$', login_required(views.TestUpdateView.as_view()), name='test_update'),
    url(r'^(?P<pk>\d+)/delete/$', login_required(views.TestDeleteView.as_view()), name='test_delete'),
)
