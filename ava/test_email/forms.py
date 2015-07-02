from django.forms import ModelForm

from . import models


class EmailTestForm(ModelForm):

    class Meta:
        model = models.EmailTest
        exclude = ['project', 'user', 'test_status', 'test_type', 'redirect_url', 'page_template']
        labels = {
            'name': 'Test Name',
            'description': 'Test Description',
        }


class EmailTargetForm(ModelForm):

    class Meta:
        model = models.EmailTestTarget
        exclude = []
