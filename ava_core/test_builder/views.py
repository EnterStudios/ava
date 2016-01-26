# Python Imports
from logging import getLogger
import json
import os
# Django Imports
from django.apps import *
from django.conf import settings
from django.http import HttpResponse
# Rest Imports
from rest_framework.views import APIView
from rest_framework import status

# Logger
log = getLogger(__name__)

"""
Helper functions
"""


def plain_to_bumpy(plain):
    bumpy = ''

    if len(plain) is not 0:
        to_upper = True
        for character in plain:
            if to_upper:
                bumpy += character.upper()
                to_upper = False
            elif character is ' ':
                to_upper = True
            else:
                bumpy += character

    return bumpy


def bumpy_to_plain(bumpy):
    plain = ''

    if len(bumpy) is not 0:
        plain += bumpy[0].lower()
        for character in bumpy[1:]:
            if character.isupper():
                plain += ' '
            plain += character.lower()

    return plain


def plain_to_snake(plain):
    snake = ''

    for character in plain:
        if character is ' ':
            snake += '_'
        else:
            snake += character

    return snake


def snake_to_plain(snake):
    plain = ''

    for character in snake:
        if character is '_':
            plain += ' '
        else:
            plain += character

    return plain


def bumpy_to_snake(bumpy):
    return plain_to_snake(bumpy_to_plain(bumpy))


def snake_to_bumpy(snake):
    return plain_to_bumpy(snake_to_plain(snake))


"""
Creates the data for a project
"""


class ProjectDataBuilder(APIView):
    def get(self, request):
        # Load settings from Django.
        prefix = settings.TEST_BUILDER_PREFIX
        ignore_apps = settings.TEST_BUILDER_IGNORED_APPS
        ignore_models = settings.TEST_BUILDER_IGNORED_MODELS

        # Iterate over app configs, storing related data.
        project_data = dict()
        for app in apps.get_app_configs():
            # Check that app isn't to be ignored and is a part of the project directory.
            # True - Iterate over apps models, gathering relevant data.
            if app.name not in ignore_apps and app.name.startswith(prefix):
                # Iterate over models in app, storing relevant information.
                app_data = dict()
                for model in app.get_models():
                    # Check the model belongs to the app to avoid inheritance and abstraction,
                    # and check that it is not an ignored model.
                    # True - Format the data for model, adding it to app data.
                    if app.name in str(model) and str(model) not in ignore_models:
                        # Strip the model name from string
                        model_name = str(model).split('\'')[1].split('.')[-1]
                        app_data[model_name] = self.generate_model_data(model)

                # Add apps model data to dict.
                project_data[app.name] = app_data

        # Attempt to create directory for files.
        # Passing if already created.
        directory_name = '{}project_data/'.format(settings.TEST_BUILDER_DIRECTORY)
        try:
            os.makedirs(directory_name)
        except FileExistsError:
            pass

        # Format output file name and output json dump of project data.
        file_name = '{}{}.json'.format(directory_name, settings.TEST_BUILDER_PROJECT_DATA_OUTPUT)
        with open(file_name, 'w') as outfile:
            print(json.dumps(obj=project_data,
                             sort_keys=True,
                             indent=4,
                             separators=(',', ': ')),
                  file=outfile)
        outfile.close()

        return HttpResponse('Success', status=status.HTTP_200_OK)

    def generate_model_data(self, model):
        # Load settings from Django.
        ignore_fields = settings.TEST_BUILDER_IGNORED_FIELDS

        # Iterate over all fields on the model, gathering relevant data.
        field_data = dict()
        for field in model._meta.get_fields(include_parents=False, include_hidden=False):
            # Check that field is not in ignored fields settings.
            # True - Store field data for return.
            if field.name not in ignore_fields:
                fields_data = self.generate_field_data(field)
                if fields_data:
                    field_data[field.name] = fields_data

        # Populate the model data with default values to be processed by user.
        model_data = dict()
        model_data['fields'] = field_data
        model_data['url'] = '/example'
        model_data['permissions'] = {
            'admin': ['PUSH', 'GET', 'PUT', 'DELETE'],
            'user': ['PUSH', 'GET', 'PUT', 'DELETE']
        }
        model_data['requires_owner'] = True
        model_data['requires_authentication'] = True
        model_data['unique_together'] = []

        return model_data

    def generate_field_data(self, field):
        # Attempt to get the internal type of the field.
        # Returning None on failure.
        try:
            field_type = field.get_internal_type()
        except AttributeError:
            return None

        # Gather relevant data for field.
        field_data = dict()
        field_data['type'] = field_type
        if field_data['type'] == 'ForeignKey':
            _break = 4
        self.generate_field_attribute(field, field_data, 'max_length')
        self.generate_field_attribute(field, field_data, 'unique')
        self.generate_field_attribute(field, field_data, 'null')
        self.generate_field_attribute(field, field_data, 'blank')
        # field_data = self.generate_field_attribute(field, field_data, 'default')

        self.generate_field_attribute(field, field_data, 'related_model')
        if 'related_model' in field_data:
            field_data['related_model'] = str(field_data['related_model']).split('\'')[1]

        self.generate_field_attribute(field, field_data, 'choices')
        if 'choices' in field_data:
            choices = field_data['choices']
            if len(choices) is not 0:
                choice_list = []
                for choice in choices:
                    choice_list.append(choice[0])
                field_data['choices'] = choice_list
            else:
                field_data.pop('choices', None)

        return field_data

    @staticmethod
    def generate_field_attribute(field, field_dict, attribute_name):
        # Check that the attribute name belongs to the field.
        # True - Update the field dictionary with the attributes value.
        attr = getattr(field, attribute_name, None)
        if attr is not None:
            field_dict[attribute_name] = attr


