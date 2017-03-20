# coding=utf8
from __future__ import unicode_literals
from datetime import datetime

from django.db import models

# Create your models here.


class CityDict(models.Model):
    name = models.CharField(max_length=20, verbose_name=u'城市')
    description = models.CharField(max_length=200, verbose_name=u'描述')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'时间')

    class Meta:
        verbose_name = u'城市'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name


class CourseOrg(models.Model):
    COURSE_CATEGORY = (
        ('edu_org', u'培训机构'),
        ('teacher', u'高校'),
        ('other', u'个人')
    )
    name = models.CharField(max_length=50, verbose_name=u'机构名称')
    description = models.TextField(verbose_name=u'描述')
    course_category = models.CharField(default='edu_org', choices=COURSE_CATEGORY, max_length=20, verbose_name=u'机构类别')
    click_number = models.IntegerField(default=0, verbose_name=u'点击次数')
    favorite_number = models.IntegerField(default=0, verbose_name=u'收藏数')
    image = models.ImageField(upload_to='org/%Y/%m', verbose_name=u'机构头像')
    address = models.CharField(max_length=150, verbose_name=u'机构地址')
    city = models.ForeignKey(CityDict, verbose_name=u'城市')
    join_number = models.IntegerField(default=0, verbose_name=u'学习人数')
    lesson_number = models.IntegerField(default=0, verbose_name=u'课程数')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'时间')

    class Meta:
        verbose_name = u'课程机构'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name


class Teacher(models.Model):
    organization = models.ForeignKey(CourseOrg, verbose_name=u'所属机构')
    name = models.CharField(max_length=50, verbose_name=u'教师名称')
    work_years = models.IntegerField(default=0, verbose_name=u'工作年限')
    work_company = models.CharField(max_length=50, verbose_name=u'就职公司')
    work_position = models.CharField(max_length=50, verbose_name=u'公司职位')
    points = models.CharField(max_length=50, verbose_name=u'教学特点')
    click_number = models.IntegerField(default=0, verbose_name=u'点击次数')
    favorite_number = models.IntegerField(default=0, verbose_name=u'收藏数')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'时间')
    image = models.ImageField(default='', upload_to='org/%Y/%m', verbose_name=u'讲师头像')

    class Meta:
        verbose_name = u'老师'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name
