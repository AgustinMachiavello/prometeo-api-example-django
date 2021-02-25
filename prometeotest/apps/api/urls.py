"""
Prometeo API URLs
"""

# Django

from django.urls import include, path

# Views
from .views.api import (
    LoginAPIView, 
    GetUser,
    GetAccount,
    GetProvidersList,
)


# {{doamin}}/api/<page>
urlpatterns = [
    path('login/', LoginAPIView.as_view(), name='login'),
    path('info/', GetUser.as_view(), name='get_user'),
    path('account/', GetAccount.as_view(), name='get_account'),
    path('provider/', GetProvidersList.as_view(), name='get_provider_list'),
]
