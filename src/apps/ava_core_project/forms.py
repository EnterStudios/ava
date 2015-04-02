from django.forms import ModelForm

from apps.ava_core_project.models import Project, ProjectTeam
from django.forms.models import inlineformset_factory


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ('name', 'description')
        #exclude = []


class ProjectTeamForm(ModelForm):
    class Meta:
        model = ProjectTeam
        fields = ('accesslevel',)
