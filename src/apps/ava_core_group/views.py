from django.core.urlresolvers import reverse
from django.views.generic import CreateView, ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView
from django.db.models import Count

from apps.ava_core_group.models import Group
from apps.ava_core_group.forms import GroupForm


class GroupIndex(ListView):
    template_name = 'group/group_index.html'
    context_object_name = 'group_list'
    model = Group

    def get_queryset(self):
        return Group.objects.annotate(identity_count=Count('identities')).order_by('name', 'group_type')


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
