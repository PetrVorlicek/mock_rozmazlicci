from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.views import generic
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect

# Create your views here.
import logging

logger = logging.getLogger(__name__)


class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "username", "email", "password"]
        widgets = {"password": forms.PasswordInput()}

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/user/login")
        return render(request, "user_auth.html", {"form": form, "type": "register"})
    else:
        form = RegisterForm()
        return render(request, "user_auth.html", {"form": form, "type": "register"})


def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)

        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        if user is None:
            return render(request, "user_auth.html", {"form": form, "type": "login"})

        login(request, user)

        next = request.GET.get("next", "/user/profile")
        response = HttpResponseRedirect(next)
        response.set_cookie("username", user.username)
        return response

    form = AuthenticationForm()
    return render(request, "user_auth.html", {"form": form, "type": "login"})


@login_required
def profile(request):
    return render(request, "user_profile.html")


@login_required
def user_logout(request):
    logout(request)
    response = HttpResponseRedirect("/")
    response.delete_cookie("username")
    return response
