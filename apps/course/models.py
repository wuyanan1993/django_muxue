# coding=utf8
from __future__ import unicode_literals
from datetime import datetime

from django.db import models

from organization.models import CourseOrg

# Create your models here.


class Course(models.Model):
    COURSE_DEGREE_CHOICES = (
        ('primary', u'初级'),
        ('middle', u'中级'),
        ('high', u'高级')
    )
    name = models.CharField(max_length=50, verbose_name=u'课程名')
    courser_org = models.ForeignKey(CourseOrg, verbose_name=u'课程机构', null=True, blank=True)
    description = models.CharField(max_length=300, verbose_name=u'课程描述')
    detail = models.TextField(verbose_name=u'课程详情')
    degree = models.CharField(max_length=10, choices=COURSE_DEGREE_CHOICES, verbose_name=u'难度')
    learn_times = models.IntegerField(default=0, verbose_name=u'学习时长')
    students = models.IntegerField(default=0, verbose_name=u'学习人数')
    favorite_numbers = models.IntegerField(default=0, verbose_name=u'收藏人数')
    image = models.ImageField(upload_to='course/%Y/%m', verbose_name=u'封面图片')
    click_numbers = models.IntegerField(default=0, verbose_name=u'点击数')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u'课程'
        verbose_name_plural = verbose_name


class Lesson(models.Model):
    course = models.ForeignKey(Course, verbose_name=u'课程')
    name = models.CharField(max_length=100, verbose_name=u'章节名')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u'章节'
        verbose_name_plural = verbose_name


class Video(models.Model):
    lesson = models.ForeignKey(Course, verbose_name=u'课程')
    name = models.CharField(max_length=100, verbose_name=u'视频名')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'视频'
        verbose_name_plural = verbose_name


class CourseResource(models.Model):
    course = models.ForeignKey(Course, verbose_name=u'课程')
    name = models.CharField(max_length=100, verbose_name=u'资源名称')
    download = models.FileField(upload_to="course/resource/%Y/%m", verbose_name=u'资源文件', max_length=100)
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'资源'
        verbose_name_plural = verbose_name


