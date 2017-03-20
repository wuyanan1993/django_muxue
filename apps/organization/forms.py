# _*_ coding: utf-8 _*_
import re

from django import forms

from operation.models import UserAsk


class UserAskModelForm(forms.ModelForm):
    class Meta:
        model = UserAsk
        fields = ['name', 'mobile', 'course_name']

    # 自定义手机验证

    def clean_mobile(self):
        mobile = self.cleaned_data['mobile']
        regex_mobile = "^1[358]\d{9}$|^147\d{8}$|^176\d{8}$"
        p = re.compile(regex_mobile)
        if p.match(mobile):
            return mobile
        else:
            raise forms.ValidationError(u"手机号码非法", code="mobile invalid!")
