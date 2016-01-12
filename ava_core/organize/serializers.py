import logging

from rest_framework import serializers

from ava_core.abstract.validators import GenericTogetherValidator
from .models import PersonIdentifier, Person, Group, GroupIdentifier, PersonAttribute, PersonIdentifierAttribute, \
    GroupIdentifierAttribute, PersonIdentifierReport, GroupReport

log = logging.getLogger(__name__)


class GroupIdentifierSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupIdentifier
        fields = ('id', 'identifier', 'identifier_type', 'belongs_to')
        validators = [GenericTogetherValidator(queryset=GroupIdentifier.objects.all(),
                                               query_fields={
                                                   'identifier': '_iexact',
                                                   'identifier_type': '_iexact',
                                                   'belongs_to': 'id'
                                               },
                                               message='Identifier with this name and type already exists.')]


class GroupMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ('id', 'first_name', 'surname')


class GroupSerializer(serializers.ModelSerializer):
    members = GroupMemberSerializer(read_only=True, many=True)
    group_ids = GroupIdentifierSerializer(read_only=True, many=True)

    class Meta:
        model = Group
        fields = (
            'id', 'name', 'description', 'group_type', 'parent', 'google_group_data', 'ldap_group_data',
            'members', 'group_ids')
        validators = [GenericTogetherValidator(queryset=Group.objects.all(),
                                               query_fields={
                                                   'name': '_iexact',
                                                   'group_type': '_iexact'
                                               },
                                               message='Group with this name and type already exists.')]


class PersonIdentifierSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonIdentifier
        fields = ('id', 'identifier', 'identifier_type', 'belongs_to')
        validators = [GenericTogetherValidator(queryset=PersonIdentifier.objects.all(),
                                               query_fields={
                                                   'identifier': '_iexact',
                                                   'identifier_type': '_iexact',
                                                   'belongs_to': 'id'
                                               },
                                               message='Identifier with this name and type already exists.')]


class PersonSerializer(serializers.ModelSerializer):
    groups = GroupSerializer(many=True, read_only=True)
    person_ids = PersonIdentifierSerializer(read_only=True, many=True)

    class Meta:
        model = Person
        fields = (
            'id', 'first_name', 'surname', 'groups', 'google_identity_data', 'ldap_identity_data', 'person_ids')


class PersonAttributeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonAttribute
        fields = ('person', 'non_human')


class PersonIdentifierAttributeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonIdentifierAttribute
        fields = ('id', 'created', 'modified', 'identifier', 'ignore_type')


class GroupIdentifierAttributeSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupIdentifierAttribute
        fields = ('id', 'created', 'modified', 'identifier', 'ignore_type')


class PersonIdentifierReportSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.email')
    is_resolved = serializers.ReadOnlyField()

    class Meta:
        model = PersonIdentifierReport
        fields = (
            'id', 'created', 'modified', 'owner', 'identifier', 'reason_type', 'priority_type', 'description',
            'is_resolved')


class GroupReportSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.email')
    is_resolved = serializers.ReadOnlyField()

    class Meta:
        model = GroupReport
        fields = (
            'id', 'created', 'modified', 'owner', 'group', 'reason_type', 'priority_type', 'description',
            'is_resolved')
