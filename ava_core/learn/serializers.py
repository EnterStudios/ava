import logging

from rest_framework import serializers

from .models import Role, Module, Path

log = logging.getLogger(__name__)


class RoleSerializer(serializers.ModelSerializer):
    path = serializers.PrimaryKeyRelatedField(queryset=Path.objects.all(), many=True)

    class Meta:
        model = Role
        fields = ('id', 'name', 'description', 'path')


class ModuleSerializer(serializers.ModelSerializer):
    parent = serializers.PrimaryKeyRelatedField(queryset=Module.objects.all(), many=False, required=False)
    path = serializers.PrimaryKeyRelatedField(queryset=Path.objects.all(), many=True)

    class Meta:
        model = Module
        fields = ('id', 'name', 'description', 'module_url', 'parent', 'path')


class PathSerializer(serializers.ModelSerializer):
    path_modules = serializers.PrimaryKeyRelatedField(queryset=Module.objects.all(), many=True)
    path_roles = serializers.PrimaryKeyRelatedField(queryset=Role.objects.all(), many=True)

    class Meta:
        model = Path
        fields = ('id', 'name', 'description', 'path_modules', 'path_roles')
