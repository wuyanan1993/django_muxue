# _*_ coding: utf-8 _*_
import simplejson

from django.shortcuts import render
from django.views.generic import View
from django.http.response import HttpResponse

from operation.models import UserFavorite


# Create your views here.0000


class UserFavoriteView(View):
    def post(self, request):
        if request.user.is_authenticated():
            user = request.user.name
            favorite_id = request.POST.get('favorite_id', 0)
            favorite_type = request.POST.get('favorite_type', 0)
            old_record = UserFavorite.objects.get(user=user, favorite_id=int(favorite_id),
                                                  favorite_type=int(favorite_type))
            if old_record:
                data = {
                    'status': 'success',
                    'msg': u'收藏'
                }
                old_record.delete()
                return HttpResponse(simplejson.dumps(data, ensure_ascii=False), content_type='application/json')
            else:
                data = {
                    'status': 'success',
                    'msg': u'已收藏'
                }
                new_record = UserFavorite()
                if int(favorite_id) > 0 and int(favorite_type) > 0:
                    new_record.favorite_id = int(favorite_id)
                    new_record.favorite_type = int(favorite_type)
                    new_record.user = user
                    new_record.save()
                    return HttpResponse(simplejson.dumps(data, ensure_ascii=False), content_type='application/json')
        else:
            data = {
                'status': 'fail',
            }
            return HttpResponse(simplejson.dumps(data, ensure_ascii=False), content_type='application/json')
