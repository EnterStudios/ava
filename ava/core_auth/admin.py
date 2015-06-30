from django.contrib import admin

from apps.ava_core_auth.models import UserRights, Team


admin.site.register(UserRights)
admin.site.register(Team)
