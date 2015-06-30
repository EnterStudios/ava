from django.forms import ModelForm

from apps.ava_core_group.models import Group


class GroupForm(ModelForm):
    class Meta:
        model = Group
        exclude = []
