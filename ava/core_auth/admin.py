from django.contrib import admin

from ava.core_auth.models import UserRights, Team


admin.site.register(UserRights)
admin.site.register(Team)
