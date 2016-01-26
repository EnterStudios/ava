# Django Imports
from django.conf import settings
from django.contrib.auth.models import User
# Rest Imports
from rest_framework import status
from rest_framework.test import APITestCase
# Local Imports



# Implementation
class AvaTest(APITestCase):
    """
    Test setup
    """

    def setUp(self):
        # Create required users
        self.user_admin = {'email': 'admin@test.com', 'password': 'test'}
        self.user_user = {'email': 'user@test.com', 'password': 'test'}
        self.user_other = {'email': 'other@test.com', 'password': 'test'}
        self.create_user(self.user_admin)
        self.create_user(self.user_user)
        self.create_user(self.user_other)

        # Create assert testing variables
        self.status_forbidden = {status.HTTP_401_UNAUTHORIZED, status.HTTP_403_FORBIDDEN}

    """
    Helper methods
    """

    def create_user(self, user):
        User.objects.create_user(username=user['email'], email=user['email'], password=user['password'])

    def login_user(self, user):
        return self.client.login(username=user['email'], email=user['email'], password=user['password'])

    def format_url(self, extension):
        return '{}{}'.format(settings.BASE_URL, extension)

    def create_model(self, data_set, data_name='standard', owner=None):
        data = data_set.get_data(data_name)
        if owner is not None and 'owner' in data:
            user = self.login_user(owner)
            data['owner'] = user

        model = data_set.model.objects.create(data)

        return '{}{}{}'.format(settings.BASE_URL, data.url, model.id)

    def create_model_logout(self, data_set, data_name='standard', owner=None):
        url = self.create_model(data_set=data_set,
                                data_name=data_name,
                                owner=owner)

        self.client.logout()

        return url

    def does_contain_data(self, data_target, data_source):
        return_value = True

        # Iterate over source items checking that target has matching items
        for key in data_source.keys():
            if data_source[key] != data_target[key]:
                return_value = False
                break

        return return_value

    def does_contain_data_list(self, data_list_target, data_list_source):
        return_value = True

        # Iterate over values in target list, ensuring that match is found in source
        for data_target in data_list_target:
            found = False
            for data_source in data_list_source:
                found |= self.does_contain_data(data_target, data_source)

            if not found:
                return_value = False
                break

        return return_value

    def does_contain_data_url(self, data_target_url, data_source):
        # Log in as admin
        self.login_user(self.user_admin)

        # Make get request and ensure OK response
        response = self.client.get(data_target_url)

        # Return if data contains source
        return self.does_contain_data(response.data, data_source)

