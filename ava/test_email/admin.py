from django.contrib import admin

from . import models

admin.site.register(models.EmailTest)
admin.site.register(models.EmailTestTarget)
admin.site.register(models.EmailTemplate)
