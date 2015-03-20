from django.shortcuts import redirect
from django.views import generic
from apps.ava_core_identity.models import Person, Identity
from apps.ava_core_ldap.models import LDAPConfiguration
from apps.ava_core_project.models import Project
from apps.ava_test_email.models import EmailTest
from apps.ava_test_twitter.models import TwitterTest


class FormsetMixin(object):
    '''
    This is a generic mixin to provide clean functionality for creating and updating related models via FormSet
    This mixin can be inherited and used as an alternative to generic.CreateView and generic.UpdateView


    Example:

    class PersonCreate(FormsetMixin, CreateView):
        template_name = 'identity/person.html'
        model = Person
        form_class = PersonForm
        formset_class = IdentifierFormSet
    '''

    object = None

    def get(self, request, *args, **kwargs):
        if getattr(self, 'is_update_view', False):
            self.object = self.get_object()
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        formset_class = self.get_formset_class()
        formset = self.get_formset(formset_class)
        return self.render_to_response(self.get_context_data(form=form, formset=formset))

    def post(self, request, *args, **kwargs):
        if getattr(self, 'is_update_view', False):
            self.object = self.get_object()
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        formset_class = self.get_formset_class()
        formset = self.get_formset(formset_class)
        if form.is_valid() and formset.is_valid():
            return self.form_valid(form, formset)
        else:
            return self.form_invalid(form, formset)

    def get_formset_class(self):
        return self.formset_class

    def get_formset(self, formset_class):
        return formset_class(**self.get_formset_kwargs())

    def get_formset_kwargs(self):
        kwargs = {
            'instance': self.object
        }
        if self.request.method in ('POST', 'PUT'):
            kwargs.update({
                'data': self.request.POST,
                'files': self.request.FILES,
            })
        return kwargs

    def form_valid(self, form, formset):
        self.object = form.save()
        formset.instance = self.object
        formset.save()
        if hasattr(self, 'get_success_message'):
            self.get_success_message(form)
        return redirect(self.object.get_absolute_url())

    def form_invalid(self, form, formset):
        return self.render_to_response(self.get_context_data(form=form, formset=formset))



class DashboardView(generic.TemplateView):
    template_name = 'core/dashboard.html'
    
    def get_context_data(self, **kwargs):
        context = super(DashboardView, self).get_context_data(**kwargs)
        context['person_count'] = Person.objects.count()
        context['identity_count'] = Identity.objects.count()
        context['ldap_count'] = LDAPConfiguration.objects.count()
        context['project_count'] = Project.objects.count()
        context['email_test_count'] = EmailTest.objects.count()
        context['twitter_test_count'] = TwitterTest.objects.count()
        return context
