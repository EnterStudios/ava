from django.shortcuts import redirect
from django.views import generic
from django.utils import safestring, html
from django.db.models import Model
from ava.core_identity.models import Person, Identity
from ava.import_ldap.models import LDAPConfiguration
from ava.core_project.models import Project
from ava.test_email.models import EmailTest
from ava.test_twitter.models import TwitterTest


class FormsetMixin(object):

    """
    This is a generic mixin to provide clean functionality for creating and updating related models via FormSet
    This mixin can be inherited and used as an alternative to generic.CreateView and generic.UpdateView

    Example:

    class PersonCreate(FormsetMixin, CreateView):
        template_name = 'identity/person.html'
        model = Person
        form_class = PersonForm
        formset_class = IdentifierFormSet
    """

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


class AddManyToManyView(generic.DetailView):

    """
    A sublass of DetailView that specialises in adding items to a many to
    many relationship between models.

    Example:

    class PersonAddIdentities(AddManyToManyView):
        template_name = 'person/person_addidentities.html'
        model = Person
        target_model = Identity
        context_object_name = 'person'
        targets_context_object_name = 'identity_list'
        target_id_field = 'identity'

        def search_targets(self, target_queryset, search_term):
            return target_queryset.filter(name__contains=search_term)

        def get_many_to_many(self):
            return self.object.identities
    """
    # Values that may be overridden in subclasses
    target_model = None
    targets_context_object_name = 'target_list'
    target_search_field = 'search'
    target_id_field = 'add'
    target_default_items = 20
    default_limited_message_class = 'alert alert-info'
    default_limited_message = 'The first {0} items are displayed. Search to return more items.'

    def get_target_queryset(self):
        """
        Gets the query set that will be used to search for targets to add.
        """
        if not issubclass(self.target_model, Model):
            raise AssertionError("target_model must be a model type")
        return self.target_model.objects

    def order_target_queryset(self, target_queryset):
        """
        Orders the items in the target query set for display.
        :param target_queryset: The query set of items to order.
        :returns The ordered query set.
        """
        return target_queryset

    def search_targets(self, target_queryset, search_term):
        """
        Searches the query set for items matching the supplied search term.
        :param target_queryset: A query set containing possible targets to add.
        :param search_term: A value to search for within the query set.
        """
        raise NotImplementedError('Must implement get_target_queryset_filter(self, search_term)')

    def get_many_to_many(self):
        """
        Gets the field that represents the many-to-many relationship.
        """
        raise NotImplementedError('Must implement get_many_to_many(self)')

    def get_success_url(self):
        """
        Gets the URL that will be displayed when the target members are removed.
        """
        return self.object.get_absolute_url()

    def get_target_list(self, search_term=None):
        """
        Gets a list of target items to choose from.
        :param search_term: A search term to filter items. If this is not set,
                    a default set of items will be returned.
        """
        queryset = self.order_target_queryset(self.get_target_queryset())
        if search_term:
            return self.search_targets(queryset, search_term)
        elif self.target_default_items > 0:
            if queryset.count() > self.target_default_items:
                self.default_results_limited = True
            return queryset.all()[:self.target_default_items]
        else:
            return None

    def order_target_list(self, target_list):
        """
        Orders the items in the target list for display.
        :param target_list: The list of items to order. Unless
                    the get_target_list method has been modified, this value
                    will be a query set.
        """
        return target_list

    def add_targets(self, target_ids):
        """
        Adds targets to the many-to-many relationship.
        :param target_ids: The identifiers of the target items to add.
        """
        targets = self.get_target_queryset().filter(id__in=target_ids)
        self.get_many_to_many().add(*targets.all())

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        # Get the current search term.
        search_term = ''
        if self.target_search_field in request.GET:
            search_term = request.GET.get(self.target_search_field)
        # Build the default context.
        context = {
            'search_term': search_term,
            self.targets_context_object_name: self.get_target_list(search_term)
        }
        # If the default result list is being truncated, add a relevant message.
        if getattr(self, 'default_results_limited', False):
            message = self.default_limited_message.format(self.target_default_items)
            message_display = '<div class="{0}">{1}</div>'.format(
                self.default_limited_message_class,
                html.escape(message),
            )
            context['default_results_message'] = safestring.mark_safe(message_display)
        # Render the page.
        return self.render_to_response(self.get_context_data(**context))

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        # Get the URL to redirect to when we're done. By convention, this is
        # obtained before any changes are made.
        success_url = self.get_success_url()
        # If the post data contains the IDs of targets to add, add them.
        if self.target_id_field in request.POST:
            target_ids = request.POST.getlist(self.target_id_field)
            self.add_targets(target_ids)
        # Redirect to the success URL.
        return redirect(success_url)


