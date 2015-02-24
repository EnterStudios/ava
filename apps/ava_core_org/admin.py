from django.contrib import admin

from apps.ava_core_org.models import *


admin.site.register(Organisation)
admin.site.register(OrganisationGroup)
admin.site.register(GroupIdentifier)

