# _*_ coding: utf-8 _*_

from django import forms
from captcha.fields import CaptchaField


class LoginForm(forms.Form):
    username = forms.CharField(required=True, min_length=6)
    password = forms.CharField(required=True, min_length=6)


class RegisterForm(forms.Form):
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True, min_length=8)
    captcha = CaptchaField(error_messages={'invalid': u'验证码出错'})


class ForgetPwdForm(forms.Form):
    email = forms.EmailField(required=True)
    captcha = CaptchaField(error_messages={'invalid': u'验证码出错'})


class ModifyPwdForm(forms.Form):
    email = forms.EmailField(required=True)
    password1 = forms.CharField(required=True, min_length=8)
    password2 = forms.CharField(required=True, min_length=8)
