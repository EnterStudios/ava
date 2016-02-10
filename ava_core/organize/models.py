# Django Imports
from django.conf import settings
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.urlresolvers import reverse
from django.core.validators import validate_email, validate_slug, validate_ipv46_address
from django.db import models
from django.utils.crypto import get_random_string
# Python Imports
import logging
import string
# Local Imports
from .validators import validate_skype, validate_twitter
from ava_core.abstract.models import TimeStampedModel
from ava_core.notify.models import NotificationEmail
from ava_core.utils import send_mail_smtp

# Loggers
log = logging.getLogger(__name__)


# Implementation
class Person(TimeStampedModel):
    first_name = models.CharField(max_length=75, validators=[validate_slug])
    surname = models.CharField(max_length=75, validators=[validate_slug], null=True, blank=True, )
    groups = models.ManyToManyField('Group', blank=True, related_name='members')
    google_identity_data = models.CharField(max_length=10000, null=True, blank=True, verbose_name='Google Data')
    ldap_identity_data = models.CharField(max_length=10000, null=True, blank=True, verbose_name='LDAP Data')
    office365_identity_data = models.CharField(max_length=10000, null=True, blank=True, verbose_name='Office365 Data')

    def __str__(self):
        return self.surname + ', ' + self.first_name or ''

    def get_absolute_url(self):
        return reverse('person-detail', kwargs={'pk': self.id})

    def get_formatting(self):
        return {
            'first_name': self.first_name,
            'surname': self.surname,
            'full_name': '{} {}'.format(self.first_name, self.surname)
        }

    def run_intro(self):
        log.debug('Function Called'
                  ' - organize::Person::run_intro')

        # Attempt to get the primary email that belongs to person
        # Returning from function if failed
        try:
            primary_identifier = PersonIdentifier.objects.get(belongs_to=self, primary_identifier=True,
                                                              identifier_type=PersonIdentifier.EMAIL)
        except PersonIdentifier.DoesNotExist:
            log.debug('Function Error:'
                      ' - organize::Person::run_intro'
                      ' - PersonIdentifier.DoesNotExist')
            return

        # Attempt to get the introduction email to send
        # Returning from function if failed
        try:
            intro_email = NotificationEmail.objects.get(notification_type=NotificationEmail.INTRO)
        except NotificationEmail.DoesNotExist:
            log.debug('Function Error:'
                      ' - organize::Person::run_intro'
                      ' - NotificationEmail.DoesNotExist')
            return

        # Get map for formatting template
        intro_formatting = self.get_formatting()

        # Send email to primary email address, checking mail has been sent correctly
        # True - Run the task for sending email invite
        return send_mail_smtp(primary_identifier.identifier,
                              intro_email.address_from,
                              string.Template(intro_email.subject).safe_substitute(intro_formatting),
                              string.Template(intro_email.body).safe_substitute(intro_formatting))

    def run_invite(self):
        log.debug('Function Called'
                  ' - organize::Person::run_invite')

        # Attempt to get the primary email that belongs to person
        # Returning from function if failed
        try:
            primary_identifier = PersonIdentifier.objects.get(belongs_to=self, primary_identifier=True,
                                                              identifier_type=PersonIdentifier.EMAIL)
        except PersonIdentifier.DoesNotExist:
            log.debug('Function Error:'
                      ' - organize::Person::run_invite'
                      ' - PersonalIdentifier.DoesNotExist')
            return

        # Create a new user from the primary email address
        user = User.objects.create_user(username=primary_identifier.identifier,
                                        email=primary_identifier.identifier,
                                        password=get_random_string())

        from ava_core.my.models import People
        my_people_object, created = People.objects.update_or_create(owner=user, person=self)

        # Attempt to get the introduction email to send
        # Returning from function if failed
        try:
            invite_email = NotificationEmail.objects.get(notification_type=NotificationEmail.INVITE)
        except NotificationEmail.DoesNotExist:
            log.debug('Function Error:'
                      ' - organize::Person::run_intro'
                      ' - NotificationEmail.DoesNotExist')
            return

        # Get map for formatting template
        invite_formatting = self.get_formatting()

        # Send email to primary email address, checking mail has been sent correctly
        # True - Run the task for sending email invite
        return send_mail_smtp(primary_identifier.identifier,
                              invite_email.address_from,
                              string.Template(invite_email.subject).safe_substitute(invite_formatting),
                              string.Template(invite_email.body).safe_substitute(invite_formatting))

    class Meta:
        verbose_name = 'person'
        verbose_name_plural = 'people'
        ordering = ['surname', 'first_name']


