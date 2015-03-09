from django.forms import ModelForm

from apps.ava_core_group.models import Group, GroupType


class GroupForm(ModelForm):
    class Meta:
        model = Group

class GroupTypeForm(ModelForm):
    class Meta:
        model = GroupType