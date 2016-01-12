import json
import os
from logging import getLogger

from django.apps import *
from django.conf import settings
from django.http import HttpResponse
from rest_framework.views import APIView

from .models import TestDataFieldReference

log = getLogger(__name__)


class TestDataBuilder(APIView):
    test_data_file_handle = None
    test_file_handle = None

    directory_name = None

    field_types = {}

    app_data = {}

    def get(self, request):
        app_configs = apps.get_app_configs()

        ignore_apps = settings.TEST_BUILDER_IGNORED_APPS

        for app in app_configs:
            if app.name not in ignore_apps and app.name.startswith(settings.TEST_BUILDER_PREFIX):
                log.debug("Found app : " + str(app.name))

                model_app_data = {}
                for curr_model in apps.get_models(app.name):

                    # avoid inheritance and abstraction - check if the model actually belongs to the app
                    if app.name in str(curr_model):
                        log.debug("Model :: " + str(curr_model))
                        model_app_data[curr_model._meta.verbose_name_raw] = self.model_to_json(curr_model)

                        # log.debug("Results for " + app.name + " :: " + str(model_app_data))

                self.app_data[app.name] = model_app_data
                file_contents = self.generate_test_data(app_name=app.name)
                self.export_test_data(app.name, file_contents)

        return HttpResponse(str(self.field_types))

    def update_test_data_field_reference(self, field_type):
        TestDataFieldReference.objects.update_or_create(field_type=field_type)

    def model_to_json(self, model):

        # get all the fields for the model (returned <format, fieldname>)
        model_fields = model._meta.get_fields(include_parents=False, include_hidden=False)

        model_dict = {}
        test_data_dict = {}

        app_data = {}

        # convert model_fields to dictionary of fieldname -> internal type
        for field in model_fields:
            # log.debug("Field :: " + str(field.name) + " Type ::" + field.get_internal_type())

            # ignoring the field we don't control or use in tests

            ignore_fields = ['id', 'created', 'modified']

            if field.name not in ignore_fields:
                model_dict[field.name] = field.get_internal_type()
                test_data_dict[field.name] = ''
                self.update_test_data_field_reference(field.get_internal_type())

        app_data['model'] = model_dict
        app_data['data'] = test_data_dict

        return app_data

    def generate_test_data(self, app_name):

        app_data = self.app_data[app_name]

        model_data = {}
        for model, data in app_data.items():
            test_data = {}
            model_dict = app_data[model]['model']
            test_data['standard'] = self.populate_data(model_dict)
            data_name_prefixes = ['missing', 'modified']  # , 'too_long_', 'too_short_', 'wrong_type_']

            for key, value in model_dict.items():
                for prefix in data_name_prefixes:
                    field_modification = {key: prefix}
                    test_data[prefix + '_' + key] = self.populate_data(model_dict, field_modification)

            model_underscore = model.replace(" ", "_")
            model_data[model_underscore] = test_data

        test_data_file_contents = model_data

        return test_data_file_contents

    def populate_data(self, model_dict, field_modification={}):
        test_data = {}

        for key, value in model_dict.items():

            if key in field_modification:
                if field_modification[key] is 'missing':
                    test_data[key] = ''

                elif field_modification[key] is 'modified':
                    test_data[key] = TestDataFieldReference.objects.get(field_type=value).modified_value

            else:
                test_data[key] = TestDataFieldReference.objects.get(field_type=value).standard_value

            # TODO how are we going to do related things... this doesn't work so well right now
            # log.debug("test_data[key] ::" + str(test_data[key]))
            # if test_data[key] == "null":
            #     log.debug("Processing null")
            #     test_data[key] = None

        return test_data

    def create_app_directory(self, app_name):

        directory_name = settings.TEST_BUILDER_DIRECTORY + "" + app_name

        log.debug(" Attempting to create app directory for " + app_name)

        try:
            os.makedirs(directory_name)
        except FileExistsError as e:
            pass

        return directory_name

    def export_test_data(self, app_name, test_data):

        directory_name = self.create_app_directory(app_name)

        file_name = directory_name + '/test_data.py'

        prefix = "data = "
        json_string = json.dumps(obj=test_data, sort_keys=True, indent=4, separators=(',', ': '))
        file_contents = prefix + json_string

        with open(file_name, 'w') as outfile:
            print(file_contents, file=outfile)
        outfile.close()
