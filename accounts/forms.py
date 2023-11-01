from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
from django.db import models
from django.utils.translation import gettext, gettext_lazy as _
from django.contrib.auth import password_validation


class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(max_length=100,
                                 required=True,
                                 widget=forms.TextInput(attrs={'placeholder': 'Name',
                                                               'class': 'form-control',
                                                               }))

    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'placeholder': 'Username',
                                                             'class': 'form-control',
                                                             }))
    email = forms.EmailField(required=True,
                             widget=forms.TextInput(attrs={'placeholder': 'Email',
                                                           'class': 'form-control',
                                                           }))
    password1 = forms.CharField(max_length=50,
                                required=True,
                                widget=forms.PasswordInput(attrs={'placeholder': 'Password',
                                                                  'class': 'form-control',
                                                                  'data-toggle': 'password',
                                                                  'id': 'password1',
                                                                  }))
    password2 = forms.CharField(max_length=50,
                                required=True,
                                widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password',
                                                                  'class': 'form-control',
                                                                  'data-toggle': 'password',
                                                                  'id': 'password2',
                                                                  }))
    PERMISSION_TYPE_CHOICES = (
        ("super_admin", "Super Admin"),
        ("admin", "Admin"),
    )
    permission_type = forms.ChoiceField(choices=PERMISSION_TYPE_CHOICES,
                                        widget=forms.Select(attrs={'class': 'form-control',}))

    class Meta:

        model = CustomUser
        fields = ['first_name', 'username', 'email', 'password1', 'password2', 'permission_type']


class CustomUserChangeForm(UserChangeForm):
    first_name = forms.CharField(max_length=100,
                                 required=True,
                                 widget=forms.TextInput(attrs={'placeholder': 'Name',
                                                               'class': 'form-control input-block',
                                                               }))

    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'placeholder': 'Username',
                                                             'class': 'form-control input-block',
                                                             }))
    email = forms.EmailField(required=True,
                             widget=forms.TextInput(attrs={'placeholder': 'Email',
                                                           'class': 'form-control input-block',
                                                           }))
    password1 = forms.CharField(
        label=_("Password"),
        strip=False,
        required=False,
        widget=forms.PasswordInput(attrs={'placeholder': 'Password',
                                          'class': 'form-control',
                                          'data-toggle': 'password',
                                          'id': 'password1',
                                          }))

    password2 = forms.CharField(
        label=_("Password confirmation"),
        strip=False,
        required=False,
        widget=forms.PasswordInput(attrs={'placeholder': 'Password',
                                          'class': 'form-control',
                                          'data-toggle': 'password',
                                          'id': 'password2',
                                          }))

    PERMISSION_TYPE_CHOICES = (
        ("super_admin", "Super Admin"),
        ("admin", "Admin"),
    )
    permission_type = forms.ChoiceField(choices=PERMISSION_TYPE_CHOICES,
                                        required=False,
                                        widget=forms.Select(attrs={'class': 'form-control',}))

    class Meta:

        model = CustomUser
        fields = ['first_name', 'username', 'email', 'password1', 'password2', 'permission_type']


class ChangePasswordForm(UserChangeForm):
    first_name = forms.CharField(required=False,
                                widget=forms.TextInput(attrs={'placeholder': 'Name',
                                                               'class': 'form-control input-block',
                                                               'id': 'first_name',
                                                               }))

    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Email',
                                                           'class': 'form-control input-block',
                                                           'id': 'email',
                                                           }))

    password1 = forms.CharField(
        label=_("Password"),
        strip=False,
        required=True,
        widget=forms.PasswordInput(attrs={'placeholder': 'Password',
                                          'class': 'form-control',
                                          'data-toggle': 'password',
                                          'id': 'password1',
                                          }))

    password2 = forms.CharField(
        label=_("Password confirmation"),
        strip=False,
        required=True,
        widget=forms.PasswordInput(attrs={'placeholder': 'Password',
                                          'class': 'form-control',
                                          'data-toggle': 'password',
                                          'id': 'password2',
                                          }))

    class Meta:
        model = CustomUser
        fields = ['first_name', 'email', 'password1', 'password2']
