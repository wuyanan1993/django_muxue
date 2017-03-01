# _*_ coding: utf-8 _*_

import xadmin
from .models import CityDict, CourseOrg, Teacher


class CityDictAdmin(object):
    list_display = ['name', 'description', 'add_time']
    search_fields = ['name', 'description']
    list_filter = ['name', 'description', 'add_time']


class CourseOrgAdmin(object):
    list_display = ['name', 'description', 'click_number', 'favorite_number', 'image', 'address', 'city', 'add_time']
    search_fields = ['name', 'description', 'click_number', 'favorite_number', 'image', 'address', 'city']
    list_filter = ['name', 'description', 'click_number', 'favorite_number', 'image', 'address', 'city', 'add_time']


class TeacherAdmin(object):
    list_display = ['organization', 'name', 'work_years', 'work_company', 'work_position', 'points', 'click_number', 'favorite_number', 'add_time']
    search_fields = ['organization', 'name', 'work_years', 'work_company', 'work_position', 'points', 'click_number', 'favorite_number']
    list_filter = ['organization', 'name', 'work_years', 'work_company', 'work_position', 'points', 'click_number', 'favorite_number', 'add_time']

xadmin.site.register(CityDict, CityDictAdmin)
xadmin.site.register(Teacher, TeacherAdmin)
xadmin.site.register(CourseOrg, CourseOrgAdmin)