"""
Account page
"""

# Django
from prometeotest.apps.api.views.api import GetAccount, GetUser
from django.http.response import HttpResponse
from django.views.generic import TemplateView
from django.shortcuts import render, redirect, reverse


# Helpers
from ..helpers.api import is_request_success, get_request_status, get_request_status_message

class AccountTemplateView(TemplateView):
    """
    Account page for the prometeo api

    Retrieves session key
    """

    template_name = 'pages/account.html'
    context = {}

    def get(self, request):
        request_errors = []
        user_request =  GetUser.as_view()(request).data
        account_request =  GetAccount.as_view()(request).data
        if is_request_success(user_request):
            self.context['user_info'] =  user_request['info']
        else:
            self.context['request_errors'] = request_errors.append(get_request_status_message(user_request))
        if is_request_success(account_request):
            self.context['accounts'] =  account_request['accounts']
        else:
            self.context['request_errors'] = request_errors.append(get_request_status_message(account_request))
        return render(request, self.template_name, self.context)
    