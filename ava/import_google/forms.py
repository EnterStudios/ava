from django.forms import ModelForm

from ava.core_google_apps.models import GoogleConfiguration


class GoogleConfigurationForm(ModelForm):
    class Meta:
        model = GoogleConfiguration
