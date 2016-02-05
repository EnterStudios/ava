# Rest Imports
from rest_framework import serializers
# Local Imports
from ava_core.evaluate.models import EvaluateController, EvaluateResult, EvaluateSender, EvaluateTest, \
    EvaluateTemplate
from ava_core.validators import NotBlankWhenTypeValidator
from ava_core.organize.serializers import PersonSerializer

# Implementation
from ava_core.organize.models import Person


class EvaluateSenderSerializer(serializers.ModelSerializer):
    hidden = serializers.ReadOnlyField()

    class Meta:
        model = EvaluateSender
        fields = ('id', 'first_name', 'last_name', 'email_address', 'slack_name', 'hidden')


class EvaluateTemplateSerializer(serializers.ModelSerializer):
    hidden = serializers.ReadOnlyField()

    class Meta:
        model = EvaluateTemplate
        fields = ('id', 'name', 'description', 'template_type', 'email_subject', 'email_body', 'hidden')
        validators = [
            NotBlankWhenTypeValidator('email_subject', 'template_type', EvaluateTemplate.EMAIL),
            NotBlankWhenTypeValidator('email_body', 'template_type', EvaluateTemplate.EMAIL)
        ]


class EvaluateSimpleTargetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ('id', 'first_name', 'surname')


class EvaluateControllerSerializer(serializers.ModelSerializer):
    sender = serializers.PrimaryKeyRelatedField(queryset=EvaluateSender.objects.all(), many=False)
    template = serializers.PrimaryKeyRelatedField(queryset=EvaluateTemplate.objects.all(), many=False)
    targets = serializers.PrimaryKeyRelatedField(queryset=Person.objects.all(), many=True)
    status = serializers.ReadOnlyField()
    expiry_time = serializers.ReadOnlyField()

    class Meta:
        model = EvaluateController
        fields = (
            'id', 'name', 'description', 'scheduled_type', 'scheduled_time', 'expiry_type', 'expiry_time', 'sender',
            'template', 'status', 'targets'
        )


class EvaluateTestSerializer(serializers.ModelSerializer):
    target_controller = EvaluateControllerSerializer(read_only=True, many=True)
    target = PersonSerializer(many=True, read_only=True)
    token = serializers.ReadOnlyField()
    delivery_status = serializers.ReadOnlyField()

    class Meta:
        model = EvaluateTest
        fields = ('id', 'target_controller', 'target', 'token', 'delivery_status',)


class EvaluateResultSerializer(serializers.ModelSerializer):
    target_profile = EvaluateTestSerializer(read_only=True, many=True)

    class Meta:
        model = EvaluateResult
        fields = ('id', 'target_profile', 'timestamp', 'result')
