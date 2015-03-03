from django.contrib import admin

from apps.ava_core_group.models import Group, GroupType


admin.site.register(Group)
admin.site.register(GroupType)