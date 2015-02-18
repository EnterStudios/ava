from django.views.generic import CreateView, ListView, DetailView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView

from django.shortcuts import get_object_or_404
from apps.ava_core_project.models import Project
from apps.ava_core_project.forms import  ProjectForm

class DashboardView(ListView):
    template_name = 'project/home.html'
    context_object_name = 'list'

    def get_queryset(self):
        self.request.session['project']=None 
        return Project.objects.filter(user=self.request.user)


class ProjectIndexView(ListView):
    template_name = 'project/index.html'
    context_object_name = 'list'

    def get_queryset(self):
        self.request.session['project']=None 
        return Project.objects.filter(user=self.request.user)

class ProjectDetailView(DetailView):
    model = Project
    context_object_name = 'project'
    template_name = 'project/view.html'

    def get(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk')
        if pk:
            project = get_object_or_404(Project, pk=pk)
            request.session['project']=project.id
        return super(ProjectDetailView,self).get(self, request, *args, **kwargs)

class ProjectDeleteView(DeleteView):
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
