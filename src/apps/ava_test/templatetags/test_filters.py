from django import template
from apps.ava_test.models import Test

# This line is needed in order to register the filters in the file.
# Each filter function should be decorated with one of:
# @register.filter
# @register.filter(name='alternate_name_of_filter')
register = template.Library()


class Constants(object):
    '''
    Constants that are used by the filter functions in this file.
    '''
    TEST_TYPE_NAMES = dict(Test.TEST_TYPE_CHOICES)
    TEST_STATUS_NAMES = dict(Test.TEST_STATUS_CHOICES)

@register.filter
def test_type(value):
    return Constants.TEST_TYPE_NAMES[value]

@register.filter
def test_status(value):
    return Constants.TEST_STATUS_NAMES[value]
