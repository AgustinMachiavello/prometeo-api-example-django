"""
Login page
"""

# Django
from rest_framework.response import Response
from prometeotest.apps.api.views.api import GetProvidersList, LoginAPIView
from django.http.response import HttpResponseRedirect
from django.views.generic import TemplateView
from django.shortcuts import render, redirect, reverse


# Json
import json

# Forms
from ..forms.login import LoginForm

# Helpers
from ..helpers.api import is_request_success, get_request_status, get_request_status_message


class LoginTemplateView(TemplateView):
    """
    Login page for the prometeo api
    """

    template_name = 'pages/login.html'
    context = {}

    def get(self, request):
        self.context['request_errors'] = None # Clear request errors
        self.context['form'] = LoginForm()
        if request.session.get('session_key', None):
            pass
            # TODO offer to login as User
        provider_request = GetProvidersList.as_view()(request).data
        if is_request_success(provider_request):
            self.context['providers'] =  provider_request['providers']
        else:
            self.context['request_errors'] = [get_request_status_message(provider_request),]
        if request.session.get('request_errors', None):
            self.context['request_errors'] = request.session.get('request_errors')
            del(request.session['request_errors'])
        if request.session.get('last_provider', None):
            # pre select last successful provider
            self.context['last_provider'] = request.session.get('last_provider')
            # del(request.session['last_provider'])
        return render(request, self.template_name, self.context)
    

    def post(self, request, *args, **kwargs):
        form = LoginForm(request.POST)
        if form.is_valid():
            provider = form.cleaned_data['provider']
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            login_request =  LoginAPIView.as_view()(request).data # POST data in request
            if is_request_success(login_request):
                request.session['last_provider'] = provider
                return HttpResponseRedirect(reverse('prometeo:account'))
            else:
                request.session['request_errors'] = [get_request_status_message(login_request),]
        self.context['form'] = form
        return redirect(reverse('prometeo:login'))