class RemoveManyToManyView(generic.DetailView):

    """
    A sublass of DetailView that specialises in removing items from a many to
    many relationship between models.

    Example:

    class PersonRemoveIdentities(RemoveManyToManyView):
        template_name = 'person/person_removeidentities.html'
        model = Person
        context_object_name = 'person'
        targets_context_object_name = 'identity_list'
        target_post_field = 'identity'
        target_kwargs_field = 'identity'

        def get_many_to_many(self):
            return self.object.identities
    """
    # Values that may be overridden in subclasses
    targets_context_object_name = 'remove_list'
    target_post_field = 'remove'
    target_kwargs_field = 'remove'

    # Constants
    CONFIRM_FIELD = 'confirm'
    CONFIRM_VALUE = 'yes'
    CONFIRM_INPUT = '<input type="hidden" name="{0}" value="{1}" />'

    def get_many_to_many(self):
        """
        Gets the field that represents the many-to-many relationship.
        """
        raise NotImplementedError('Must implement get_many_to_many(self)')

    def get_success_url(self):
        """
        Gets the URL that will be displayed when the target members are removed.
        """
        return self.object.get_absolute_url()

    def get_target_ids(self, request):
        """
        Gets the list of identifier for the targets to remove from the
        many-to-many relationship.
        :param request: The incoming HTTP request.
        """
        target_ids = []
        # If the user list is in the POST request, pull the IDs out.
        if request.POST and self.target_post_field in request.POST:
            target_ids = request.POST.getlist(self.target_post_field)
        # If not, use the ID passed in via the URL.
        elif self.target_kwargs_field in request.resolver_match.kwargs:
            target_ids.append(request.resolver_match.kwargs.get(self.target_kwargs_field))
        return target_ids

    def get_target_list(self, request):
        """
        Gets the list of targets to remove from the many-to-many relationship.
        :param request: The incoming HTTP request.
        """
        # Return all current members matching the target IDs.
        target_ids = self.get_target_ids(request)
        return self.get_many_to_many().filter(id__in=target_ids)

    def order_target_list(self, target_list):
        """
        Orders the items in the target list for display.
        :param target_list: The list of items to order. Unless
                    the get_target_list method has been modified, this value
                    will be a query set.
        :returns The ordered list.
        """
        return target_list

    def confirm_targets_to_remove(self, request):
        """
        Confirms the list of targets to remove from the many-to-many relationship.
        If there are no valid targets or a single valid target, it will be
        removed immediately.
        :param request: The incoming HTTP request.
        """
        # Do a quick check on the number of users. If there's only one, just
        # remove them immediately.
        target_list = self.get_target_list(request)
        if target_list.count() <= 1:
            return self.remove_targets_and_return(request)
        # If there's more than one user, display a list.
        confirm_input = safestring.mark_safe(self.CONFIRM_INPUT.format(self.CONFIRM_FIELD, self.CONFIRM_VALUE))
        context = {
            'confirm': confirm_input,
            self.targets_context_object_name: self.order_target_list(target_list),
        }
        return self.render_to_response(self.get_context_data(**context))

    def remove_targets(self, request):
        """
        Removes targets from the many-to-many relationship.
        :param request: The incoming HTTP request.
        """
        # Find the list or targets and remove them.
        target_list = self.get_target_list(request)
        self.get_many_to_many().remove(*target_list.all())

    def remove_targets_and_return(self, request):
        # Get the URL to redirect to when we're done. By convention, this is
        # obtained before any changes are made.
        success_url = self.get_success_url()
        # Remove the targets.
        self.remove_targets(request)
        # Redirect to the success URL.
        return redirect(success_url)

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        return self.confirm_targets_to_remove(request)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        # If the user has confirmed removal, do the removal.
        if self.CONFIRM_FIELD in request.POST and request.POST.get(self.CONFIRM_FIELD) == self.CONFIRM_VALUE:
            return self.remove_targets_and_return(request)
        # If not, render the page as if this was a GET request.
        return self.confirm_targets_to_remove(request)


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
