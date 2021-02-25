"""
Prometeo app URLs
"""

# Django
from django.urls import include, path

# Views
from .views import (
    LoginTemplateView,
    AccountTemplateView,
)


# {{doamin}}/<page>
urlpatterns = [
    path('', LoginTemplateView.as_view(), name='login_fallback'),
    path('login/', LoginTemplateView.as_view(), name='login'),
    path('account/', AccountTemplateView.as_view(), name='account'),
]
