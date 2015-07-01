from django.forms import ModelForm

from ava.test_email.models import *


class EmailTestForm(ModelForm):
    class Meta:
        model = EmailTest
        exclude = ['project', 'user', 'test_status', 'test_type', 'redirect_url', 'page_template']
        labels = {
            'name': 'Test Name',
            'description': 'Test Description',
        }


class EmailTargetForm(ModelForm):
    class Meta:
        model = EmailTestTarget
        exclude = []
