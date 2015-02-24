from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404
from django.views.generic import CreateView, ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView

from apps.ava_core.views import FormsetMixin
from apps.ava_core_identity.models import Identity, Person, Identifier
from apps.ava_core_identity.forms import IdentityForm, IdentifierFormSet, PersonForm



class IdentityIndex(ListView):
    template_name = 'identity/identity_index.html'
    context_object_name = 'identity_list'
    model = Identity

    def get_queryset(self):
        return Identity.objects.all()


class IdentityDetail(DetailView):
    model = Identity
    context_object_name = 'identity'
    template_name = 'identity/identity_detail.html'


class IdentityCreate(FormsetMixin, CreateView):
    template_name = 'identity/identity.html'
    model = Identity
    form_class = IdentityForm
    formset_class = IdentifierFormSet

#    def form_valid(self, form, formset):
#        org_id = self.request.session['organisation']
#        if org_id:
#            organisation = get_object_or_404(Organisation, pk=org_id)
#            form.instance.organisation = organisation
#            form.instance.user = self.request.user
#        return super(PersonCreate, self).form_valid(form, formset)


class IdentityUpdate(FormsetMixin, UpdateView):
    template_name = 'identity/identity.html'
    context_object_name = 'identity'
    model = Identity
    is_update_view = True
    form_class = IdentityForm
    formset_class = IdentifierFormSet


class IdentityDelete(DeleteView):
    model = Identity
    template_name = 'confirm_delete.html'
    
    def get_success_url(self):
        return reverse('index')


class PersonIndex(ListView):
    template_name = 'identity/index.html'
    context_object_name = 'people_list'
    model = Person

    def get_queryset(self):
        return Person.objects.all()

class PersonDetail(DetailView):
    model = Person
    context_object_name = 'person'
    template_name = 'identity/person_detail.html'


class PersonCreate(FormsetMixin, CreateView):
    template_name = 'identity/person.html'
    model = Person
    form_class = PersonForm
    formset_class = IdentifierFormSet

#    def form_valid(self, form, formset):
#        org_id = self.request.session['organisation']
#        if org_id:
#            organisation = get_object_or_404(Organisation, pk=org_id)
#            form.instance.organisation = organisation
#            form.instance.user = self.request.user
#        return super(PersonCreate, self).form_valid(form, formset)


class PersonUpdate(FormsetMixin, UpdateView):
    template_name = 'identity/person.html'
    model = Person
    is_update_view = True
    form_class = PersonForm
    formset_class = IdentifierFormSet


class PersonDelete(DeleteView):
    model = Person
    template_name = 'confirm_delete.html'
    
    def get_success_url(self):
        #TODO: Redirect to parent object
        return reverse('index')


class IdentifierUpdate(UpdateView):
    model = Identifier
    fields = ['identifier', 'identifiertype']
    template_name = 'identity/identifier_update_form.html'


class IdentifierDelete(DeleteView):
    model = Identifier
    template_name = 'confirm_delete.html'
    
    def get_success_url(self):
        #TODO: Redirect to parent object
        return reverse('index')