"""
Creates the tests for a project
"""


class ProjectTestBuilder(APIView):
    def get(self, request):
        # Attempt to open JSON input file with project information.
        # Return bad request response on failure.
        try:
            file_name = '{}project_data/{}.json'.format(settings.TEST_BUILDER_DIRECTORY,
                                                        settings.TEST_BUILDER_PROJECT_DATA_INPUT)
            with open(file_name) as data_file:
                project_data = json.load(data_file)
            data_file.close()
        except:
            return HttpResponse('No input file.', status=status.HTTP_400_BAD_REQUEST)

        # Attempt to create directory for files.
        # Passing if already created.
        try:
            os.makedirs(settings.TEST_BUILDER_ABSTRACT_DIRECTORY)
        except FileExistsError:
            pass

        # Take copy of template classes
        file_name = '{}project_data/test_template.py'.format(settings.TEST_BUILDER_DIRECTORY)
        with open(file_name) as data_file:
            directory_name = '{}/test.py'.format(settings.TEST_BUILDER_ABSTRACT_DIRECTORY)
            with open(directory_name, 'w') as outfile:
                print(data_file.read().format(project_name_snake=settings.TEST_BUILDER_PREFIX,
                                              project_name_bumpy=snake_to_bumpy(settings.TEST_BUILDER_PREFIX)),
                      file=outfile)
            outfile.close()
        data_file.close()

        file_name = '{}project_data/test_data_template.py'.format(settings.TEST_BUILDER_DIRECTORY)
        with open(file_name) as data_file:
            directory_name = '{}/test_data.py'.format(settings.TEST_BUILDER_ABSTRACT_DIRECTORY)
            with open(directory_name, 'w') as outfile:
                print(data_file.read().format(project_name=snake_to_bumpy(settings.TEST_BUILDER_PREFIX)),
                      file=outfile)
            outfile.close()
        data_file.close()

        # Iterate over apps in project data, creating all necessary files.
        for app in project_data:
            # Create the test and data files for app.
            test_output = self.generate_app_test(app_name=app,
                                                 app_data=project_data[app])
            data_output = self.generate_app_data(app_name=app,
                                                 app_data=project_data[app])

            # Attempt to create directory for files.
            # Passing if already created.
            directory_name = '{}{}/'.format(settings.TEST_BUILDER_DIRECTORY, app)
            try:
                os.makedirs(directory_name)
            except FileExistsError:
                pass

            # Format output file name and output json dump of project data.
            test_file = '{}tests.py'.format(directory_name, settings.TEST_BUILDER_PROJECT_DATA_OUTPUT)
            with open(test_file, 'w') as outfile:
                print(test_output,
                      file=outfile)
            outfile.close()

            test_file = '{}test_data.py'.format(directory_name, settings.TEST_BUILDER_PROJECT_DATA_OUTPUT)
            with open(test_file, 'w') as outfile:
                print(data_output,
                      file=outfile)
            outfile.close()

        return HttpResponse('Success.', status=status.HTTP_200_OK)

    """
    Output formatting for tests
    """

    def generate_app_test(self, app_name, app_data):
        # Create empty string for app file.
        app_string = str()

        app_string += self.generate_header_test(app_name=app_name,
                                                app_data=app_data) + '\n\n'

        app_string += '# Implementation\n'
        for model in app_data:
            app_string += self.generate_model_test(model_name=model,
                                                   model_data=app_data[model]) + '\n\n'

        # Replace tabs with spaces
        out_string = str()
        for character in app_string:
            if character is '\t':
                out_string += '    '
            else:
                out_string += character

        return out_string

    def generate_header_test(self, app_name, app_data):
        out_string = str()

        # Format the dependency imports header for app file.
        out_string += '# Rest Imports\n'
        out_string += 'from rest_framework import status\n'

        # Format the local imports header for app file.
        out_string += '# Local Imports\n'
        out_string += 'from {}.abstract.tests import {}Test\n'.format(settings.TEST_BUILDER_PREFIX,
                                                                      snake_to_bumpy(
                                                                              settings.TEST_BUILDER_PREFIX))

        # Make initial formatting for model imports
        model_import = 'from {}.models import'.format(app_name)
        data_import = 'from {}.test_data import'.format(app_name)

        # Iterate over apps models, creating necessary imports.
        first_iteration = True
        for model in app_data:
            model_import += (' ' if first_iteration else ', ') + model
            data_import += (' ' if first_iteration else ', ') + model + 'TestData'
            first_iteration = False

        out_string += model_import + '\n'
        out_string += data_import + '\n'

        return out_string

    def generate_model_test(self, model_name, model_data):
        out_string = str()

        # Create test model header
        out_string += 'class {}Test({}Test):\n'.format(plain_to_bumpy(model_name),
                                                       snake_to_bumpy(settings.TEST_BUILDER_PREFIX))
        out_string += '\t\"\"\"\n'
        out_string += '{} Test'.format(plain_to_bumpy(model_name))
        out_string += '\t\"\"\"\n'
        out_string += '\n'

        # Create setup for tests
        out_string += '\tdef setUp(self):\n'
        out_string += '\t\t# Make call to super.'
        out_string += '\t\tsuper({}Test, self).setUp()\n'.format(plain_to_bumpy(model_name))
        out_string += '\n'
        out_string += '\t\t# Set the data type.\n'
        out_string += '\t\tself.data = {}TestData\n'.format(plain_to_bumpy(model_name))
        out_string += '\n'

        # Create each of the CRUD test functions
        out_string += self.generate_create_tests(model_name, model_data)
        out_string += self.generate_retrieve_tests(model_name, model_data)
        out_string += self.generate_update_tests(model_name, model_data)
        out_string += self.generate_delete_tests(model_name, model_data)

        return out_string

    def generate_create_tests(self, model_name, model_data):
        out_string = str()

        out_string += self.generate_create_as_tests(model_name, model_data, 'user')
        out_string += self.generate_create_as_tests(model_name, model_data, 'admin')
        out_string += self.generate_create_as_tests(model_name, model_data)

        return out_string

    def generate_create_as_tests(self, model_name, model_data, user=None):
        out_string = str()

        # Create function header
        out_string += '\tdef test_{}_create_as_{}(self):\n'.format(bumpy_to_snake(model_name),
                                                                   user if user is not None else 'unauthenticated')

        # Create required login
        if user is not None:
            out_string += '\t\t# Log in as {}.\n'.format(user)
            out_string += '\t\tself.login_user(self.user_{})\n'.format(user)
            out_string += '\n'

        # Create count storage
        out_string += '\t\t# Take count.\n'
        out_string += '\t\tcount = self.data.model.objects.count()\n'
        out_string += '\n'

        # Determine if push was successful
        create_successful = False
        if user in model_data['permissions'] and 'PUSH' in model_data['permissions'][user]:
            create_successful = True
        elif user is None and not model_data['requires_authentication']:
            create_successful = True

        # Create data storage
        out_string += '\t\t# Store data to use.\n'
        out_string += '\t\tdata = self.data.get_data()\n'
        out_string += '\n'

        # Create push request
        out_string += '\t\t# Make push request and ensure {} response.\n'.format(
                'created' if create_successful else 'unauthorized')
        out_string += '\t\tresponse = self.client.push(self.format_url(self.data.url), data, format=\'json\')\n'

        if create_successful:
            out_string += '\t\tself.assertEqual(response.status_code, status.HTTP_201_CREATED)\n'
            out_string += '\t\tself.assertEqual(self.data.model.objects.count(), count + 1)\n'
            out_string += '\t\tself.assertTrue(self.does_contain_data(response.data, data))\n'
            out_string += '\n'
        else:
            out_string += '\t\tself.assertIn(response.status_code, self.status_forbidden)\n'
            out_string += '\t\tself.assertEqual(self.data.model.objects.count(), count)\n'
            out_string += '\n'

        return out_string

    def generate_retrieve_tests(self, model_name, model_data):
        out_string = str()

        out_string += self.generate_retrieve_as_tests(model_name, model_data, False, 'user')
        out_string += self.generate_retrieve_as_tests(model_name, model_data, True, 'user')
        out_string += self.generate_retrieve_as_tests(model_name, model_data, False, 'admin')
        out_string += self.generate_retrieve_as_tests(model_name, model_data, True, 'admin')
        out_string += self.generate_retrieve_as_tests(model_name, model_data, False)
        out_string += self.generate_retrieve_as_tests(model_name, model_data, True)

        return out_string

    def generate_retrieve_as_tests(self, model_name, model_data, all=False, user=None):
        out_string = str()

        out_string += '\tdef test_{}_retrieve_{}_as_{}(self):\n'.format(bumpy_to_snake(model_name),
                                                                        'all' if all else 'single',
                                                                        user if user is not None else 'unauthorized')

        if all:
            out_string += '\t\t# Create new {} models.\n'.format(model_name)
            out_string += '\t\tself.create_model_logout(self.data, \'standard\', self.user_{})\n'.format(
                    user if user is not None else 'admin')
            out_string += '\t\tself.create_model_logout(self.data, \'modified\', self.user_{})\n'.format(
                    user if user is not None else 'admin')
            out_string += '\n'
        else:
            out_string += '\t\t# Create new {} models, storing URL.\n'.format(model_name)
            out_string += '\t\turl = self.create_model_logout(self.data, \'standard\', self.user_{})\n'.format(
                    user if user is not None else 'admin')
            out_string += '\n'

        # Create required login
        if user is not None:
            out_string += '\t\t# Log in as {}.\n'.format(user)
            out_string += '\t\tself.login_user(self.user_{})\n'.format(user)
            out_string += '\n'

        # Determine if get was successful
        retrieve_successful = False
        if user in model_data['permissions'] and 'GET' in model_data['permissions'][user]:
            retrieve_successful = True
        elif user is None and not model_data['requires_authentication']:
            retrieve_successful = True

        out_string += '\t\t# Make get request and ensure {} response\n'.format(
                'OK' if retrieve_successful else 'unauthorized')
        out_string += '\t\tresponse = self.client.get({})\n'.format('self.format_url(self.data.url)' if all else 'url')

        if retrieve_successful:
            out_string += '\t\tself.assertEqual(response.status_code, status.HTTP_200_OK)\n'
            if all:
                out_string += '\t\tself.assertTrue(self.does_contain_data_list(response.data[\'results\'], [self.data.standard, self.data.modified]))\n'
            else:
                out_string += '\t\tself.assertTrue(self.does_contain_data(response.data, self.data.standard))\n'
        else:
            out_string += '\t\tself.assertIn(response.status_code, self.status_forbidden)\n'

        out_string += '\n\n'

        return out_string

    def generate_update_tests(self, model_name, model_data):
        return '\t# TODO: Write update tests\n'

    def generate_delete_tests(self, model_name, model_data):
        return '\t# TODO: Write delete tests\n'

    """
    Output formatting for test data
    """

    def generate_app_data(self, app_name, app_data):
        # Create empty string for app file.
        app_string = str()

        app_string += self.generate_header_data(app_name, app_data) + '\n\n'

        app_string += '# Implementation\n'
        for model in app_data:
            app_string += '{}\n\n'.format(self.generate_model_data(model_name=model,
                                                                   model_data=app_data[model]))

        # Replace tabs with spaces
        out_string = str()
        for character in app_string:
            if character is '\t':
                out_string += '    '
            else:
                out_string += character

        return out_string

    def generate_header_data(self, app_name, app_data):
        out_string = str()

        # Format the dependency imports header for app file.
        out_string += '# Rest Imports\n'
        out_string += 'from rest_framework import status\n'

        # Format the local imports header for app file.
        out_string += '# Local Imports\n'
        out_string += 'from {}.abstract.test_data import {}TestData\n'.format(settings.TEST_BUILDER_PREFIX,
                                                                              snake_to_bumpy(
                                                                                      settings.TEST_BUILDER_PREFIX))

        # Make initial formatting for model imports
        model_import = 'from {}.models import'.format(app_name)

        # Iterate over apps models, creating necessary imports.
        first_iteration = True
        for model in app_data:
            model_import += (' ' if first_iteration else ', ') + model
            first_iteration = False

        out_string += model_import + '\n'

        return out_string

    def generate_model_data(self, model_name, model_data):
        out_string = str()

        out_string += 'class {}TestData({}TestData):\n'.format(model_name,
                                                               snake_to_bumpy(settings.TEST_BUILDER_PREFIX))
        out_string += '\t\"\"\"\n'
        out_string += '\tTest data for {}\n'.format(model_name)
        out_string += '\t\"\"\"\n'
        out_string += '\n'
        out_string += '\tmodel = {}\n'.format(plain_to_bumpy(model_name))
        out_string += '\turl = \'{}\'\n'.format(model_data['url'])
        out_string += '\n'

        out_string += self.generate_test_data(model_data=model_data)

        return out_string

    def generate_test_data(self, model_data):
        out_string = str()

        field_data = model_data['fields']
        out_string += self.generate_formatted_data(field_data=field_data)
        out_string += '\n'
        out_string += self.generate_formatted_data(field_data=field_data,
                                                   name='modified')
        out_string += '\n'

        for field in field_data:
            varient_data = self.generate_varient_data(field_name=field,
                                                      field_data=field_data[field])
            for varient in varient_data:
                out_string += self.generate_formatted_data(field_data=field_data,
                                                           name=varient,
                                                           modified_field=varient_data[varient])
                out_string += '\n'

        return out_string

    def generate_formatted_data(self, field_data, name='standard', modified_field=None):
        out_string = str()

        out_string += '\t{} = {{\n'.format(name)

        for field in field_data:
            if modified_field is not None and field is modified_field['field']:
                if modified_field['line'] is not None:
                    out_string += modified_field['line']
            else:
                out_string += '\t\t\'{}\': {},\n'.format(field,
                                                         self.generate_data(field_name=field,
                                                                            field_data=field_data[field]))

        out_string += '\t}\n'

        return out_string

    def generate_data(self, field_name, field_data, prefix='standard'):
        out_string = str()

        if 'default' in field_data:
            out_string += field_data['default']
        elif 'choices' in field_data:
            choice = field_data['choices'][0 if prefix == 'standard' else -1]
            out_string += ('{}' if type(choice) == int else '\'{}\'').format(choice)
        else:
            field_type = field_data['type']
            if field_type == 'BooleanField':
                out_string += 'True' if prefix == 'standard' else 'False'
            elif field_type == 'CharField':
                char = '{}_char'.format(prefix)
                out_string = '\'{}\''.format(char[:field_data['max_length']])
            elif field_type == 'DateField':
                out_string = '\'{}\''.format(
                        '2015-01-20' if prefix == 'standard' else '2015-02-20')  # TODO: Figure out if this needs anything more complex
            elif field_type == 'EmailField':
                email = '{}_email'.format(prefix)
                out_string = '\'{}\'@d.io'.format(
                        email[:-field_data['max_length']])  # TODO:  Check that this is how this field actually works
            elif field_type == 'IntegerField':
                integer = '12345' if prefix == 'standard' else '54321'
                if 'max_length' in field_data:
                    integer = integer[:field_data['max_length']]
                out_string = '{}'.format(integer)
            elif field_type == 'SlugField':
                slug = '{}_slug'.format(prefix)
                out_string = '\'{}\''.format(slug[:field_data['max_length']])
            elif field_type == 'TextField':
                text = '{}_text'.format(prefix)
                out_string = '\'{}\''.format(text[:field_data['max_length']])
            elif field_type == 'ForeignKey':
                out_string += '\'REQUIRES: {}\''.format(field_data['related_model'])  # TODO:   Make this work properly
            elif field_type == 'OneToOne':
                out_string += '\'REQUIRES: {}\''.format(field_data['related_model'])  # TODO:   Make this work properly
            elif field_type == 'ManyToMany':
                out_string += '\'REQUIRES: {}\''.format(field_data['related_model'])  # TODO:   Make this work properly
            else:
                out_string = '\'default\''

        return out_string

    def generate_varient_data(self, field_name, field_data):
        out_dict = dict()
        out_dict.update({
            'missing_{}'.format(field_name): {
                'field': field_name,
                'line': None
            },
            'modified_{}'.format(field_name): {
                'field': field_name,
                'line': '\t\t\'{}\': {},\n'.format(field_name, self.generate_data(field_name=field_name,
                                                                                  field_data=field_data,
                                                                                  prefix='modified'))
            }
        })

        # TODO: Get individual model varients

        return out_dict
