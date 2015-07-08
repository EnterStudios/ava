import django.views.generic.edit
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User

from . import forms


class CreateFirstUser(django.views.generic.edit.FormView):
    template_name = 'welcome/create_first_user.html'
    form_class = forms.CreateFirstSuperUser

    # TODO: Determine where to send the user after creation, set
    #       to the dashboard at the moment but later might be
    #       'step 2' of the first-use wizard.
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        # create the new superuser as described in the form
        user = form.save()

        # Now use the data from the same form to authenticate() and
        # login(). This looks weird, but it's required to set the
        # correct auth_backend. See the link for details:
        # https://docs.djangoproject.com/en/1.8/topics/auth/default/#django.contrib.auth.login
        user = authenticate(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password1']
        )
        login(self.request, user)

        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add a conventient template context variable to know if the
        # form should be visible.
        context['no_users_exist'] = not User.objects.exists()
        return context
