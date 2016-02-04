# Python Imports
from logging import getLogger
import json
import os
import shutil
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


def write_to_file(path, data, archive_old=False):
    # Check that the setting for storing locally is true.
    # True - Update path to be within the media file for test builder.
    if settings.TEST_BUILDER_STORE_TEMP:
        path_split = path.rsplit('/', 1)
        directory = '{}output/{}/'.format(settings.TEST_BUILDER_DIRECTORY, path_split[0])

        # Attempt to create the new directory.
        # Directory exists on exception.
        try:
            os.makedirs(directory)
        except FileExistsError:
            pass

        # Update the used path variable
        path = directory + path_split[1]

    # Check that the file already exists and archiving is set.
    # True - copy current file with '.old_n' prefixed (where n is the first available digit).
    if os.path.isfile(path) and archive_old and not settings.TEST_BUILDER_FORCE_NO_ARCHIVE:
        # Create template for path format.
        path_template = '{}.old_{{}}'.format(path)

        # Create initial path
        archive_digit = 0
        old_path = path_template.format(archive_digit)

        # Increment archive digit until a file is not found.
        while os.path.isfile(old_path):
            archive_digit += 1
            old_path = path_template.format(archive_digit)

        # Copy current file to old file.
        shutil.copyfile(path, old_path)

    # Output data to path
    with open(path, 'w') as outfile:
        print(data, file=outfile)
    outfile.close()


"""
Creates the data for a project
"""


