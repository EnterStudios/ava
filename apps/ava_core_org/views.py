from django.views.generic import CreateView, ListView, DetailView
from django.shortcuts import get_object_or_404
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView

from apps.ava_core_org.models import Organisation
from apps.ava_core_org.forms import OrganisationForm
from apps.ava_core_identity.models import Person
from apps.ava_core_project.models import Project


class OrganisationIndex(ListView):
    template_name = 'organisation/index.html'
    context_object_name = 'org_list'

    def get_queryset(self):
        self.request.session['organisation']=None
        return Organisation.objects.filter(user=self.request.user,project=self.request.session['project'])

class OrganisationDetail(DetailView):
    model = Organisation
    context_object_name = 'organisation'
    template_name = 'organisation/view.html'

    def get_context_data(self, **kwargs):
        context = super(OrganisationDetail, self).get_context_data(**kwargs)

        pk = self.kwargs.get('pk')
        id_count=0
        organisation = get_object_or_404(Organisation, pk=pk)
        people = Person.objects.filter(organisation=organisation)
        for p in people:
            fish = p.identifier_set.all().count()
            id_count = id_count + fish

        context['org_identifier_count'] = id_count

        return context

    def get(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk')
        if pk:
            organisation = get_object_or_404(Organisation, pk=pk)
            request.session['organisation']=organisation.id
        return super(OrganisationDetail,self).get(self, request, *args, **kwargs)

class OrganisationDelete(DeleteView):
    model = Organisation
    template_name = 'confirm_delete.html'

class OrganisationCreate(CreateView):
    model = Organisation
    form_class = OrganisationForm
    template_name = 'organisation/organisation.html'
    
    def form_valid(self, form):
        project_id = self.request.session['project']
        if project_id:
            project = get_object_or_404(Project, pk=project_id)
            form.instance.project = project
            form.instance.user = self.request.user
        return super(OrganisationCreate, self).form_valid(form)

class OrganisationUpdate(UpdateView):
    model = Organisation
    template_name = 'organisation/organisation.html'
    form_class = OrganisationForm
