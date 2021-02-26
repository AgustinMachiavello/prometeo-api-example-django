"""
API helpers
"""

# Django
from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect, reverse
from rest_framework.response import Response


ERROR_MESSAGE_CODES = {
    'select_client': 'Please, select a client',
    'wrong_credentials': 'Invalid user or password',
    'missing_credentials': 'Credential field missing',
    'logged_in': 'Successful login',
    'interaction_required': 'Interaction required. It can be a Captcha or a security question',
    'misssing_credentials': 'Missing credentials',
}

def get_request_status(request_json):
    try:
        return request_json['status']
    except KeyError as e:
        print(e) # TODO Do something with the exception
    return None


def is_request_success(request_json):
    is_success = False
    try:
        status = request_json['status']
        if status == 'success' or status == 'logged_in':
            is_success = True
    except KeyError as e:
        print(e) # TODO Do something with the exception
    return is_success


def get_request_status_message(request_json):
    try:
        return request_json['message']
    except KeyError as e:
        print(e) # TODO Do something with the exception
    try:
        return ERROR_MESSAGE_CODES.get(request_json['status']) or 'Something went wrong :('
    except KeyError as e:
        print(e) # TODO Do something with the exception
    return 'Something went wrong :('
