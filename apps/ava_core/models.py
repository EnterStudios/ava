from django.db import models

# ABSTRACT MODELS
class TimeStampedModel (models.Model):
    """An abstract base class model that provides creation and modification date 
    information to all models in AVA
    """

    created=models.DateTimeField(auto_now_add=True)
    modified=models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class ReferenceModel (TimeStampedModel):
    """An abstract base class model for reference tables 
    """
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name or u''

    class Meta:
        abstract = True

class ConfigurationModel (TimeStampedModel):
    """An abstract base class model for configuration tables 
    """
    name=models.CharField(max_length=255, unique=True)
    value=models.CharField(max_length=255)
    help_text = models.CharField(max_length=200)
   
    def __unicode__(self):
        return self.name or u''

    class Meta:
        abstract = True

# REFERENCE TABLES 

class UserStatus(ReferenceModel):
    # see Reference model for field descriptions
    pass

class Role(ReferenceModel):
    # see Reference model for field descriptions
    pass

class Mode(ReferenceModel):
    # see Reference model for field descriptions
    pass

class TestStatus(ReferenceModel):
    # see Reference model for field descriptions
    pass

    class Meta:
        verbose_name_plural = ('teststatus')

class Group(ReferenceModel):
    # see Reference model for field descriptions
    pass

class GeneralStatus(ReferenceModel):
    # see Reference model for field descriptions
    pass
    
    class Meta:
        verbose_name_plural = ('generalstatus')

# CORE TABLES: SYSTEM 

class Module(ReferenceModel):
    MODULE_STATUS_CHOICES = (
                    ('Y', 'Enabled'),
                    ('N', 'Disabled'),
    )
    enabled=models.CharField(max_length=1,
            choices=MODULE_STATUS_CHOICES,default='N')
  

class SystemConfig(ConfigurationModel):
    # see Configuration model for field descriptions
    pass

class UserPreference(ConfigurationModel):
    # see Configuration model for field descriptions
    #user = model.ForeignKey('django.contrib.auth.models.User', null=False)
    pass
    #class Meta:
    #    unique_together = ('user','name')


