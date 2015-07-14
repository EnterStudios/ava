import django.forms

from django.contrib.auth import forms as auth_forms
from django.contrib.auth import models as auth_models


class CreateFirstSuperUser(auth_forms.UserCreationForm):
    # TODO: add any other interesting fields other than the defaults
    #       (username and password).

    def clean(self):
        # This form must never be 'valid' if any other users exist in
        # the system. It's a one-off for first-time AVA use.
        if auth_models.User.objects.exists():
            raise django.forms.ValidationError(
                'Initial user already exists.'
            )
        return super().clean()

    def save(self, commit=True):
        assert self.is_valid(), "Attempted to call save() on invalid form"

        # Use the superclass's save() but don't commit to the db yet.
        user = super().save(commit=False)

        # Set the elevated privileges.
        user.is_staff = True
        user.is_superuser = True

        # and *now* commit to the DB.
        if commit:
            user.save()
        return user
