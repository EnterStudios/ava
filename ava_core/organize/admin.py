from django.contrib import admin

from .models import Person, PersonIdentifier, Group, GroupIdentifier, PersonAttribute, PersonIdentifierAttribute, \
    GroupIdentifierAttribute, PersonIdentifierReport, GroupReport

admin.site.register(Person)
admin.site.register(PersonAttribute)
admin.site.register(PersonIdentifier)
admin.site.register(PersonIdentifierReport)
admin.site.register(PersonIdentifierAttribute)
admin.site.register(Group)
admin.site.register(GroupIdentifier)
admin.site.register(GroupIdentifierAttribute)
admin.site.register(GroupReport)
