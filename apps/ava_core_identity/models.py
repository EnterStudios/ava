from django.db import models
from django.core.validators import validate_email,validate_slug,validate_ipv46_address
from django.core.exceptions import ValidationError
from django.core.urlresolvers import reverse

from apps.ava_core.models import ReferenceModel, TimeStampedModel



class Identity(ReferenceModel):
    '''
    TODO: DocString
    '''
    def get_absolute_url(self):
        return reverse('identity-detail',kwargs={'pk': self.pk})

    class Meta:
        verbose_name = ('identity')
        verbose_name_plural = ('identities')


class Person(TimeStampedModel):
    '''
    TODO: DocString
    '''
    firstname = models.CharField(max_length=75,validators=[validate_slug])
    surname = models.CharField(max_length=75,validators=[validate_slug])
    identity = models.ManyToManyField('Identity')

    def __unicode__(self):
        return self.firstname+" "+self.surname or u''

    def get_absolute_url(self):
        return reverse('person-detail',kwargs={'pk': self.pk})
    
    class Meta:
        verbose_name = ('person')
        verbose_name_plural = ('people')


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
        (EMAIL,  'Email Address'),
        (SKYPE,  'Skype ID'),
        (IP,  'IP Address'),
        (UNAME, 'Username'),
        (TWITTER , 'Twitter ID'),
    )

    identifier = models.CharField(max_length=100)
    identifiertype = models.CharField(max_length=7,
                            choices=IDENTIFIER_TYPE_CHOICES, default=EMAIL,
                                verbose_name='Identifier Type')
    identity = models.ForeignKey('Identity')

    class Meta:
        unique_together = ("identifier", "identifiertype", "identity")


    def __unicode__(self):
        return self.identifier or u''

    def get_absolute_url(self):
	    return reverse('identifier-detail',kwargs={'pk': self.pk})
    
    def clean(self):
        if self.identifiertype == 'EMAIL':
            try:
                validate_email(self.identifier)
            except ValidationError as e:
                raise ValidationError('Identifier declared as EMAIL but does not contain a valid email address')
        
        if self.identifiertype == 'IPADD':
            try:
                validate_ipv46_address(self.identifier)
            except ValidationError as e:
                raise ValidationError('Identifier declared as IP ADDRESS but does not contain a valid ip4/ip6 address')

        if self.identifiertype == 'UNAME' or self.identifiertype =='SKYPE':
            try:
                validate_slug(self.identifier)
            except ValidationError as e:
                raise ValidationError('Identifier declared as USERNAME/SKYPE but does not contain a username or skype identifier')

        if self.identifiertype == 'TWITTER':
            try:
                validate_slug(self.identifier)
            except ValidationError as e:
                raise ValidationError('Identifier declared as Twitter ID but does not contain a valid twitter id')
        


