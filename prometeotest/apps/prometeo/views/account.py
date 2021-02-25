"""
Account page
"""

# Django
from prometeotest.apps.api.views.api import GetAccount
from django.http.response import HttpResponse
from django.views.generic import TemplateView
from django.shortcuts import render, redirect, reverse


class AccountTemplateView(TemplateView):
    """
    Account page for the prometeo api

    Retrieves session key
    """

    template_name = 'pages/account.html'
    context = {}

    def get(self, request):
        self.context['data'] =  GetAccount.as_view()(request).data
        return render(request, self.template_name, self.context)
    