from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required

from apps.ava_core_project import views
from apps.ava_core_project.decorators import project_access_required
from apps.ava_core_project.models import ProjectAccess


urlpatterns = patterns('',
    
    url(r'^$', login_required(views.ProjectIndex.as_view()), name='project-index'),
    url(r'^new/$',login_required(views.ProjectCreate.as_view()),name='project-create'),
    url(r'^(?P<pk>\d+)/$', project_access_required(ProjectAccess.VIEW, views.ProjectDetail.as_view()), name='project-detail'),
    url(r'^(?P<pk>\d+)/update/$', project_access_required(ProjectAccess.MODIFY, views.ProjectUpdate.as_view()), name='project-update'),
    url(r'^(?P<pk>\d+)/delete/$', project_access_required(ProjectAccess.MODIFY, views.ProjectDelete.as_view()), name='project-delete'),
    
    url(r'^(?P<pk>\d+)/(?P<gk>\d+)/delete/$', project_access_required(ProjectAccess.MODIFY, views.ProjectGroupDelete.as_view()), name='project-group-delete'),
)
