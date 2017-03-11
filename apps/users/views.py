# _*_ encoding:utf-8 _*_
from django.shortcuts import render
from django.http.response import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from django.views.generic.base import View
from .forms import LoginForm

from .models import UserProfile

# Create your views here.


class CustomBackend(ModelBackend):
    def authenticate(self, username=None, password=None, **kwargs):
        try:
            user = UserProfile.objects.get(Q(username=username)|Q(email=username))
            if user.check_password(password):
                return user
        except Exception as e:
            return None


class LoginView(View):
    def get(self, request):
        data = {

        }
        return render(request, "login.html", data)

    def post(self, request):
        login_form = LoginForm(request.POST)
        username = request.POST.get("username", "")
        password = request.POST.get('password', "")
        if login_form.is_valid():
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                data = {

                }
                return render(request, "index.html", data)
            else:
                data = {
                    "msg": u'用户名或密码错误',
                    "username": username,
                    "password": password,
                }
                return render(request, "login.html", data)
        else:
            data = {
                "username": username,
                "password": password,
                "login_form": login_form
            }
            return render(request, "login.html", data)
