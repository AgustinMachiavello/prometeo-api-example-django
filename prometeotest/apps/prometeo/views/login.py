"""
Login page
"""

# Django
from django.http.response import HttpResponse
from django.views.generic import TemplateView
from django.shortcuts import render, redirect, reverse


class LoginTemplateView(TemplateView):
    """
    Login page for the prometeo api

    Retrieves session key
    """

    template_name = 'pages/login.html'
    context = {}

    def get(self, request):
        return render(request, self.template_name, self.context)
    
    """
    # TODO Delete? We are calling the API not this view post
    def post(self, request):
        email = request.POST.get('email', None)
        password = request.POST.get('password', None)
        print(email, password) # TODO call API point and if OK proceed to page
        return HttpResponse('LoginTemplateView')"""
