"""
Login page
"""

# Django
from prometeotest.apps.api.views.api import GetProvidersList, LoginAPIView
from django.http.response import HttpResponseRedirect
from django.views.generic import TemplateView
from django.shortcuts import render, redirect, reverse


# Json
import json

# Forms
from ..forms.login import LoginForm


class LoginTemplateView(TemplateView):
    """
    Login page for the prometeo api
    """

    template_name = 'pages/login.html'
    context = {}

    def get(self, request):
        self.context['form'] = None
        if request.session.get('session_key', None):
            pass
            # TODO offer to login as User
        self.context['providers'] =  GetProvidersList.as_view()(request).data
        return render(request, self.template_name, self.context)
    

    def post(self, request, *args, **kwargs):
        form = LoginForm(request.POST)
        if form.is_valid():
            provider = form.cleaned_data['provider']
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            login_request =  LoginAPIView.as_view()(request).data
            return HttpResponseRedirect(reverse('prometeo:account'))
        self.context['form'] = form # TODO Catch errors
        return render(request, self.template_name, self.context)
