"""
API Views
"""

# DJango
from django.http.response import HttpResponse, JsonResponse

# Django REST Framework

from rest_framework.views import APIView
from rest_framework.response import Response

# Requests
import requests

# Json
import json

# Settings
from django.conf import settings

# Helpers
from ...prometeo.helpers.api import is_request_success, get_request_status


def get_or_retrieve_session_key():
    """
    In case 
    """
    return 

class LoginAPIView(APIView):
    """
    View to retrieve session token
    """

    def post(self, request, format=None):
        response = requests.post(settings.API_BANK_HOST + '/login/', data={
            'provider': request.POST.get('provider'),
            'username': request.POST.get('username'),
            'password': request.POST.get('password'),
        }, headers={
            'X-API-Key': settings.API_KEY,
        })
        response_json = json.loads(response.text)
        print(response_json)
        if is_request_success(response_json):
            request.session['session_key'] = response_json['key'] # assign Prometeo API session key to Django secured session token
        return Response(response_json)


class GetUser(APIView):
    """
    View to retrieve user's information
    """

    def get(self, request, format=None):
        # TODO Check if ther is a session key before fetching
        response = requests.get(settings.API_BANK_HOST + '/info/', params={
            'key': request.session['session_key'],
        }, headers={
            'X-API-Key': settings.API_KEY,
        })
        response_json = json.loads(response.text)
        return Response(response_json)


class GetAccount(APIView):
    """
    View to retrieve user's account information
    """

    def get(self, request, format=None):
        # TODO Check if ther is a session key before fetching
        response = requests.get(settings.API_BANK_HOST + '/account/', params={
            'key': request.session['session_key'],
        }, headers={
            'X-API-Key': settings.API_KEY,
        })
        response_json = json.loads(response.text)
        return Response(response_json)


class GetProvidersList(APIView):
    """
    View to retrieve Prometeo's API available providers
    """

    def get(self, request, format=None):
        # TODO Check if ther is a session key before fetching
        response = requests.get(settings.API_BANK_HOST + '/provider/', params={
            'key': request.session['session_key'],
        }, headers={
            'X-API-Key': settings.API_KEY,
        })
        response_json = json.loads(response.text)
        return Response(response_json)