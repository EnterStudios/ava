from django.forms import ModelForm

from apps.ava_core_project.models import Project, ProjectTeam


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ('name', 'description')


class ProjectTeamForm(ModelForm):
    class Meta:
        model = ProjectTeam
        fields = ('accesslevel',)
