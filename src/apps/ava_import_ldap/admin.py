from django.contrib import admin

# Register your models here.
from apps.ava_import_ldap.models import ActiveDirectoryUser, ActiveDirectoryGroup,LDAPConfiguration

admin.site.register(ActiveDirectoryUser)
admin.site.register(ActiveDirectoryGroup)
admin.site.register(LDAPConfiguration)
