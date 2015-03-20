from django.forms import ModelForm

from apps.ava_test_email.models import *


class EmailTestForm(ModelForm):
    class Meta:
        model = EmailTest
        exclude = ['user','teststatus', 'testtype']


class EmailTargetForm(ModelForm):
    class Meta:
        model = EmailTestTarget
        exclude = []
