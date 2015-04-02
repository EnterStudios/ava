from django.db import models
from django.core.validators import validate_email, validate_slug, validate_ipv46_address
from django.core.exceptions import ValidationError
from django.core.urlresolvers import reverse
from apps.ava_core.models import ReferenceModel, TimeStampedModel
from apps.ava_core_group.models import Group
from apps.ava_core_identity.validators import validate_skype, validate_twitter


class Identity(ReferenceModel):
    '''
    An identity is an online persona that can map to a single person, a group
    of people, or an automated service.
    '''
    
    groups = models.ManyToManyField(Group,
                                    null=True,
                                    blank=True,
                                    related_name='identities')

    def get_absolute_url(self):
        return reverse('identity-detail', kwargs={'pk': self.id})

    class Meta:
        verbose_name = 'identity'
        verbose_name_plural = 'identities'
        ordering = ['name']


class Person(TimeStampedModel):
    '''
    TODO: DocString
    '''
    
    firstname = models.CharField(max_length=75, validators=[validate_slug])
    surname = models.CharField(max_length=75, validators=[validate_slug])
    identity = models.ManyToManyField('Identity', blank=True)

    def __unicode__(self):
        return (self.firstname + " " + self.surname).strip() or u''

    def get_absolute_url(self):
        return reverse('person-detail', kwargs={'pk': self.id})
    
    class Meta:
        verbose_name = 'person'
        verbose_name_plural = 'people'
        ordering = ['surname', 'firstname']


class Identifier(TimeStampedModel):
    '''
    TODO: DocString
    '''

    EMAIL = 'EMAIL'
    SKYPE = 'SKYPE'
    IP = 'IPADD'
    UNAME = 'UNAME'
    TWITTER = 'TWITTER'

    IDENTIFIER_TYPE_CHOICES = (
        (EMAIL,   'Email Address'),
        (SKYPE,   'Skype ID'),
        (IP,      'IP Address'),
        (UNAME,   'Username'),
        (TWITTER, 'Twitter ID'),
    )
    
    identifier = models.CharField(max_length=100)
    identifiertype = models.CharField(max_length=10,
                                      choices=IDENTIFIER_TYPE_CHOICES,
                                      default=EMAIL,
                                      verbose_name='Identifier Type')
    identity = models.ForeignKey('Identity', related_name='identifiers')

    def __unicode__(self):
        return self.identifier or u''

    def get_absolute_url(self):
        return reverse('identifier-detail', kwargs={'pk': self.id})
    
    def clean(self):
        if self.identifiertype == 'EMAIL':
            try:
                validate_email(self.identifier)
            except ValidationError:
                raise ValidationError('Identifier is not a valid email address')
        
        if self.identifiertype == 'IPADD':
            try:
                validate_ipv46_address(self.identifier)
            except ValidationError:
                raise ValidationError('Identifier is not a valid IPv4/IPv6 address')

        if self.identifiertype == 'UNAME':
            try:
                validate_slug(self.identifier)
            except ValidationError:
                raise ValidationError('Identifier is not a valid username')

        if self.identifiertype =='SKYPE':
            try:
                validate_skype(self.identifier)
            except ValidationError:
                raise ValidationError('Identifier is not a valid Skype user name')

        if self.identifiertype == 'TWITTER':
            try:
                validate_twitter(self.identifier)
            except ValidationError:
                raise ValidationError('Identifier is not a valid Twitter user name')

    class Meta:
        unique_together = ("identifier", "identifiertype", "identity")
        ordering = ['identifier', 'identifiertype']