class PersonAttribute(TimeStampedModel):
    person = models.ForeignKey(to=Person)
    non_human = models.BooleanField(default=False)

    def __str__(self):
        return 'Person Attribute ({})'.format(self.id)


class Identifier(TimeStampedModel):
    EMAIL = 'EMAIL'
    SKYPE = 'SKYPE'
    IP = 'IPADD'
    UNAME = 'UNAME'
    TWITTER = 'TWITTER'
    NAME = 'NAME'
    GOOGLE_ID = 'GOOGLE_ID'
    OFFICE_ID = 'OFFICE_ID'
    GUID = 'GUID'
    SID = 'SID'

    IDENTIFIER_TYPE_CHOICES = (
        (EMAIL, 'Email Address'),
        (SKYPE, 'Skype ID'),
        (IP, 'IP Address'),
        (UNAME, 'Username'),
        (TWITTER, 'Twitter ID'),
        (NAME, 'Other name'),
        (GOOGLE_ID, 'Google ID'),
        (OFFICE_ID, 'Office ID'),
        (GUID, 'Guid'),
        (SID, 'Sid'),
    )

    identifier = models.CharField(max_length=500)
    identifier_type = models.CharField(max_length=10,
                                       choices=IDENTIFIER_TYPE_CHOICES,
                                       default=EMAIL,
                                       verbose_name='Identifier Type')

    primary_identifier = models.BooleanField(default=False)

    def __str__(self):
        return self.identifier or ''

    @staticmethod
    def get_display_identifier_type(self, look_up):
        return self.IDENTIFIER_TYPE_CHOICES[look_up]

    def clean(self):
        if self.identifier_type is 'EMAIL':
            try:
                validate_email(self.identifier)
            except ValidationError:
                raise ValidationError('Identifier is not a valid email address')

        if self.identifier_type is 'IPADD':
            try:
                validate_ipv46_address(self.identifier)
            except ValidationError:
                raise ValidationError('Identifier is not a valid IPv4/IPv6 address')

        if self.identifier_type is 'UNAME' or self.identifier_type is 'NAME':
            try:
                validate_slug(self.identifier)
            except ValidationError:
                raise ValidationError('Identifier is not a valid username or name')

        if self.identifier_type is 'SKYPE':
            try:
                validate_skype(self.identifier)
            except ValidationError:
                raise ValidationError('Identifier is not a valid Skype user name')

        if self.identifier_type is 'TWITTER':
            try:
                validate_twitter(self.identifier)
            except ValidationError:
                raise ValidationError('Identifier is not a valid Twitter user name')

    class Meta:
        ordering = ['identifier', 'identifier_type']
        abstract = True


class Group(TimeStampedModel):
    AD = 'ACTIVE DIRECTORY'
    SOCIAL = 'SOCIAL GROUP'
    PROJECT = 'PROJECT'
    WORKING = 'WORKING GROUP'
    TEAM = 'TEAM'
    GENERIC = 'GENERIC'
    ORG = 'ORGANISATION'
    DIST = 'DISTRIBUTION LIST'
    GOOGLE = 'GOOGLE APPS'

    GROUP_TYPE_CHOICES = (
        (AD, 'Active Directory'),
        (SOCIAL, 'Social Group'),
        (PROJECT, 'Project'),
        (WORKING, 'Working Group'),
        (TEAM, 'Team'),
        (GENERIC, 'Generic Group'),
        (ORG, 'Organisation'),
        (DIST, 'Distribution List'),
        (GOOGLE, 'Google Apps Group'),
    )

    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    group_type = models.CharField(max_length=20, choices=GROUP_TYPE_CHOICES, default=GENERIC, verbose_name='Group Type')
    parent = models.ForeignKey('Group', null=True, blank=True, related_name='parent_group')
    google_group_data = models.CharField(max_length=10000, null=True, blank=True)
    ldap_group_data = models.CharField(max_length=10000, null=True, blank=True)

    def __str__(self):
        return self.name or ''

    @staticmethod
    def get_display_group_type(self, look_up):
        return self.GROUP_TYPE_CHOICES[look_up]

    def get_absolute_url(self):
        return reverse('groups-detail', kwargs={'pk': self.pk})

    class Meta:
        ordering = ['name', 'group_type']


