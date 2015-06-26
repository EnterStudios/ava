from django.db import models


# ABSTRACT MODELS
class TimeStampedModel(models.Model):
    """An abstract base class model that provides creation and modification date 
    information to all models in AVA
    """

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class ReferenceModel(TimeStampedModel):
    """An abstract base class model for reference tables 
    """
    name = models.CharField(max_length=100, verbose_name='Name')
    description = models.TextField(max_length=500, verbose_name='Description')

    def __unicode__(self):
        return self.name or u''

    class Meta:
        abstract = True
