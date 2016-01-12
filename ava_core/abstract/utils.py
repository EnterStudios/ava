import json
import logging

import requests
from django.conf import settings
from django.shortcuts import render, redirect

log = logging.getLogger(__name__)


def handle_error(request, context, status_code, error_message='Unknown Error'):
    log.debug("Called handle_error with status code :: " + str(status_code))
    # if status_code is 401 or 403:
    #     return redirect('login')
    # else:
    context['status_code'] = status_code
    context['error_message'] = error_message
    return False


def csrf_request(request, url, request_type='POST', api_data={}, headers={}, is_authenticated=False):

    # add authorization header to existing headers if is_authenticated == True
    if is_authenticated is True:
        if 'token' in request.session:
            headers['Authorization'] = 'JWT ' + request.session['token']

    # add csrf header to existing headers
    if request:
        headers['HTTP_X_CSRFTOKEN'] = request.COOKIES['csrftoken']

    try:
        if request_type is 'POST':
            return requests.post(url, data=api_data, headers=headers)
        elif request_type is 'GET':
            return requests.get(url, headers=headers)
        elif request_type is 'DELETE':
            return requests.delete(url, headers=headers)
        elif request_type is 'PUT':
            return requests.put(url, data=api_data, headers=headers)
    except ConnectionError as e:
        log.debug("Exception:: Connection Error " + e)
        return handle_error(None, '404')
