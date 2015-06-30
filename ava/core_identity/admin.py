from django.contrib import admin

from ava.core_identity.models import Identity, Person, Identifier


admin.site.register(Identity)
admin.site.register(Person)
admin.site.register(Identifier)
