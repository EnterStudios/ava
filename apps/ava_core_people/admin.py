from django.contrib import admin

from apps.ava_core_people.models import Person, Identifier


admin.site.register(Person)
admin.site.register(Identifier)
