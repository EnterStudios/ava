import logging

from ava_core.abstract.models import ReferenceModel
from django.db import models

log = logging.getLogger(__name__)


class Module(ReferenceModel):
    module_url = models.URLField()
    path = models.ManyToManyField(to='Path', related_name='path_modules')
    parent = models.ForeignKey(to='Module', related_name='parent_module', null=True, blank=True)

    def __str__(self):
        return self.name


class Path(ReferenceModel):
    def __str__(self):
        return self.name


class Role(ReferenceModel):
    path = models.ManyToManyField(to='Path', related_name='path_roles')

    def __str__(self):
        return self.name
