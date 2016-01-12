from logging import getLogger

from django.apps import apps
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase, APIClient

log = getLogger(__name__)


class AVATestCase(APITestCase):
    status_forbidden = {status.HTTP_401_UNAUTHORIZED, status.HTTP_403_FORBIDDEN}
    user_admin = {'username': 'admin@test.com', 'email': 'admin@test.com', 'password': 'test'}
    user_standard = {'username': 'standard@test.com', 'email': 'standard@test.com', 'password': 'test'}

    def setUp(self):
        self.client = APIClient(enforce_csrf_checks=False)

        # Create required users
        self.setup_admin_user()
        self.setup_standard_user()

    def setup_standard_user(self):
        # log.debug("Setting up standard user")
        try:
            user = User.objects.create_user(username=self.user_standard['username'], email=self.user_standard['email'],
                                            password=self.user_standard['password'])
            user.save()
        except Exception as e:
            log.debug("Exception when trying to create standard user " + str(e))

    def setup_admin_user(self):
        # log.debug("Setting up staff user")
        try:
            user = User.objects.create_user(username=self.user_admin['username'], email=self.user_admin['email'],
                                            password=self.user_admin['password'], is_staff=True)
            user.save()
        except Exception as e:
            log.debug("Exception when trying to create admin user " + str(e))

    def setup_super_user(self):
        # log.debug("Setting up admin user")
        try:
            user = User.objects.create_superuser(username=self.user_admin['username'], email=self.user_admin['email'],
                                                 password=self.user_admin['password'])
            user.save()
        except Exception as e:
            log.debug("Exception when trying to create admin user " + str(e))

    def login_user(self, user):
        try:
            self.client.login(username=user['username'], password=user['password'])
        except Exception as e:
            log.debug("Exception when trying to authenticate as " + str(user['username']) + " Exception :: " + str(e))

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

    def create_data(self, user, test_data_attributes, request_data):
        # Log in as passed user
        self.login_user(user)

        # Store current count of queryset
        count = test_data_attributes.query_set.count()

        # Add new data and ensure created successfully
        response = self.client.post(test_data_attributes.url, request_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(test_data_attributes.query_set.count(), count + 1)
        self.assertTrue(self.does_contain_data(response.data, request_data))

        # Return formatted URL
        return response.data['url']

    def create_data_logout(self, user, test_data_attributes, request_data, via_api=True):

        if via_api:
            # Create data as user and store URL
            url = self.create_data(user=user, test_data_attributes=test_data_attributes, request_data=request_data)
        else:
            id = self.create_data_via_model(user=user, model_name=test_data_attributes.model_name, query_set=test_data_attributes.query_set,
                                            request_data=request_data)
            url = test_data_attributes.url_format.format(id)
        # Logout of user
        self.client.logout()

        # Return formatted URL
        return url

    def create_data_via_model(self, user, model_name, query_set, request_data):
        # Log in as passed user
        self.login_user(user)

        # Store current count of queryset
        count = query_set.count()

        # get the model for the item by model name using the django app registry
        current_model = apps.get_model(model_name)

        # create an object using the request data
        object = current_model.objects.create(**request_data)

        # check if the insert was successful
        self.assertEqual(query_set.count(), count + 1)

        # Return object id
        return object.id


def update_keys_value(self, data, key, value):
    # Take copy of data
    return_data = data

    # Update keys value
    return_data[key] = value

    # Return formatted data
    return return_data
