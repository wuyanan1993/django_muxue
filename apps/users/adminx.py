# _*_ coding: utf-8 _*_
import xadmin
from xadmin import views
from .models import EmailVerifyRecord, Banner, UserProfile


class BaseSetting(object):
    # Theme register
    enable_themes = True
    use_bootswatch = True


class GlobalSettings(object):
    site_title = u'在线教学网'
    site_footer = u'在线教学网'
    menu_style = 'accordion'


class UserProfileAdmin(object):
    pass


class EmailVerifyRecordAdmin(object):
    list_display = (
        'code',
        'email',
        'send_type',
        'send_time',
    )
    search_fields = (
        'code',
        'email',
        'send_type',
    )
    list_filter = (
        'code',
        'email',
        'send_type',
        'send_time',
    )


class BannerAdmin(object):
    list_display = ['title', 'image', 'url', 'index', 'add_time']
    search_fields = ['title', 'image', 'url', 'index']
    list_filter = ['title', 'image', 'url', 'index', 'add_time']

xadmin.site.register(UserProfile, UserProfileAdmin)
xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)
xadmin.site.register(Banner, BannerAdmin)
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)