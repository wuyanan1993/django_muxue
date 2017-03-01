# coding=utf8
from __future__ import unicode_literals
from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class UserProfile(AbstractUser):
    GENDER_CHOICES = (
        ('male', u'男'),
        ('female', u'女')
    )
    nick_name = models.CharField(max_length=30, verbose_name=u'昵称', default='')
    birthday = models.DateField(verbose_name='birthday', null=True, blank=True)
    gender = models.CharField(max_length=10, verbose_name='gender', choices=GENDER_CHOICES, default="female")
    address = models.CharField(max_length=100, default='', verbose_name='address', null=True, blank=True)
    mobile = models.CharField(max_length=11, verbose_name='Phone', null=True, blank=True)
    image = models.ImageField(upload_to="image/%Y/%m", default="image/default.png")

    class Meta:
        verbose_name = u'用户信息'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.username


class EmailVerifyRecord(models.Model):
    SEND_TYPE_CHOICE = (
        ('register', u'register'),
        ('forget', u'forget')
    )
    code = models.CharField(max_length=20, verbose_name=u'code')
    email = models.EmailField(max_length=50, verbose_name=u'email')
    send_type = models.CharField(max_length=10, choices=SEND_TYPE_CHOICE, default='forget')
    send_time = models.DateTimeField(default=datetime.now)

    def __unicode__(self):
        return '{0}({1})'.format(self.code, self.email)

    class Meta:
        verbose_name = u'Email验证码'
        verbose_name_plural = verbose_name


class Banner(models.Model):
    title = models.CharField(max_length=50, verbose_name=u'标题')
    image = models.ImageField(upload_to='banner/%Y/%m', verbose_name='轮播图')
    url = models.URLField(max_length=100, verbose_name=u'访问地址')
    index = models.SmallIntegerField(default=100, verbose_name=u'图片顺序')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'创建时间')

    class Meta:
        verbose_name = u'轮播图'
        verbose_name_plural = verbose_name
