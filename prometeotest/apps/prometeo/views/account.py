"""
Account page
"""

# Django
from prometeotest.apps.api.views.api import GetAccount, GetMovementsList, GetUser
from django.http.response import HttpResponse, HttpResponseRedirect
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
    movements_limit = 5

    def get(self, request):
        try:
            # TODO You'll see this TRY-EXCEPT repeated. I tried to make it a function but the APIView would ignore it
            # I don't know why yet, I'll try to fix this with more investigation.
            request.session['session_key']
        except KeyError as e:
            return redirect(reverse('prometeo:login'))
            
        request_errors = []
        user_request =  GetUser.as_view()(request).data
        account_request =  GetAccount.as_view()(request).data
        movements_list = []

        if is_request_success(user_request):
            self.context['user_info'] =  user_request['info']
        else:
            self.context['request_errors'] = request_errors.append(get_request_status_message(user_request))
        if is_request_success(account_request):
            self.context['accounts'] =  account_request['accounts']
        else:
            self.context['request_errors'] = request_errors.append(get_request_status_message(account_request))

        for account in self.context['accounts']:
            # TODO this can be optimized or move to another page
            try:
                movements_account = GetMovementsList.as_view()(request).data
                if len(movements_account['movements']) < self.movements_limit:
                    movements = movements_account['movements'][:len(movements_account['movements'])] # Limit movements
                else:
                    movements = movements_account['movements'][:self.movements_limit]
                movements_list.append(movements)
            except KeyError as e:
                print(e)
                continue
        try:
            if len(self.context['request_errors']) > 1:
                return reverse(reverse('prometeo:login'))
        except KeyError:
            pass
        self.context['movements'] = movements_list
        return render(request, self.template_name, self.context)
    