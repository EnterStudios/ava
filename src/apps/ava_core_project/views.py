from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404, render_to_response
from django.views.generic import CreateView, ListView, DetailView, View
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.db.models import Q

from apps.ava_core_auth.models import UserRights
from apps.ava_core_group.models import Group
from apps.ava_core_project.models import Project
from apps.ava_core_project.forms import ProjectForm


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
            return Project.objects.filter(Q(teams__team__users__exact=user)|Q(owner__exact=user))


class ProjectDetail(DetailView):
    model = Project
    context_object_name = 'project'
    template_name = 'project/project_detail.html'


class ProjectDelete(DeleteView):
    model = Project
    template_name = 'confirm_delete.html'
    success_url = '/project/'


class ProjectCreate(CreateView):
    model = Project
    template_name = 'project/project.html'
    form_class = ProjectForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(ProjectCreate, self).form_valid(form)


class ProjectUpdate(UpdateView):
    model = Project
    template_name = 'project/project.html'
    form_class = ProjectForm


class ProjectGroupDelete(DetailView):
    model = Project
    context_object_name = 'project'
    template_name = 'project/project_detail.html'

    def get_object(self):
        project_id = self.kwargs.get('pk')
        group_id = self.kwargs.get('gk')
        if project_id:
            if group_id:
                proj = get_object_or_404(Project, pk=project_id)
                group = get_object_or_404(Group, pk=group_id)
                proj.group.remove(group)

        return super(ProjectGroupDelete, self).get_object()
