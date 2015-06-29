from django.views import generic
from django.db.models import Count, Q
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.shortcuts import redirect
from apps.ava_core.views import AddManyToManyView, RemoveManyToManyView
from apps.ava_core_auth.models import Team
from apps.ava_core_auth.forms import UserCreateForm, UserUpdateForm, TeamForm


class UserIndex(generic.ListView):
    model = User
    template_name = 'auth/user_index.html'
    context_object_name = 'user_list'

    def get_queryset(self):
        return User.objects.select_related('rights')


class UserDetail(generic.DetailView):
    model = User
    template_name = 'auth/user_detail.html'
    context_object_name = 'view_user'

    def get_object(self, queryset=None):
        queryset = queryset or User.objects
        pk = self.kwargs[self.pk_url_kwarg]
        return queryset.select_related('rights', 'teams').get(pk=pk)


class UserCreate(generic.CreateView):
    model = User
    template_name = 'auth/user.html'
    context_object_name = 'user'
    form_class = UserCreateForm

    def get_success_url(self):
        return reverse('user-detail', kwargs={'pk': self.object.id})


class UserUpdate(generic.UpdateView):
    model = User
    template_name = 'auth/user.html'
    context_object_name = 'user'
    form_class = UserUpdateForm

    def get_success_url(self):
        return reverse('user-detail', kwargs={'pk': self.object.id})


class UserDelete(generic.DeleteView):
    model = User
    template_name = 'confirm_delete.html'

    def get_success_url(self):
        return reverse('user-index')


class TeamIndex(generic.ListView):
    model = Team
    template_name = 'auth/team_index.html'
    context_object_name = 'team_list'

    def get_queryset(self):
        return Team.objects.annotate(member_count=Count('users'))


class TeamDetail(generic.DetailView):
    model = Team
    template_name = 'auth/team_detail.html'
    context_object_name = 'team'

    def get_object(self, queryset=None):
        queryset = queryset or Team.objects
        pk = self.kwargs[self.pk_url_kwarg]
        return queryset.select_related('users').get(pk=pk)


class TeamCreate(generic.CreateView):
    model = Team
    template_name = 'auth/team.html'
    context_object_name = 'team'
    form_class = TeamForm

    def get_success_url(self):
        return self.object.get_absolute_url()


class TeamUpdate(generic.UpdateView):
    model = Team
    template_name = 'auth/team.html'
    context_object_name = 'team'
    form_class = TeamForm

    def get_success_url(self):
        return self.object.get_absolute_url()


class TeamDelete(generic.DeleteView):
    model = Team
    template_name = 'confirm_delete.html'

    def get_success_url(self):
        return reverse('team-index')


class TeamAddMembers(AddManyToManyView):
    template_name = 'auth/team_addmembers.html'
    model = Team
    target_model = User
    context_object_name = 'team'
    targets_context_object_name = 'user_list'
    target_id_field = 'user'

    def search_targets(self, target_queryset, search_term):
        search_filter = Q(username__icontains=search_term
                          ) | Q(first_name__icontains=search_term
                                ) | Q(last_name__icontains=search_term
                                      ) | Q(email__icontains=search_term
                                            )
        return target_queryset.filter(search_filter)

    def get_many_to_many(self):
        return self.object.users

    def order_target_queryset(self, target_queryset):
        return target_queryset.order_by('username')


class TeamRemoveMembers(RemoveManyToManyView):
    template_name = 'auth/team_removemembers.html'
    model = Team
    context_object_name = 'team'
    targets_context_object_name = 'user_list'
    target_post_field = 'user'
    target_kwargs_field = 'user'

    def get_many_to_many(self):
        return self.object.users

    def order_target_list(self, target_list):
        return target_list.order_by('username')
