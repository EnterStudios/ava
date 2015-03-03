from django.core.urlresolvers import reverse
from django.views.generic import CreateView, ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView

from apps.ava_core_group.models import Group, GroupType
from apps.ava_core_group.forms import GroupForm, GroupTypeForm


class GroupIndex(ListView):
    template_name = 'group/group_index.html'
    context_object_name = 'group_list'
    model = Group

    def get_queryset(self):
        return Group.objects.all()


class GroupDetail(DetailView):
    model = Group
    context_object_name = 'group'
    template_name = 'group/group_detail.html'


class GroupCreate(CreateView):
    template_name = 'group/group.html'
    model = Group
    form_class = GroupForm


class GroupUpdate(UpdateView):
    template_name = 'group/group.html'
    context_object_name = 'group'
    model = Group
    form_class = GroupForm


class GroupDelete(DeleteView):
    model = Group
    template_name = 'confirm_delete.html'

    def get_success_url(self):
        return reverse('index')


class GroupTypeIndex(ListView):
    template_name = 'group/group_type_index.html'
    context_object_name = 'group_type_list'
    model = GroupType

    def get_queryset(self):
        return GroupType.objects.all()


class GroupTypeDetail(DetailView):
    model = GroupType
    context_object_name = 'group_type'
    template_name = 'group/group_type_detail.html'


class GroupTypeCreate(CreateView):
    template_name = 'group/group_type.html'
    model = GroupType
    form_class = GroupTypeForm


class GroupTypeUpdate(UpdateView):
    template_name = 'group/group_type.html'
    context_object_name = 'group_type'
    model = GroupType
    form_class = GroupTypeForm


class GroupTypeDelete(DeleteView):
    model = GroupType
    template_name = 'confirm_delete.html'

    def get_success_url(self):
        return reverse('index')