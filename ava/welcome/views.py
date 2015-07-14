import logging

import django.views.generic.edit
import django.views.generic.base
from django.db import transaction
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User

from . import forms

from ava.import_ldap import forms as import_ldap_forms

log = logging.getLogger(__name__)


class CreateFirstUser(django.views.generic.edit.FormView):
    template_name = 'welcome/create_first_user.html'
    form_class = forms.CreateFirstSuperUser
    success_url = reverse_lazy('welcome-import-selection')

    def form_valid(self, form):
        # create the new superuser as described in the form
        user = form.save()

        # Now use the data from the same form to authenticate() and
        # login(). This looks weird, but it's required to set the
        # correct auth_backend. See the link for details:
        # https://docs.djangoproject.com/en/1.8/topics/auth/default/#django.contrib.auth.login
        user = authenticate(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password1']
        )
        login(self.request, user)

        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add a conventient template context variable to know if the
        # form should be visible.
        context['no_users_exist'] = not User.objects.exists()
        return context


class ImportSelection(django.views.generic.base.TemplateView):
    template_name = 'welcome/import_selection.html'


class ImportLDAP(django.views.generic.edit.FormView):
    template_name = 'welcome/import_ldap.html'
    success_url = reverse_lazy('welcome-import-progress')

    # This is temporary: Soon we'll want to create our own form class here
    # instead of reusing the ModelForm, this will happen when we remove the
    # password-saving part.
    form_class = import_ldap_forms.LDAPConfigurationForm

    def form_valid(self, form):
        return self.run_ldap_import(form)

    def run_ldap_import(self, form):
        """Run the LDAP Import using the form.

        We wrap the operation in a transaction, and run the import. If
        the import fails, we roll back the transaction, insert an
        error into the form's error list, and call the view's
        'form_invalid' views.

        Before you ask: Yeah, this is weird.

        But it saves us a lot of trouble with error-handling during
        the import:

        - We get bounced back to the LDAP wizard step, with a useful
          error message.

        - The LDAP configuration is not saved to the database, so
          we're not left in an inconsistent state, the user can
          simply try again.

        """
        try:
            # enter the transaction.
            with transaction.atomic():
                # save the form.
                form.save()
                # run the LDAP import
                form.instance.import_all()

            # If we got here, then the import succeeded, and the transaction
            # has committed the results.
            return super().form_valid(form)

        except Exception as e:
            # Something went wrong, the transaction has already rolled
            # back. We log the exception, insert an error into the
            # form's errorlist, and trigger the 'invalid_form' view
            # path to return the customer to the LDAP configuration
            # screen.
            log.exception("Error during LDAP import.", exc_info=e)
            form.add_error(
                field=None,
                error="Sorry, an error occurred during LDAP import. See the debug log for details"
            )
            # And now finish the view using form_invalid, as if it was a bad form all along.
            return self.form_invalid(form)


class ImportProgress(django.views.generic.base.TemplateView):
    template_name = 'welcome/import_progress.html'
