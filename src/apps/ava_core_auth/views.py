from django.views import generic
from django.db.models import Count, Q
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.shortcuts import redirect
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
        return reverse('user-detail', kwargs={'pk':self.object.id})


class UserUpdate(generic.UpdateView):
    model = User
    template_name = 'auth/user.html'
    context_object_name = 'user'
    form_class = UserUpdateForm
    
    def get_success_url(self):
        return reverse('user-detail', kwargs={'pk':self.object.id})


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


class TeamAddMembers(generic.DetailView):
    model = Team
    template_name = 'auth/team_addmembers.html'
    context_object_name = 'team'
    
    CONTEXT_ATTRIBUTES = ['user_list', 'search_term']
    
    def get_context_data(self, **kwargs):
        context_data = super(TeamAddMembers, self).get_context_data(**kwargs)
        if hasattr(self, 'user_list'):   context_data['user_list'] = self.user_list
        if hasattr(self, 'search_term'): context_data['search_term'] = self.search_term
        return context_data
    
    def get_user_list(self, search_term=None):
        # If no search term is provided, just list the first 20 users.
        if not search_term:
            return User.objects.all()[:20]
        # If there is a search term, look for it in the username, first name,
        # last name and emaila ddress.
        search_filter = Q(
                            username__contains=search_term
                        )|Q(
                            first_name__contains=search_term
                        )|Q(
                            last_name__contains=search_term
                        )|Q(
                            email__contains=search_term
                        )
        return User.objects.filter(search_filter)
    
    def add_users(self, user_id_list):
        users = User.objects.filter(id__in=user_id_list)
        self.object.users.add(*users.all())
    
    def get(self, request, *args, **kwargs):
        if 'search' in request.GET:
            self.search_term = request.GET.get('search')
            self.user_list = self.get_user_list(self.search_term)
        else:
            self.user_list = self.get_user_list()
        # Display the view.
        return super(TeamAddMembers, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        if 'user' in request.POST:
            self.add_users(request.POST.getlist('user'))
        return redirect(reverse('team-detail', kwargs={'pk':self.object.id}))


class TeamRemoveMembers(generic.DetailView):
    model = Team
    template_name = 'auth/team_removemembers.html'
    context_object_name = 'team'
    
    CONFIRMATION_VALUE = 'yes'
    
    def get_user_list(self, request):
        user_ids = []
        # If the user list is in the POST request, pull the IDs out.
        if request.POST and 'user' in request.POST:
            user_ids = request.POST.getlist('user')
        # If not, use the ID passed in via the URL.
        elif 'user' in request.resolver_match.kwargs:
            user_ids.append(request.resolver_match.kwargs.get('user'))
        # Return all current members matching the IDs.
        return self.object.users.filter(id__in=user_ids)
    
    def display_users(self, request):
        context = {
                   'confirm': self.CONFIRMATION_VALUE,
                   'user_list': self.get_user_list(request),
                   }
        return self.render_to_response(self.get_context_data(**context))
    
    def remove_users(self, request):
        user_list = self.get_user_list(request)
        self.object.users.remove(*user_list.all())
    
    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        return self.display_users(request)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        # If the user has confirmed removal, do the removal.
        if 'confirm' in request.POST and request.POST.get('confirm') == self.CONFIRMATION_VALUE:
            self.remove_users(request)
            return redirect(reverse('team-detail', kwargs={'pk':self.object.id}))
        # If not, render the page as if this was a GET request.
        return self.display_users(request)
    
