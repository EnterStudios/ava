from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required

from ava.core_project import views
from ava.core_project.decorators import project_access_required
from ava.core_project.models import ProjectAccess

urlpatterns = patterns(
    '',
    url(r'^$', login_required(views.ProjectIndex.as_view()), name='project-index'),
    url(r'^new/$', login_required(views.ProjectCreate.as_view()), name='project-create'),
    url(r'^(?P<pk>\d+)/$', project_access_required(ProjectAccess.VIEW, views.ProjectDetail.as_view()),
        name='project-detail'),
    url(r'^(?P<pk>\d+)/update/$', project_access_required(ProjectAccess.MODIFY, views.ProjectUpdate.as_view()),
        name='project-update'),
    url(r'^(?P<pk>\d+)/delete/$', project_access_required(ProjectAccess.MODIFY, views.ProjectDelete.as_view()),
        name='project-delete'),

    # Team security management within the project.
    url(r'^(?P<pk>\d+)/teams/(?P<team>\d+)/$',
        project_access_required(ProjectAccess.MODIFY, views.ProjectTeams.as_view()), name='project-teams'),
    url(r'^(?P<pk>\d+)/teams/add/$', project_access_required(ProjectAccess.MODIFY, views.ProjectTeamsAdd.as_view()),
        name='project-teams-add'),
    url(r'^(?P<pk>\d+)/teams/remove/(?:(?P<team>\d+)/)?$',
        project_access_required(ProjectAccess.MODIFY, views.ProjectTeamsRemove.as_view()), name='project-teams-remove'),

    url(r'^(?P<pk>\d+)/groups/add/$', project_access_required(ProjectAccess.MODIFY, views.ProjectGroupsAdd.as_view()),
        name='project-groups-add'),
    url(r'^(?P<pk>\d+)/groups/remove/(?:(?P<group>\d+)/)?$',
        project_access_required(ProjectAccess.MODIFY, views.ProjectGroupDelete.as_view()),
        name='project-groups-remove'),

    url(r'^(?P<pk>\d+)/identities/add/$',
        project_access_required(ProjectAccess.MODIFY, views.ProjectIdentitiesAdd.as_view()),
        name='project-identities-add'),
    url(r'^(?P<pk>\d+)/identities/remove/(?:(?P<ident>\d+)/)?$',
        project_access_required(ProjectAccess.MODIFY, views.ProjectIdentitiesRemove.as_view()),
        name='project-identities-remove'),

    url(r'^(?P<pk>\d+)/identifiers/add/$',
        project_access_required(ProjectAccess.MODIFY, views.ProjectIdentifiersAdd.as_view()),
        name='project-identifiers-add'),
    url(r'^(?P<pk>\d+)/identities/remove/(?:(?P<ident>\d+)/)?$',
        project_access_required(ProjectAccess.MODIFY, views.ProjectIdentifiersRemove.as_view()),
        name='project-identifiers-remove'),
)
