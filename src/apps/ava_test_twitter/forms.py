from django.forms import ModelForm

from apps.ava_test_twitter.models import *


class TwitterTestForm(ModelForm):
    class Meta:
        model = TwitterTest
        exclude = ['project','user','teststatus', 'testtype','redirect_url','page_template','link']
        labels = {
            'name':('Test Name'),
            'description':('Test Description'),
        }
