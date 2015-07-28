from django.db import transaction
from django.forms import ModelForm
from pip.utils import logging

from ava.import_google.models import GoogleConfiguration

log = logging.getLogger(__name__)

class GoogleConfigurationForm(ModelForm):

    class Meta:
        model = GoogleConfiguration


class GoogleConfigurationForm(ModelForm):
    class Meta:
        model = GoogleConfiguration

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
            log.exception("Error during Google import.", exc_info=e)
            self.add_error(
                field=None,
                error="Sorry, an error occurred during Google import. See the debug log for details"
            )
            return False