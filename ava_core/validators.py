# Django Imports
from django.core.validators import ValidationError
# Python Imports
from logging import getLogger

# Loggers
logger = getLogger(__name__)


# Implementation
class NotBlankWhenTypeValidator(object):
    def __init__(self, validate_field, type_field, desired_type):
        self.validate_field = validate_field
        self.type_field = type_field
        self.desired_type = desired_type
        self.message = '\'{}\' field may not be blank.'

    def __call__(self, value):
        if value[self.type_field] is self.desired_type:
            if value[self.validate_field] is '':
                raise ValidationError(self.message.format(self.validate_field))