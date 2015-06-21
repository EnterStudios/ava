from django.contrib import admin

# Register your models here.
from apps.ava_core_google_apps.models import GoogleDirectoryUser, GoogleDirectoryGroup,GoogleConfiguration

admin.site.register(GoogleDirectoryUser)
admin.site.register(GoogleDirectoryGroup)
admin.site.register(GoogleConfiguration)
