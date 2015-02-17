from django.db import models
from django.core.validators import validate_email,validate_slug,validate_ipv46_address
from django.core.exceptions import ValidationError
from django.core.urlresolvers import reverse

from django.contrib.auth.models import User

from apps.ava_core.models import TimeStampedModel
import apps.ava_core_org.models


# CORE TABLES: TARGETS


class Person(TimeStampedModel):
    firstname = models.CharField(max_length=75,validators=[validate_slug])
    surname = models.CharField(max_length=75,validators=[validate_slug])
    user = models.ForeignKey(User)
    organisation = models.ForeignKey('ava_core_org.Organisation')

    def __unicode__(self):
        return self.firstname+" "+self.surname or u''

    def get_absolute_url(self):
	    return reverse('person-detail',kwargs={'pk': self.pk})
    
    class Meta:
        verbose_name = ('person')
        verbose_name_plural = ('people')

class Identifier(TimeStampedModel):

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
    person = models.ForeignKey('Person', null=True)

    class Meta:
        unique_together = ("identifier", "identifiertype","person")


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
        


