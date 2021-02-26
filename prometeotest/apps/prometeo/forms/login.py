"""
Prometeo app form
"""

# DJango
from django import forms


class LoginForm(forms.Form):
    """
    Form used for the login page
    """
    provider = forms.CharField(max_length=20, required=True)
    username = forms.CharField(max_length=100, required=True)
    password = forms.CharField(required=True)

    def clean(self):
        cleaned_data = super(LoginForm, self).clean()
        provider = cleaned_data.get('provider')
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')
        if not username or not password or not provider:
            raise forms.ValidationError('Complete the required fields')