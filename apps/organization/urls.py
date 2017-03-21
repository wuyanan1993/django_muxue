# _*_ coding: utf-8 _*_
from django.conf.urls import url

from organization.views import OrgListView, AddUserAskView, OrganizationView, OrgCourseView, OrgTeacherView

urlpatterns = [
    url(r'^list/$', OrgListView.as_view(), name='org_list'),
    url(r'^ask/$', AddUserAskView.as_view(), name='ask'),
    url(r'^org_home/(?P<org_id>\d*)', OrganizationView.as_view(), name='org_home'),
    url(r'^org_desc/(?P<org_id>\d*)', OrganizationView.as_view(), name='org_desc'),
    url(r'^org_teacher/(?P<org_id>\d*)', OrgTeacherView.as_view(), name='org_teacher'),
    url(r'^org_course/(?P<org_id>\d*)', OrgCourseView.as_view(), name='org_course'),
]
