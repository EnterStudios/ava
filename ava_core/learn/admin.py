from django.contrib import admin

from .models import Path, Module, Role

admin.site.register(Path)
admin.site.register(Module)
admin.site.register(Role)
