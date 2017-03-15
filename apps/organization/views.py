# _*_ coding: utf-8 *_*
import simplejson

from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse

from organization.models import CourseOrg, CityDict
from organization.forms import UserAskModelForm

from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.


class OrgListView(View):
    def get(self, request):
        try:
            page = int(request.GET.get('page', 1))
        except ValueError:
            page = 1
        city_id = request.GET.get('city', "")
        category_id = request.GET.get('ct', "")
        sort = request.GET.get('sort', "")

        all_org = CourseOrg.objects.all()
        hot_org = all_org.order_by("-click_number")[:3]
        if city_id:
            all_org = all_org.filter(city_id=city_id)
        if category_id:
            all_org = all_org.filter(course_category=category_id)
        if sort:
            if sort == 'join_number':
                all_org = all_org.order_by("-join_number")
            elif sort == 'lesson_number':
                all_org = all_org.order_by("-lesson_number")
            else:
                pass

        all_cities = CityDict.objects.all()
        org_numbers = all_org.count()

        p = Paginator(all_org, 3, request=request)
        organization_in_pages = p.page(page)
        data = {
            'all_org': organization_in_pages,
            'all_cities': all_cities,
            'org_numbers': org_numbers,
            'city_id': city_id,
            'category_id': category_id,
            'hot_org': hot_org,
            'sort': sort
        }
        return render(request, 'org-list.html', data)


class AddUserAskView(View):
    def post(self, request):
        user_ask_form = UserAskModelForm(request.POST)
        if user_ask_form.is_valid():
            user_ask = user_ask_form.save(commit=True)
            data = {
                'status': 'success'
            }
            return HttpResponse(simplejson.dumps(data, ensure_ascii=False), content_type='application/json')
        else:
            data = {
                'status': 'fail',
                'msg': u'添加出错',
            }
            return HttpResponse(simplejson.dumps(data, ensure_ascii=False), content_type='application/json')
