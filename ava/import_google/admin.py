from django.contrib import admin

# Register your models here.
import ava.import_google.models

admin.site.register(ava.import_google.models.GoogleDirectoryUser)
admin.site.register(ava.import_google.models.GoogleDirectoryGroup)
admin.site.register(ava.import_google.models.GoogleConfiguration)
