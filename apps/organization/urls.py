# _*_ coding: utf-8 _*_
from django.conf.urls import url

from organization.views import OrgListView, AddUserAskView, OrganizationView

urlpatterns = [
    url(r'^list/$', OrgListView.as_view(), name='org_list'),
    url(r'^ask/$', AddUserAskView.as_view(), name='ask'),
    url(r'^org_home/(?P<org_id>\d*)', OrganizationView.as_view(), name='org_home')
]
