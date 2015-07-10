import django.forms

from ava.import_ldap.models import LDAPConfiguration


class LDAPConfigurationForm(django.forms.ModelForm):

    class Meta:
        model = LDAPConfiguration
        fields = ('user_dn', 'user_pw', 'dump_dn', 'server')
        widgets = {
            'user_pw': django.forms.PasswordInput(),
        }
