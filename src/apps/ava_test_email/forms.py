from django.forms import ModelForm

from apps.ava_test_email.models import *


class EmailTestForm(ModelForm):
    class Meta:
        model = EmailTest
        exclude = ['project','user','teststatus', 'testtype','redirect_url','page_template']
        labels = {
            'name':('Test Name'),
            'description':('Test Description'),
        }


class EmailTargetForm(ModelForm):
    class Meta:
        model = EmailTestTarget
        exclude = []
