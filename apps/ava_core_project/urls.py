from django.conf.urls import include, patterns, url
from django.contrib.auth.decorators import login_required

from apps.ava_core_project import views

urlpatterns = patterns('',
    
    url(r'^$', login_required(views.DashboardView.as_view()), name='index'),
    url(r'^(?P<pk>\d+)/$', login_required(views.ProjectIndexView.as_view()), name='project-detail'),
    url(r'^(?P<pk>\d+)/view/$', login_required(views.ProjectDetailView.as_view()), name='project_view'),
    url(r'^new/$',login_required(views.ProjectCreateView.as_view()),name='project_new'),
    url(r'^(?P<pk>\d+)/update/$', login_required(views.ProjectUpdateView.as_view()), name='project_update'),
    url(r'^(?P<pk>\d+)/delete/$', login_required(views.ProjectDeleteView.as_view()), name='project_delete'),
)
