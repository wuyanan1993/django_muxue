# _*_ encoding:utf-8 _*_
from django.shortcuts import render
from django.http.response import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.hashers import make_password
from django.db.models import Q
from django.views.generic.base import View
from utils.email_send import send_register_email

from .models import UserProfile, EmailVerifyRecord
from .forms import LoginForm, RegisterForm, ForgetPwdForm

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
                if user.is_active:
                    login(request, user)
                    return render(request, "index.html",)
                else:
                    data = {
                        'msg': u'用户未激活'
                    }
                    return render(request, "login.html", data)
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


class RegisterView(View):
    def get(self, request):
        register_form = RegisterForm()
        data = {
            'register_form': register_form
        }
        return render(request, "register.html", data)

    def post(self, request):
        register_form = RegisterForm(request.POST)
        username = request.POST.get('email', '')
        password = request.POST.get('password', '')
        if register_form.is_valid():
            if UserProfile.objects.get(email=username):
                data = {
                    'msg': u'该邮箱已经注册',
                    'register_form': register_form,
                }
                return render(request, 'register.html', data)
            user_profile = UserProfile()
            user_profile.email = username
            user_profile.password = make_password(password)
            user_profile.save()
            send_register_email(username, "register")
            return render(request, 'login.html')
        else:
            data = {
                'register_form': register_form,
            }
            return render(request, 'register.html', data)


class ActiveUserView(View):
    def get(self, request, active_code):
        records = EmailVerifyRecord.objects.filter(code=active_code)
        if records:
            for record in records:
                email = record.email
                user = UserProfile.objects.get(email=email)
                user.is_active = True
                user.save()
            return render(request, 'login.html', )
        else:
            return render(request, 'active_fail.html', )


class ForgetPwdView(View):
    def get(self, request):
        forget_pwd_form = ForgetPwdForm()
        data = {
            'forget_pwd_form': forget_pwd_form
        }
        return render(request, 'forgetpwd.html', data)

    def post(self, request):
        forget_pwd_form = ForgetPwdForm(request.POST)
        if forget_pwd_form.is_valid():
            email = request.POST.get('email', '')
            send_register_email(email, "forget")
            return render(request, 'send_email_success.html')
        else:
            data = {
                'forget_pwd_form': forget_pwd_form
            }
            return render(request, 'forgetpwd.html', data)