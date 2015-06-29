from django.forms import ModelForm

from apps.ava_core_google_apps.models import GoogleConfiguration


class GoogleConfigurationForm(ModelForm):
    class Meta:
        model = GoogleConfiguration
