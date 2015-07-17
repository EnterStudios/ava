from django.forms import ModelForm

from ava.import_google.models import GoogleConfiguration


class GoogleConfigurationForm(ModelForm):

    class Meta:
        model = GoogleConfiguration