class ProjectDataBuilder(APIView):
    def get(self, request):
        # Load settings from Django.
        prefix = settings.TEST_BUILDER_INPUT_APP_PREFIX
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
        directory_name = settings.TEST_BUILDER_DIRECTORY
        try:
            os.makedirs(directory_name)
        except FileExistsError:
            pass

        # Format output file name and output json dump of project data.
        file_name = '{}{}.json'.format(directory_name, settings.TEST_BUILDER_PROJECT_DATA_OUTPUT)
        json_data = json.dumps(obj=project_data,
                               sort_keys=True,
                               indent=4,
                               separators=(',', ': '))
        write_to_file(file_name, json_data, True)

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
            file_name = '{}{}.json'.format(settings.TEST_BUILDER_DIRECTORY,
                                           settings.TEST_BUILDER_PROJECT_DATA_INPUT)
            with open(file_name) as data_file:
                self.project_data = json.load(data_file)
            data_file.close()
        except:
            return HttpResponse('No input file.', status=status.HTTP_400_BAD_REQUEST)

        # Attempt to copy template file to new directory.
        # Return bad request response on failure.
        try:
            # Take a copy of the template data.
            file_name = '{}test_template.py'.format(settings.TEST_BUILDER_DIRECTORY)
            with open(file_name) as data_file:
                # Create file path for the output of copy.
                directory_name = '{}/test.py'.format(settings.TEST_BUILDER_ABSTRACT_DIRECTORY)

                # Format the data for appropriate usage.
                data = data_file.read().format(project_name_snake=settings.TEST_BUILDER_INPUT_APP_PREFIX,
                                               project_name_bumpy=snake_to_bumpy(
                                                   settings.TEST_BUILDER_OUTPUT_APP_PREFIX))

                # Write the data to file.
                write_to_file(directory_name, data)

            # Close the file handle.
            data_file.close()
        except FileNotFoundError:
            return HttpResponse('No test template file.', status=status.HTTP_400_BAD_REQUEST)

        # Attempt to copy template file to new directory.
        # Return bad request response on failure.
        try:
            # Take a copy of the template data.
            file_name = '{}test_data_template.py'.format(settings.TEST_BUILDER_DIRECTORY)
            with open(file_name) as data_file:
                # Create file path for the output of copy.
                directory_name = '{}/test_data.py'.format(settings.TEST_BUILDER_ABSTRACT_DIRECTORY)

                # Format the data for appropriate usage.
                data = data_file.read().format(project_name=snake_to_bumpy(settings.TEST_BUILDER_OUTPUT_APP_PREFIX))

                # Write the data to file.
                write_to_file(directory_name, data)

            # Close the file handle.
            data_file.close()
        except FileNotFoundError:
            return HttpResponse('No test data template file.', status=status.HTTP_400_BAD_REQUEST)

        # Iterate over apps in project data, creating all necessary files.
        for app, app_name in self.project_data.items():
            # Create the test and data files for app.
            test_output = self.generate_app_test(app_name=app,
                                                 app_data=self.project_data[app])
            data_output = self.generate_app_data(app_name=app,
                                                 app_data=self.project_data[app])

            # Create output directory name.
            directory_name = '{}/{}/'.format(settings.TEST_BUILDER_OUTPUT_APP_PREFIX,
                                             app.split('.', 1)[1].replace('.', '/'))

            # Format output file name and output test and test data.
            test_file = '{}tests.py'.format(directory_name)
            write_to_file(test_file, test_output, True)

            test_file = '{}test_data.py'.format(directory_name)
            write_to_file(test_file, data_output, True)

        return HttpResponse('Success.', status=status.HTTP_200_OK)

    """
        Helper functions
    """

    def get_model_data_from_name(self, model_name):
        # Iterate over apps in project.
        for app, app_data in self.project_data.items():
            # Iterate over models in app.
            for model, model_data in app_data.items():
                # Check if current model name is the same as that passed.
                # True - return the models data
                if model in model_name:
                    return model_data

        return None

    """
    Output formatting for tests
    """

    def generate_app_test(self, app_name, app_data):
        # Create empty string for app file.
        app_string = str()

        # Store app information for future reference.
        self.current_app_name = app_name
        self.current_app_data = app_data

        # Add header data to out string.
        app_string += self.generate_header_test(app_name=app_name,
                                                app_data=app_data) + '\n\n'

        # Iterate over models in app, adding data to out string.
        app_string += '# Implementation\n'
        for model, model_data in app_data.items():
            app_string += self.generate_model_test(model_name=model,
                                                   model_data=model_data)
            app_string += '\n'

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
        out_string += 'from {}.abstract.test import {}Test\n' \
            .format(settings.TEST_BUILDER_OUTPUT_APP_PREFIX,
                    snake_to_bumpy(settings.TEST_BUILDER_OUTPUT_APP_PREFIX))

        # Make initial formatting for model imports
        data_import = 'from {}.{}.test_data import'.format(settings.TEST_BUILDER_OUTPUT_APP_PREFIX,
                                                           app_name.split('.', 1)[1])

        # Iterate over apps models, creating necessary imports.
        first_iteration = True
        for model in app_data:
            data_import += (' ' if first_iteration else ', ') + model + 'TestData'
            first_iteration = False

        out_string += data_import + '\n'

        return out_string

    def generate_model_test(self, model_name, model_data):
        out_string = str()

        # Create test model header
        out_string += 'class {}Test({}Test):\n'.format(model_name,
                                                       snake_to_bumpy(settings.TEST_BUILDER_OUTPUT_APP_PREFIX))
        out_string += '\t\"\"\"\n'
        out_string += '\t{} Test\n'.format(model_name)
        out_string += '\t\"\"\"\n'
        out_string += '\n'

        # Create setup for tests
        out_string += '\tdef setUp(self):\n'
        out_string += '\t\t# Make call to super.\n'
        out_string += '\t\tsuper({}Test, self).setUp()\n'.format(snake_to_bumpy(model_name))
        out_string += '\n'
        out_string += '\t\t# Set the data type.\n'
        out_string += '\t\tself.data = {}TestData\n'.format(model_name)
        out_string += '\t\tself.data.init_requirements()\n'
        out_string += '\n'

        # Create each of the CRUD test functions
        out_string += self.generate_create_tests(model_name, model_data)
        out_string += self.generate_retrieve_tests(model_name, model_data)
        out_string += self.generate_update_tests(model_name, model_data)
        out_string += self.generate_delete_tests(model_name, model_data)

        return out_string

    def generate_create_tests(self, model_name, model_data):
        out_string = str()

        # Create tests as user, admin and unauthenticated.
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
        out_string += '\t\tdata = self.data.get_data(\'standard\')\n'
        out_string += '\n'

        # Create push request
        out_string += '\t\t# Make post request and ensure {} response.\n'.format(
            'created' if create_successful else 'unauthorized')
        out_string += '\t\tresponse = self.client.post(self.format_url(self.data.url), data, format=\'json\')\n'

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

        if 'requires_owner' in model_data and model_data['requires_owner']:
            out_string += '\t# TODO:\tWrite retrieve owner tests'
            pass
        return out_string

    def generate_retrieve_as_tests(self, model_name, model_data, all=False, user=None):
        out_string = str()

        out_string += '\tdef test_{}_retrieve_{}_as_{}(self):\n'.format(bumpy_to_snake(model_name),
                                                                        'all' if all else 'single',
                                                                        user if user is not None else 'unauthorized')

        if all:
            out_string += '\t\t# Create new {} models.\n'.format(model_name)
            out_string += '\t\tself.create_model_logout(self.data, data_name=\'standard\', owner=self.user_{})\n'.format(
                user if user is not None else 'admin')
            out_string += '\t\tself.create_model_logout(self.data, data_name=\'modified\', owner=self.user_{})\n'.format(
                user if user is not None else 'admin')
            out_string += '\n'
        else:
            out_string += '\t\t# Create new {} models, storing URL.\n'.format(model_name)
            out_string += '\t\turl = self.create_model_logout(self.data, data_name=\'standard\', owner=self.user_{})\n'.format(
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

        out_string += '\n'

        return out_string

    def generate_update_tests(self, model_name, model_data):
        out_string = str()

        out_string += self.generate_update_as_tests(model_name, model_data, True, 'user')
        out_string += self.generate_update_as_tests(model_name, model_data, False, 'user')
        out_string += self.generate_update_as_tests(model_name, model_data, True, 'admin')
        out_string += self.generate_update_as_tests(model_name, model_data, False, 'admin')
        out_string += self.generate_update_as_tests(model_name, model_data, True)
        out_string += self.generate_update_as_tests(model_name, model_data, False)

        if 'requires_owner' in model_data and model_data['requires_owner']:
            out_string += '\t# TODO:\tWrite update owner tests'
            pass

        return out_string

    def generate_update_as_tests(self, model_name, model_data, exists=False, user=None):
        out_string = str()

        out_string += '\tdef test_{}_update_{}_as_{}(self):\n'.format(bumpy_to_snake(model_name),
                                                                      'exists' if exists else 'does_not_exist',
                                                                      user if user is not None else 'unauthorized')

        if exists:
            out_string += '\t\t# Create new {} models, storing URL.\n'.format(model_name)
            out_string += '\t\turl = self.create_model_logout(self.data, data_name=\'standard\', owner=self.user_{})\n' \
                .format(user if user is not None else 'admin')

        # Create required login
        if user is not None:
            out_string += '\t\t# Log in as {}.\n'.format(user)
            out_string += '\t\tself.login_user(self.user_{})\n'.format(user)
            out_string += '\n'

        # Determine if delete was successful
        put_successful = False
        if user in model_data['permissions'] and 'PUT' in model_data['permissions'][user]:
            put_successful = True
        elif user is None and not model_data['requires_authentication']:
            put_successful = True

        out_string += '\t\t# Make put request and ensure {} response.\n'\
            .format(('OK' if exists else 'not found') if put_successful else 'unauthorized')
        out_string += '\t\tresponse = self.client.put({}, self.data.get_data(\'unique\'))\n' \
            .format('url' if exists else 'self.format_url(self.data.url + \'/9999\')')

        if put_successful:
            if exists:
                out_string += '\t\tself.assertEqual(response.status_code, status.HTTP_200_OK)\n'
            else:
                out_string += '\t\tself.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)\n'
        else:
            out_string += '\t\tself.assertIn(response.status_code, self.status_forbidden)\n'

        if exists:
            out_string += '\t\tself.assertTrue(self.does_contain_data_url(url, self.data.{}))\n'\
                .format('unique' if put_successful else 'standard')

        out_string += '\n'

        return out_string

    def generate_delete_tests(self, model_name, model_data):
        out_string = str()

        out_string += self.generate_delete_as_tests(model_name, model_data, True, 'user')
        out_string += self.generate_delete_as_tests(model_name, model_data, False, 'user')
        out_string += self.generate_delete_as_tests(model_name, model_data, True, 'admin')
        out_string += self.generate_delete_as_tests(model_name, model_data, False, 'admin')
        out_string += self.generate_delete_as_tests(model_name, model_data, True)
        out_string += self.generate_delete_as_tests(model_name, model_data, False)

        if 'requires_owner' in model_data and model_data['requires_owner']:
            out_string += '\t# TODO:\tWrite delete owner tests'
            pass

        return out_string

    def generate_delete_as_tests(self, model_name, model_data, exists=False, user=None):
        out_string = str()

        out_string += '\tdef test_{}_delete_{}_as_{}(self):\n'.format(bumpy_to_snake(model_name),
                                                                      'exists' if exists else 'does_not_exist',
                                                                      user if user is not None else 'unauthorized')

        if exists:
            out_string += '\t\t# Create new {} models, storing URL.\n'.format(model_name)
            out_string += '\t\turl = self.create_model_logout(self.data, data_name=\'standard\', owner=self.user_{})\n' \
                .format(user if user is not None else 'admin')

        # Create required login
        if user is not None:
            out_string += '\t\t# Log in as {}.\n'.format(user)
            out_string += '\t\tself.login_user(self.user_{})\n'.format(user)
            out_string += '\n'

        # Determine if delete was successful
        delete_successful = False
        if user in model_data['permissions'] and 'DELETE' in model_data['permissions'][user]:
            delete_successful = True
        elif user is None and not model_data['requires_authentication']:
            delete_successful = True

        out_string += '\t\t# Make delete request and ensure {} response\n' \
            .format(('no content' if exists else 'not found') if delete_successful else 'unauthorized')
        out_string += '\t\tresponse = self.client.get({})\n' \
            .format('url' if exists else 'self.format_url(self.data.url + \'/9999\')')

        if delete_successful:
            if exists:
                out_string += '\t\tself.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)\n'
            else:
                out_string += '\t\tself.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)\n'
        else:
            out_string += '\t\tself.assertIn(response.status_code, self.status_forbidden)\n'

        if exists:
                out_string += '\t\tself.assertEqual(self.data.model.objects.count(), {})\n'\
                    .format('0' if delete_successful else '1')

        out_string += '\n'

        return out_string

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
        out_string += 'from {}.abstract.test_data import {}TestData\n' \
            .format(settings.TEST_BUILDER_OUTPUT_APP_PREFIX, snake_to_bumpy(settings.TEST_BUILDER_OUTPUT_APP_PREFIX))

        # Create a dictionary that contains all files that need to be imported.
        requirements_dict = dict()

        # Iterate over the models in the current app and add them.
        requirements_dict[app_name] = list()
        for model, model_data in app_data.items():
            # Check if current model isn't in the ignored list and currently in dictionary.
            # True - add to dictionary for current model.
            if model not in settings.TEST_BUILDER_IGNORED_MODELS and model not in requirements_dict[app_name]:
                requirements_dict[app_name].append(model)

        # Iterate over the app, model pairs in required imports.
        for app, models in requirements_dict.items():
            # Format the start of the import lines.
            required_models = 'from {}.{}.models import' \
                .format(settings.TEST_BUILDER_INPUT_APP_PREFIX, app.split('.', 1)[1])

            # Iterate over models using enumerate to keep a number.
            for count, model in enumerate(models):
                # Add formatted model to each string.
                # Use count to determine if space or comma used.
                required_models += (' ' if count == 0 else ', ') + model

            # Add required models to the output string.
            out_string += required_models + '\n'


        return out_string

    def generate_model_data(self, model_name, model_data):
        out_string = str()

        out_string += 'class {}TestData({}TestData):\n' \
            .format(model_name, snake_to_bumpy(settings.TEST_BUILDER_OUTPUT_APP_PREFIX))
        out_string += '\t\"\"\"\n'
        out_string += '\tTest data for {}\n'.format(model_name)
        out_string += '\t\"\"\"\n'
        out_string += '\n'


        # Create init requirements function
        related_string = str()
        related_string += "\t@staticmethod\n"
        related_string += "\tdef init_requirements():\n"

        had_requirement = False
        # Iterate over the fields of the models.
        for field, field_data in model_data['fields'].items():
            # Check if the field has a related_model attribute.
            # True - Create model for data.
            if 'related_model' in field_data:
                # Get the related models name and splitting at '.' from the reverse.
                # NOTE: The string is split two from reverse to separate the string into
                # app name, "model", model name. The word model is discarded, hence the use of 0 and 2 indexes.
                related_model = field_data['related_model'].rsplit('.', 2)

                # Check that the model starts with the prefix.
                # True - Create model for data.
                if related_model[0].startswith(settings.TEST_BUILDER_INPUT_APP_PREFIX):
                    had_requirement = True
                    required_name = related_model[2]

                    split_name = related_model[0].split('.', 1)[1]
                    if split_name not in self.current_app_name:
                        related_string += '\t\t# Import the required model and data\n'
                        related_string += '\t\tfrom {}.models import {}\n'\
                            .format(related_model[0], required_name)

                        related_string += '\t\tfrom {}.{}.test_data import {}TestData\n'\
                            .format(settings.TEST_BUILDER_OUTPUT_APP_PREFIX,
                                    split_name,
                                    required_name)

                    related_string += '\t\t# Check that requirements haven\'t already been created.\n'
                    related_string += '\t\t# True - Create necessary requirements.\n'
                    related_string += '\t\tif {}.objects.count() == 0:\n'.format(required_name)
                    related_string += '\t\t\t{}TestData.init_requirements()\n'.format(required_name)
                    related_string += '\t\t\tmodel = {0}.objects.create(**{0}TestData.get_data(\'standard\'))\n'.format(
                        required_name)
                    related_string += '\t\t\tmodel.save()\n'
                    related_string += '\t\t\tmodel = {0}.objects.create(**{0}TestData.get_data(\'unique\'))\n'.format(
                        required_name)
                    related_string += '\t\t\tmodel.save()\n'
                    related_string += '\n'

        # Check that the model hasn't had any requirements.
        # True - Add pass to the function body for init_requirements.
        if not had_requirement:
            related_string += '\t\tpass\n\n'

        out_string += '{}'.format(related_string)

        # Create required info
        out_string += '\t# Store self information\n'
        out_string += '\tmodel = {}\n'.format(plain_to_bumpy(model_name))
        out_string += '\turl = \'{}\'\n'.format(model_data['url'])
        out_string += '\n'

        # Create the test data and add to out string.
        out_string += self.generate_test_data(model_data=model_data)

        return out_string

    def generate_test_data(self, model_data):
        out_string = str()

        # Take reference to models field data.
        fields = model_data['fields']

        # Create standard formatted data and add to out string.
        out_string += self.generate_formatted_data(field_data=fields)
        out_string += '\n'

        # Create unique formatted data and add to out string.
        out_string += '\tunique = {\n'
        # Iterate over fields creating the appropriate data for each.
        for field, field_data in fields.items():
            out_string += '\t\t\'{}\': {},\n' \
                .format(field, self.generate_data(field_name=field, field_data=field_data, prefix='unique'))
        out_string += '\t}\n\n'

        # Iterate over fields for model creating the required variant pairs for each, outputting formatted data.
        for field, field_data in fields.items():
            variant_dict = self.generate_variant_data(field_name=field,
                                                      field_data=field_data)
            # Iterate over variant dictionary creating the appropriately formatted data for out string.
            for variant, variant_data in variant_dict.items():
                out_string += self.generate_formatted_data(field_data=fields,
                                                           name=variant,
                                                           modified_field=variant_data)
            out_string += '\n'

        return out_string

    def generate_formatted_data(self, field_data, name='standard', modified_field=None):
        out_string = str()

        # Create data header
        out_string += '\t{} = {{\n'.format(name)

        # Iterate over fields, creating appropriate data given passed parameters.
        for field, attributes in field_data.items():
            # Check that the current field is the desired modified field.
            # True - Add variant line to out string.
            # False - Add standard formatted line to outstring.
            if modified_field is not None and field is modified_field['field']:
                # Check that line isn't blank.
                # True - Add line to out string.
                if modified_field['line'] is not None:
                    out_string += modified_field['line']
            else:
                out_string += '\t\t\'{}\': {},\n' \
                    .format(field, self.generate_data(field_name=field, field_data=attributes))

        out_string += '\t}\n'

        return out_string

    def generate_data(self, field_name, field_data, prefix='standard'):
        out_string = str()

        # This is a mess of code that needs to be refactored at sometime in the hopefully near future TODO:
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
                model_data = self.get_model_data_from_name(field_data['related_model'])
                if model_data is not None:
                    out_string += '\'{}/{}/\''.format(model_data['url'], '1' if prefix == 'standard' else '2')
                else:  # TODO:   This will occur when user is the related field
                    out_string += '\'\''
            elif field_type == 'OneToOne':
                model_data = self.get_model_data_from_name(field_data['related_model'])
                if model_data is not None:
                    out_string += '\'{}/{}/\''.format(model_data['url'], '1' if prefix == 'standard' else '2')
                else:  # TODO:   This will occur when user is the related field
                    out_string += '\'\''
            elif field_type == 'ManyToMany':
                model_data = self.get_model_data_from_name(field_data['related_model'])
                if model_data is not None:
                    out_string += '\'{}/{}/\''.format(model_data['url'], '1' if prefix == 'standard' else '2')
                else:  # TODO:   This will occur when user is the related field
                    out_string += '\'\''
            else:
                out_string = '\'default\''

        return out_string

    def generate_variant_data(self, field_name, field_data):
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

        # TODO: Get individual model variants

        return out_dict
