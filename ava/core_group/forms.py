from django.forms import ModelForm

from ava.core_group.models import Group


class GroupForm(ModelForm):
    class Meta:
        model = Group
        exclude = []
