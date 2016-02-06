# Django Imports

from django.conf import settings
from django.contrib.auth.models import User
# Rest Imports
from rest_framework import status
from rest_framework.test import APITestCase


# Implementation
class AvaCoreTest(APITestCase):

    users = {
        'admin': {'email': 'admin@test.com', 'password': 'test'},
        'user': {'email': 'user@test.com', 'password': 'test'},
        'other': {'email': 'other@test.com', 'password': 'test'},
    }

    status_forbidden = {status.HTTP_401_UNAUTHORIZED, status.HTTP_403_FORBIDDEN}

    def setUp(self):
        # Create required users
        for key, user in self.users.items():
            self.create_user(user)
            new_user = User.objects.get(email=user['email'])
            user['id'] = new_user.id
            user['obj'] = new_user

    def create_user(self, user):
        User.objects.create_user(username=user['email'], email=user['email'], password=user['password'])

    def login_user(self, user):
        return self.client.login(username=user['email'], email=user['email'], password=user['password'])

    def format_url(self, extension):
        return '{}{}'.format(settings.BASE_URL, extension)

    # def create_model(self, data_set, data_name='standard', owner=None):
    #     data = data_set.get_data_with_owner(owner=owner, name=data_name)
    #
    #     # Log in as user.
    #     self.login_user(self.user_user)
    #
    #     if data:
    #         data_set.init_requirements(owner)
    #
    #         # Make post request and ensure created response.
    #         response = self.client.post(self.format_url(data_set.url), data, format='json')
    #         # model = data_set.model.objects.create(**data)
    #         if response.status_code is 201:
    #             url = response.data['url']
    #             return url
    #         else:
    #             print("Failed to create model : " + str(response) + " Data :: " + str(response.data))
    #     else:
    #         return False
    #
    # def create_model_logout(self, data_set, data_name='standard', owner=None):
    #     url = self.create_model(data_set=data_set,
    #                             data_name=data_name,
    #                             owner=owner)
    #
    #     self.client.logout()
    #
    #     return url
    #
    # def does_contain_data(self, data_target, data_source):
    #     return_value = True
    #
    #     # Iterate over source items checking that target has matching items
    #     for key in data_source.keys():
    #         if key not in data_target:
    #             return_value = False
    #             break
    #
    #         if data_source[key] != data_target[key]:
    #             return_value = False
    #             break
    #
    #     return return_value
    #
    # def does_contain_data_list(self, data_list_target, data_list_source):
    #     return_value = True
    #
    #     # Iterate over values in target list, ensuring that match is found in source
    #     for data_target in data_list_target:
    #         found = False
    #         for data_source in data_list_source:
    #             found |= self.does_contain_data(data_target, data_source)
    #
    #         if not found:
    #             return_value = False
    #             break
    #
    #     return return_value
    #
    # def does_contain_data_url(self, data_target_url, data_source):
    #     # Log in as admin
    #     self.login_user(self.user_admin)
    #
    #     # Make get request and ensure OK response
    #     response = self.client.get(data_target_url)
    #
    #     # Return if data contains source
    #     return self.does_contain_data(response.data, data_source)
