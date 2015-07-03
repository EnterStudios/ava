from django.shortcuts import get_object_or_404
from django.views.generic import CreateView, ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView
from django.db.models import Q, Count

from ava.core.views import AddManyToManyView, RemoveManyToManyView
from ava.core_auth.models import Team, UserRights
from ava.core_group.models import Group
from ava.core_identity.models import Identity, Identifier
from ava.core_project.models import Project, ProjectTeam, ProjectAccess
from ava.core_project.forms import ProjectForm, ProjectTeamForm


class ProjectIndex(ListView):
    template_name = 'project/project_index.html'
    context_object_name = 'project_list'
    model = Project

    def get_queryset(self):
        user = self.request.user
        # If the user is an admin, they get to see all projects.
        if UserRights.get(user).is_admin:
            return Project.objects.all()
        # Everyone else sees project they own or that their team(s) can access.
        else:
            project_teams = ProjectTeam.objects.filter(team__users__exact=user)
            return Project.objects.filter(Q(teams__in=project_teams) | Q(owner=user)).distinct()


class ProjectDetail(DetailView):
    model = Project
    context_object_name = 'project'
    template_name = 'project/project_detail.html'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data.update({
            'can_run_test': self.object.user_has_access(self.request.user, ProjectAccess.RUN_TEST),
            'can_modify': self.object.user_has_access(self.request.user, ProjectAccess.MODIFY),
            'group_list': self.object.groups.annotate(identity_count=Count('identities')),
            'identity_list': self.object.identities.annotate(identifier_count=Count('identifiers')),
            'identifier_list': self.object.identifiers,
        })
        return context_data


class ProjectDelete(DeleteView):
    model = Project
    template_name = 'confirm_delete.html'
    success_url = '/project/'


class ProjectCreate(CreateView):
    model = Project
    template_name = 'project/project.html'
    form_class = ProjectForm

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class ProjectUpdate(UpdateView):
    model = Project
    template_name = 'project/project.html'
    form_class = ProjectForm


class ProjectTeams(UpdateView):
    template_name = 'project/project_team_update.html'
    context_object_name = 'project_team'
    model = ProjectTeam
    form_class = ProjectTeamForm

    def get_object(self, queryset=None):
        project_id = self.request.resolver_match.kwargs.get('pk', None)
        team_id = self.request.resolver_match.kwargs.get('team', None)
        return get_object_or_404(ProjectTeam, project__id=project_id, team__id=team_id)

    def get_success_url(self):
        project_id = self.request.resolver_match.kwargs.get('pk', None)
        project = get_object_or_404(Project, id=project_id)
        return project.get_absolute_url()


class ProjectTeamsAdd(AddManyToManyView):
    template_name = 'project/project_team_add.html'
    model = Project
    target_model = Team
    context_object_name = 'project'
    targets_context_object_name = 'team_list'
    target_id_field = 'team'

    def search_targets(self, target_queryset, search_term):
        return target_queryset.filter(name__icontains=search_term)

    def get_many_to_many(self):
        return self.object.teams

    def order_target_list(self, target_list):
        return target_list.order_by('name')

    def add_targets(self, target_ids):
        teams = Team.objects.filter(id__in=target_ids).all()
        for team in teams:
            # Create teams as needed, with the default rights.
            ProjectTeam.objects.get_or_create(project=self.object, team=team)


class ProjectTeamsRemove(RemoveManyToManyView):
    template_name = 'project/project_team_remove.html'
    model = Project
    context_object_name = 'project'
    targets_context_object_name = 'project_team_list'
    target_post_field = 'team'
    target_kwargs_field = 'team'

    def get_many_to_many(self):
        return self.object.teams

    def get_target_list(self, request):
        target_ids = self.get_target_ids(request)
        return self.get_many_to_many().filter(team__id__in=target_ids)

    def order_target_list(self, target_list):
        return target_list.order_by('name')

    def remove_targets(self, request):
        self.get_target_list(request).delete()


class ProjectGroupsAdd(AddManyToManyView):
    template_name = 'project/project_group_add.html'
    model = Project
    target_model = Group
    context_object_name = 'project'
    targets_context_object_name = 'group_list'

    def search_targets(self, target_queryset, search_term):
        search_filter = Q(name__icontains=search_term
                          ) | Q(description__icontains=search_term)
        return target_queryset.filter(search_filter)

    def get_many_to_many(self):
        return self.object.groups

    def order_target_queryset(self, target_queryset):
        return target_queryset.order_by('name')


class ProjectGroupDelete(RemoveManyToManyView):
    template_name = 'project/project_group_remove.html'
    model = Project
    target_model = Group
    context_object_name = 'project'
    targets_context_object_name = 'group_list'
    target_post_field = 'group'
    target_kwargs_field = 'group'

    def get_many_to_many(self):
        return self.object.groups


class ProjectIdentitiesAdd(AddManyToManyView):
    template_name = 'project/project_identity_add.html'
    model = Project
    target_model = Identity
    context_object_name = 'project'
    targets_context_object_name = 'identity_list'

    def get_target_queryset(self):
        return self.target_model.objects.annotate(identifier_count=Count('identifiers'))

    def search_targets(self, target_queryset, search_term):
        search_filter = Q(name__icontains=search_term
                          ) | Q(description__icontains=search_term)
        return target_queryset.filter(search_filter)

    def get_many_to_many(self):
        return self.object.identities


class ProjectIdentitiesRemove(RemoveManyToManyView):
    template_name = 'project/project_identity_remove.html'
    model = Project
    target_model = Identifier
    context_object_name = 'project'
    targets_context_object_name = 'identity_list'
    target_post_field = 'identity'
    target_kwargs_field = 'ident'

    def get_many_to_many(self):
        return self.object.identities


class ProjectIdentifiersAdd(AddManyToManyView):
    template_name = 'project/project_identifier_add.html'
    model = Project
    target_model = Identifier
    context_object_name = 'project'
    targets_context_object_name = 'identifier_list'

    def search_targets(self, target_queryset, search_term):
        return target_queryset.filter(identifier_icontains=search_term)

    def get_many_to_many(self):
        return self.object.identifiers


class ProjectIdentifiersRemove(RemoveManyToManyView):
    template_name = 'project/project_identifier_remove.html'
    model = Project
    target_model = Identifier
    context_object_name = 'project'
    targets_context_object_name = 'identifier_list'
    target_post_field = 'identifier'
    target_kwargs_field = 'ident'

    def get_many_to_many(self):
        return self.object.identifiers
