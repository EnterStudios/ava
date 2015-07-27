# flake8: noqa

from django.shortcuts import get_object_or_404
from django.views import generic
from ava.core_group.models import Group
from ava.core_identity.models import Person, Identity
from ava.import_ldap.models import LDAPConfiguration
from ava.import_ldap.stats_interface import LDAPStatistics

class KnowDashboardView(generic.ListView):
    template_name = 'know/dashboard.html'
    model = LDAPConfiguration
    context_object_name = 'list'

    def get_context_data(self, **kwargs):
        context = super(KnowDashboardView, self).get_context_data(**kwargs)
        pk = self.kwargs.get('pk')
        if pk:
            ldap_config = get_object_or_404(LDAPConfiguration, pk=pk)
            context['ldap'] = LDAPStatistics().get_stats(ldap_config)
            context['person_count'] = Person.objects.count()
            context['identity_count'] = Identity.objects.count()
            context['group_count'] = Group.objects.count()
        return context
