from django.views import generic
from django.views.generic import CreateView
from django.shortcuts import get_object_or_404
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView

from apps.ava_core.views import FormsetMixin

from apps.ava_core_people.models import Person, Identifier
from apps.ava_core_org.models import Organisation
from apps.ava_core_people.forms import IdentifierFormSet, PersonForm


class PersonIndex(generic.ListView):
    template_name = 'people/index.html'
    context_object_name = 'people_list'

    def get_queryset(self):
        return Person.objects.filter(user=self.request.user)


class PersonDetail(generic.DetailView):
    model = Person
    context_object_name = 'person'
    template_name = 'people/view.html'


class IdentifierUpdate(UpdateView):
    model = Identifier
    fields = ['identifier', 'identifiertype']
    template_name = 'people/identifier_update_form.html'


class IdentifierDelete(DeleteView):
    model = Identifier
    template_name = 'confirm_delete.html'
    success_url = '/people/'


class PersonDelete(DeleteView):
    model = Person
    template_name = 'confirm_delete.html'
    success_url = '/people/'


class PersonUpdate(FormsetMixin, UpdateView):
    template_name = 'people/person.html'
    model = Person
    is_update_view = True
    form_class = PersonForm
    formset_class = IdentifierFormSet


class PersonCreate(FormsetMixin, CreateView):
    template_name = 'people/person.html'
    model = Person
    form_class = PersonForm
    formset_class = IdentifierFormSet

    def form_valid(self, form, formset):
        org_id = self.request.session['organisation']
        if org_id:
            organisation = get_object_or_404(Organisation, pk=org_id)
            form.instance.organisation = organisation
            form.instance.user = self.request.user
        return super(PersonCreate, self).form_valid(form, formset)