class PersonIdentifier(Identifier):
    belongs_to = models.ForeignKey('Person', related_name='person_ids')


class PersonIdentifierAttribute(TimeStampedModel):
    NONE = 0
    INTERNAL_SYSTEM_IDENTIFIER = 1
    PERSONAL_IDENTIFIER = 2

    TYPE_IGNORE = (
        (NONE, 'Don\'t Ignore'),
        (INTERNAL_SYSTEM_IDENTIFIER, 'Internal System Identifier'),
        (PERSONAL_IDENTIFIER, 'Personal Identifier'),
    )

    identifier = models.ForeignKey(to=PersonIdentifier)
    ignore_type = models.IntegerField(choices=TYPE_IGNORE, default=NONE)

    def __str__(self):
        return 'Person Identifier Attribute ({})'.format(self.id)

    @staticmethod
    def get_display_ignore_type(self, look_up):
        return self.TYPE_IGNORE[look_up]


class GroupIdentifier(Identifier):
    belongs_to = models.ForeignKey('Group', related_name='group_ids')


class GroupIdentifierAttribute(TimeStampedModel):
    NONE = 0
    INVALID_IDENTIFIER = 1

    TYPE_IGNORE = (
        (NONE, 'Don\'t Ignore'),
        (INVALID_IDENTIFIER, 'Invalid Identifier'),

    )

    identifier = models.ForeignKey(to=GroupIdentifier)
    ignore_type = models.IntegerField(choices=TYPE_IGNORE, default=NONE)

    def __str__(self):
        return 'Group Identifier Attribute ({})'.format(self.id)

    @staticmethod
    def get_display_ignore_type(self, look_up):
        return self.TYPE_IGNORE[look_up]


class PersonIdentifierReport(TimeStampedModel):
    PERSONAL = 0
    INCORRECT_INFORMATION = 1
    INCORRECT_OWNER = 2
    OUTDATED = 3

    TYPE_REASON = (
        (PERSONAL, 'Personal account'),
        (INCORRECT_INFORMATION, 'Incorrect information'),
        (INCORRECT_OWNER, 'Incorrect owner'),
        (OUTDATED, 'Outdated')
    )

    LOW = 0
    MEDIUM = 1
    HIGH = 2
    CRITICAL = 3

    TYPE_PRIORITY = (
        (LOW, 'Low'),
        (MEDIUM, 'Medium'),
        (HIGH, 'High'),
        (CRITICAL, 'Critical'),
    )

    owner = models.ForeignKey(to=settings.USER_MODEL, null=False)
    identifier = models.ForeignKey(to=PersonIdentifier)
    reason_type = models.IntegerField(choices=TYPE_REASON, default=PERSONAL)
    priority_type = models.IntegerField(choices=TYPE_PRIORITY, default=LOW)
    description = models.TextField(max_length=1000, blank=True, null=True)
    is_resolved = models.BooleanField(default=False)

    def delete(self, using=None, keep_parents=False):
        self.is_resolved = True
        self.save()

    @staticmethod
    def get_display_reason_type(self, lookup):
        return self.TYPE_REASON[lookup]

    @staticmethod
    def get_display_priority_type(self, lookup):
        return self.TYPE_PRIORITY[lookup]


class GroupReport(TimeStampedModel):
    REMOVE_FROM = 0

    TYPE_REASON = (
        (REMOVE_FROM, 'Remove me'),
    )

    LOW = 0
    MEDIUM = 1
    HIGH = 2
    CRITICAL = 3

    TYPE_PRIORITY = (
        (LOW, 'Low'),
        (MEDIUM, 'Medium'),
        (HIGH, 'High'),
        (CRITICAL, 'Critical'),
    )

    owner = models.ForeignKey(to=settings.USER_MODEL, null=False)
    group = models.ForeignKey(to=Group)
    reason_type = models.IntegerField(choices=TYPE_REASON, default=REMOVE_FROM)
    priority_type = models.IntegerField(choices=TYPE_PRIORITY, default=LOW)
    description = models.TextField(max_length=1000, blank=True, null=True)
    is_resolved = models.BooleanField(default=False)

    def delete(self, using=None, keep_parents=False):
        self.is_resolved = True
        self.save()
