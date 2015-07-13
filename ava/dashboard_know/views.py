from django.shortcuts import get_object_or_404
from django.views import generic
from ava.import_ldap.models import LDAPConfiguration, ActiveDirectoryUser


class KnowDashboardView(generic.ListView):
    template_name = 'know/dashboard.html'
    model = LDAPConfiguration
    context_object_name = 'list'

    def get_context_data(self, **kwargs):
        context = super(KnowDashboardView, self).get_context_data(**kwargs)
        # context['ldap_users_count'] =
        pk = self.kwargs.get('pk')
        if pk:
            ldap_config = get_object_or_404(LDAPConfiguration, pk=pk)
            context['ldap_config'] = ldap_config
        context['ldap_admins'] = self.get_admins(ldap_config)


        return context

    def get_admins(self, ldap_config):
        return ActiveDirectoryUser.objects.filter(ldap_configuration=ldap_config,)

    def get_account_never_expires(self, ldap_config):
        pass

    def get_never_logged_in(self, ldap_config):
        pass

    def get_oldest_password(self, ldap_config):
        pass

    def get_logon_count(self, ldap_config):
        pass
