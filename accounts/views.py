from socket import IP_DEFAULT_MULTICAST_LOOP
from django import forms
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic.edit import CreateView
from django.views.generic import View, UpdateView
from django.contrib import messages
from django.contrib.auth import get_user_model, password_validation, update_session_auth_hash, logout
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.utils.translation import gettext_lazy as _, ngettext_lazy
from django.shortcuts import render, get_object_or_404, redirect
from django.core.exceptions import ValidationError
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User

from .forms import CustomUserCreationForm, CustomUserChangeForm, ChangePasswordForm
from .models import CustomUser

class UserCreateView(CreateView):
    form_class = CustomUserCreationForm
    initial = {'key': 'value'}
    template_name = 'admin/add_user.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.name = user.email
            form.save()
            return redirect(to='admin_settings')

        return render(request, self.template_name, {'form': form})


class UserEditView(UpdateView):
    model = CustomUser
    form_class = CustomUserChangeForm
    template_name = 'admin/edit_user.html'
    initial = {'key': 'value'}
    success_url = '/settings'

    def get_object(self, queryset=None, **kwargs):
        return get_object_or_404(self.model, pk=self.kwargs['pk'])

    def post(self, request, *args, **kwargs):
        user = get_user_model().objects.get(pk=self.kwargs['pk'])
        form = self.form_class(request.POST)

        if(form["password1"].value() and form["password2"].value()):
            password1 = form["password1"].value()
            password2 = form["password2"].value()

            if password1 or password2:
                is_invalid_password = check_password(password1, password2)
                if is_invalid_password:
                    for error in is_invalid_password:
                        messages.error(self.request, error)
                    return HttpResponseRedirect(request.path_info)
            try:
             user.password = make_password(password1)
            except ValidationError as errors:
                return errors

        try:
            user.first_name = form["first_name"].value()
            user.email = form["email"].value()
            user.username = form["email"].value()
            user.permission_type = form["permission_type"].value()
            user.save()

            update_session_auth_hash(request, user)
            messages.success(self.request, 'User changed successfully')

            return HttpResponseRedirect(request.path_info)
        except ValidationError as errors:
            return errors


class UserChangePasswordView(UpdateView):
    model = CustomUser
    form_class = ChangePasswordForm
    template_name = 'admin/password_change.html'
    initial = {'key': 'value'}
    success_url = '/settings'

    def get_object(self, queryset=None):
        return get_object_or_404(self.model, pk=self.request.user.pk)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        password1 = form["password1"].value()
        password2 = form["password2"].value()
        first_name = form["first_name"].value()
        email = form["email"].value()

        is_invalid_password = check_password(password1, password2)
        if is_invalid_password:
            for error in is_invalid_password:
                messages.error(self.request, error)
            return HttpResponseRedirect(request.path_info)

        if form.is_valid():
            user = CustomUser.objects.get(username=self.request.user.username)
            user.password = make_password(password1)
            user.save()
            update_session_auth_hash(request, user)
            messages.success(self.request, 'Password changed successfully')

        return render(request, 'password_change.html',
                      {'form': form})


@login_required
def settings_view(request):
    return render(request, 'admin/settings.html')

@login_required(login_url='/admin')
def admin_settings_view(request):
    if request.user.is_superuser:
        all_users = get_user_model().objects.all()
        return render(request, 'admin_settings.html', {'users': all_users})
    else:
        return HttpResponseRedirect('/admin/')


@login_required(login_url='/admin')
def add_user_view(request):
    return render(request, 'add_user.html')


@login_required(login_url='/admin')
def delete_user(request, pk):
    user = get_user_model().objects.get(pk=pk)
    user.delete()

    return redirect('admin_settings')


def check_password(password1, password2):
    try:
        if password1 and password1 != password2:
            raise ValidationError(_('Password and confirm password does not match.'),
                                  code='invalid')

        password_validation.validate_password(password1)
    except ValidationError as errors:
        return errors


class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect('/admin/')
