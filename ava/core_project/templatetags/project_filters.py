from django import template
from ava.core_project.models import ProjectTeam

# This line is needed in order to register the filters in the file.
# Each filter function should be decorated with one of:
# @register.filter
# @register.filter(name='alternate_name_of_filter')
register = template.Library()


class Constants(object):

    '''
    Constants that are used by the filter functions in this file.
    '''
    ACCESS_LEVELS = dict(ProjectTeam.ACCESS_LEVEL_CHOICES)


@register.filter
def access_level(value):
    '''
    Converts the code name of a group type to a friendly name.
    :param group_type_code:
    '''
    return Constants.ACCESS_LEVELS[value]
