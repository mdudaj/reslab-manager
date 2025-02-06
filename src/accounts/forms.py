# -*- encoding: utf-8 -*-

from django import forms
from django.contrib.auth.forms import (
    AuthenticationForm,
    UserChangeForm,
    UserCreationForm,
)
from django.utils.translation import gettext_lazy as _

from .models import User


class CustomAuthenticationForm(AuthenticationForm):
    """Custom authentication form."""

    username = forms.CharField(
        label=_("Username"),
        widget=forms.TextInput(attrs={"autofocus": True, "class": "form-control"}),
    )
    password = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={"class": "form-control"}),
    )
