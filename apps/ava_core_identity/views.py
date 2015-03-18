from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404
from django.views.generic import CreateView, ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView

from apps.ava_core.views import FormsetMixin
from apps.ava_core_identity.models import Identity, Person, Identifier
from apps.ava_core_identity.forms import IdentityForm, PersonForm, IdentifierForm, IdentifierFormSet


### IDENTITY

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


### PERSON

class PersonIndex(ListView):
    template_name = 'identity/person_index.html'
    context_object_name = 'person_list'
    model = Person

    def get_queryset(self):
        return Person.objects.all()


class PersonDetail(DetailView):
    model = Person
    context_object_name = 'person'
    template_name = 'identity/person_detail.html'


class PersonCreate(CreateView):
    model = Person
    context_object_name = 'person'
    template_name = 'identity/person.html'
    form_class = PersonForm


class PersonUpdate(UpdateView):
    model = Person
    context_object_name = 'person'
    template_name = 'identity/person.html'
    form_class = PersonForm


class PersonDelete(DeleteView):
    model = Person
    template_name = 'confirm_delete.html'
    
    def get_success_url(self):
        #TODO: Redirect to parent object
        return reverse('person-index')


class IdentifierCreate(CreateView):
    model = Identifier
    fields = ['identifiertype', 'identifier']
    template_name = 'identity/identifier.html'
    form_class = IdentifierForm
    
    identity = None
    
    def dispatch(self, request, *args, **kwargs):
        #Check that the identity exists and store it for later.
        identity_id = kwargs['identity']
        self.identity = get_object_or_404(Identity, pk=identity_id)
        return super(IdentifierCreate, self).dispatch(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super(IdentifierCreate, self).get_context_data(**kwargs)
        context['identity'] = self.identity
        return context
    
    def form_valid(self, form):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        if self.identity and form:
            form.instance.identity = self.identity
            #TODO: Check whether the identifier is a duplicate or not.
            return super(IdentifierCreate, self).form_valid(form)
        return super(IdentifierCreate, self).form_invalid(form)
    
    def get_success_url(self):
        return self.identity.get_absolute_url()


class IdentifierUpdate(UpdateView):
    model = Identifier
    fields = ['identifiertype', 'identifier']
    template_name = 'identity/identifier_update_form.html'

    def get_success_url(self):
        return self.get_object().identity.get_absolute_url()


class IdentifierDelete(DeleteView):
    model = Identifier
    template_name = 'confirm_delete.html'
    
    def get_success_url(self):
        return self.get_object().identity.get_absolute_url()



