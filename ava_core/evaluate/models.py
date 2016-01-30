# Django Imports
from django.core.exceptions import ValidationError
from django.conf import settings
from django.db import models
from django.utils.crypto import get_random_string
# Python Imports
from logging import getLogger
from string import Template
# Local Imports
from ava_core.abstract.models import ReferenceModel, TimeStampedModel
from ava_core.organize.models import Person, PersonIdentifier
from ava_core.utils import send_mail_smtp

# Loggers
logger = getLogger(__name__)

"""
Evaluation Sender
"""


class EvaluateSender(TimeStampedModel):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    email_address = models.EmailField()
    slack_name = models.CharField(max_length=100)  # Set to 100 characters due to max size for slack username
    hidden = models.BooleanField(default=False)

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)

    def delete(self, using=None, keep_parents=False):
        self.hidden = True
        self.save()


"""
Evaluation Templates
"""


class EvaluateTemplate(ReferenceModel):
    EMAIL = 0
    SLACK = 1

    TYPE_TEMPLATE = (
        (EMAIL, 'Email'),
        (SLACK, 'Slack'),
    )

    template_type = models.IntegerField(choices=TYPE_TEMPLATE,
                                        default=EMAIL)

    email_subject = models.CharField(max_length=128, blank=True, null=True)
    email_body = models.TextField(max_length=1024, blank=True, null=True)
    hidden = models.BooleanField(default=False)

    @staticmethod
    def get_display_template_type(self, look_up):
        return self.TYPE_TEMPLATE[look_up]

    def run_evaluate(self, target_profile):
        logger.debug('Function Called'
                     ' - evaluate::EvaluateTemplate::run_evaluate')
        if self.template_type is self.EMAIL:
            return self.internal_run_evaluate_email(target_profile)
        elif self.template_type is self.SLACK:
            return self.internal_run_evaluate_slack(target_profile)
        else:
            logger.debug('Information'
                         ' - evaluate::EvaluateTemplate::run_evaluate'
                         ' - Unrecognized template type, check type is able to be processed')

    def internal_run_evaluate_email(self, target_profile):
        logger.debug('Function Called'
                     ' - evaluate::EvaluateTemplate::internal_run_evaluate_email')

        target = target_profile.target
        sender = target_profile.controller.sender
        formatting_information = {
            'target_first_name': target.first_name,
            'target_last_name': target.surname,
            'target_full_name': '{} {}'.format(target.first_name,
                                               target.surname),
            'target_token': target_profile.token,
            'sender_first_name': sender.first_name,
            'sender_last_name': sender.last_name,
            'sender_full_name': '{} {}'.format(sender.first_name,
                                               sender.last_name),
        }

        # Attempt to get the primary email that belongs to target
        # Returning from function if failed
        try:
            primary_identifier = PersonIdentifier.objects.get(belongs_to=target, primary_identifier=True,
                                                              identifier_type=PersonIdentifier.EMAIL)
        except PersonIdentifier.DoesNotExist:
            logger.debug('Function Error:'
                         ' - evaluate::EvaluateTemplate::internal_run_evaluate_email'
                         ' - NotificationEmail.DoesNotExist')
            return False

        return send_mail_smtp(primary_identifier.identifier,
                              '{} {} <{}>'.format(sender.first_name, sender.last_name, sender.email_address),
                              Template(self.email_subject).safe_substitute(formatting_information),
                              Template(self.email_body).safe_substitute(formatting_information))

    def internal_run_evaluate_slack(self, target_profile):
        logger.debug('Function Called'
                     ' - evaluate::EvaluateTemplate::internal_run_evaluate_slack')

    def delete(self, using=None, keep_parents=False):
        self.hidden = True
        self.save()


"""
Evaluation Controller
"""


