"""
Prometeo app URLs
"""

# Django
from django.urls import include, path

# Views
from .views import *


# {{doamin}}/<page>
urlpatterns = [
    path('login/', LoginTemplateView.as_view(), name='login'),
]
