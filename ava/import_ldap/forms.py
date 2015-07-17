import logging

import django.forms
from django.db import transaction

from ava.import_ldap.models import LDAPConfiguration


log = logging.getLogger(__name__)


class LDAPConfigurationForm(django.forms.ModelForm):

    class Meta:
        model = LDAPConfiguration
        fields = ('dump_dn', 'server')


class LDAPConfigurationCredentialsForm(LDAPConfigurationForm):
    user_dn = django.forms.CharField(max_length=100, help_text='User (not saved)')
    user_pw = django.forms.CharField(max_length=100, help_text='Password (not saved)')

    class Meta(LDAPConfigurationForm.Meta):
        widgets = {
            'user_pw': django.forms.PasswordInput(),
        }

    def run_ldap_import(self):
        """Run the LDAP Import using the form.

        We wrap the operation in a transaction, and run the import. If
        the import fails, we roll back the transaction and insert an
        error into the form's error list, the view can then return the
        form_invalid response.

        Before you ask: Yeah, this is weird.

        But it saves us a lot of trouble with error-handling during
        the import:

        - We get bounced back to the LDAP wizard step, with a useful
          error message.

        - The LDAP configuration is not saved to the database, so
          we're not left in an inconsistent state, the user can
          simply try again.

        Returns 'True' if the import appeared to succeed, and 'False'
        if something went wrong (while also inserting an error into
        the form object.

        """
        try:
            # enter the transaction.
            with transaction.atomic():
                # save the form.
                self.save()
                # run the LDAP import
                self.instance.import_all(
                    user_dn=self.cleaned_data['user_dn'],
                    user_pw=self.cleaned_data['user_dn'],
                )
            # At the moment 'no exception being thrown' is the best
            # measure for success we have, so if we got here, it
            # must have worked.
            return True

        except Exception as e:
            # Something went wrong, the transaction has already rolled
            # back. We log the exception, insert an error into the
            # form's errorlist, and trigger the 'invalid_form' view
            # path to return the customer to the LDAP configuration
            # screen.
            log.exception("Error during LDAP import.", exc_info=e)
            self.add_error(
                field=None,
                error="Sorry, an error occurred during LDAP import. See the debug log for details"
            )
            return False