class EvaluateController(ReferenceModel):
    NOW = 0
    SCHEDULED = 1

    TYPE_SCHEDULE = (
        (NOW, 'Now'),
        (SCHEDULED, 'Scheduled'),
    )

    DAY = 0
    WEEK = 1
    MONTH = 2

    TYPE_EXPIRY = (
        (DAY, 'Day'),
        (WEEK, 'Week'),
        (MONTH, 'Month'),
    )

    DRAFT = 0
    PENDING = 1
    PROCESSED = 2
    ACTIVE = 3
    EXPIRED = 4

    TYPE_STATUS = (
        (DRAFT, 'Draft'),
        (PENDING, 'Pending'),
        (PROCESSED, 'Processed'),
        (ACTIVE, 'Active'),
        (EXPIRED, 'Expired')
    )

    scheduled_type = models.IntegerField(choices=TYPE_SCHEDULE, default=NOW)
    scheduled_time = models.DateTimeField(null=True, blank=True)
    expiry_type = models.IntegerField(choices=TYPE_EXPIRY, default=WEEK)

    # TODO  pretty sure this is now redundant
    expiry_time = models.DateTimeField(null=True, blank=True)
    sender = models.ForeignKey(to=EvaluateSender,limit_choices_to={'hidden': False})
    template = models.ForeignKey(to=EvaluateTemplate, limit_choices_to={'hidden': False})

    targets = models.ManyToManyField(to=Person)

    status = models.IntegerField(choices=TYPE_STATUS, default=DRAFT)

    def __str__(self):
        return self.name or u''

    @staticmethod
    def get_display_scheduled_type(self, look_up):
        return self.TYPE_SCHEDULE[look_up]

    @staticmethod
    def get_display_expiry_type(self, look_up):
        return self.TYPE_EXPIRY[look_up]

    @staticmethod
    def get_display_status_type(self, look_up):
        return self.TYPE_STATUS[look_up]

    def validate_unique(self, exclude=None):
        super(EvaluateController, self).validate_unique()

        if self.status is not self.DRAFT:
            raise ValidationError('Evaluate Controller cannot be updated once scheduled')

    def run_evaluate(self):
        logger.debug('Function Called'
                     ' - evaluate::EvaluateController::run_evaluate')
        for target in self.targets.all():
            EvaluateTest.objects.create(controller=self,
                                        target=target,
                                        token=EvaluateTest.generate_unique_token())

        self.status = self.ACTIVE
        self.save()

    def expire_evaluate(self):
        logger.debug('Function Called'
                     ' - evaluate::EvaluateController::expire_evaluate')
        for target in EvaluateTest.objects.filter(controller=self):
            if not EvaluateResult.objects.filter(target_profile=target).exists():
                EvaluateResult.objects.create(target_profile=target, result=EvaluateResult.PASS)

        self.status = self.EXPIRED
        self.save()


"""
Evaluation Target Profile
"""


class EvaluateTest(TimeStampedModel):
    PENDING = 0
    CANCELLED = 1
    SENT = 2
    ERROR = 3

    TYPE_DELIVERY_STATUS = (
        (PENDING, 'Pending'),
        (SENT, 'Sent'),
        (ERROR, 'Error'),
    )

    controller = models.ForeignKey(to=EvaluateController, related_name='target_controller')
    target = models.ForeignKey(to=Person)
    token = models.CharField(max_length=settings.EVAL_TOKEN_LENGTH)
    delivery_status = models.IntegerField(choices=TYPE_DELIVERY_STATUS, default=PENDING)

    def __str__(self):
        return u'Evaluate Target Profile ({})'.format(self.id)


    @staticmethod
    def get_display_delivery_status_type(self, look_up):
        return self.TYPE_DELIVERY_STATUS[look_up]

    @staticmethod
    def generate_unique_token():
        logger.debug('Function called'
                     ' - evaluate::EvaluateTargetProfile::generate_unique_token')
        return_string = get_random_string(settings.EVAL_TOKEN_LENGTH)

        while EvaluateTest.objects.filter(token__exact=return_string).exists():
            return_string - get_random_string(settings.EVAL_TOKEN_LENGTH)

        return return_string

    def run_evaluate(self):
        logger.debug('Function called'
                     ' - evaluate::EvaluateTargetProfile::run_evaluate')
        if self.controller.template.run_evaluate(self):
            self.delivery_status = self.SENT
        else:
            self.delivery_status = self.ERROR

        self.save()


"""
Evaluation Results
"""


class EvaluateResult(TimeStampedModel):
    FAIL = 0
    PASS = 1

    TYPE_RESULT = (
        (FAIL, 'Fail'),
        (PASS, 'Pass'),
    )

    target_profile = models.ForeignKey(to=EvaluateTest)
    result = models.IntegerField(choices=TYPE_RESULT, default=FAIL)

    def __str__(self):
        return u'Evaluate Results ({})'.format(self.id)

    @staticmethod
    def get_display_result_type(self, look_up):
        return self.TYPE_RESULT[look_up]
