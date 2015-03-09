from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required

from apps.ava_core_project import views


urlpatterns = patterns('',
    
    url(r'^$', login_required(views.ProjectIndex.as_view()), name='project-index'),
    url(r'^(?P<pk>\d+)/view/$', login_required(views.ProjectDetail.as_view()), name='project-detail'),
    url(r'^new/$',login_required(views.ProjectCreate.as_view()),name='project-create'),
    url(r'^(?P<pk>\d+)/update/$', login_required(views.ProjectUpdate.as_view()), name='project-update'),
    url(r'^(?P<pk>\d+)/delete/$', login_required(views.ProjectDelete.as_view()), name='project-delete'),
    
    url(r'^(?P<pk>\d+)/(?P<gk>\d+)/delete/$', login_required(views.ProjectGroupDelete.as_view()), name='project-group-delete'),
)
