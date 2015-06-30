from django import template
from ava.core_group.models import Group

# This line is needed in order to register the filters in the file.
# Each filter function should be decorated with one of:
# @register.filter
# @register.filter(name='alternate_name_of_filter')
register = template.Library()


class Constants(object):
    """
    Constants that are used by the filter functions in this file.
    """
    GROUP_TYPES = dict(Group.GROUP_TYPE_CHOICES)


@register.filter
def group_type(value):
    """
    Converts the code name of a group type to a friendly name.
    :param group_type_code:
    """
    return Constants.GROUP_TYPES[value]
