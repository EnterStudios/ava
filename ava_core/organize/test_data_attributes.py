from .models import Person, Group


class PersonTestDataAttributes:
    query_set = Person.objects.all()

    url = '/organize/person/'
    url_does_not_exist = '/organize/person/9999/'
    url_format = '/organize/person/{}'

    model_name = 'organize.Person'


class GroupTestDataAttributes:
    query_set = Group.objects.all()

    url = '/organize/group/'
    url_does_not_exist = '/organize/group/9999/'
    url_format = '/organize/group/{}'

    model_name = 'organize.Group'
