#!/usr/bin/env python
# encoding: utf-8

import xadmin
from xadmin import views
from .models import VerifyCode, Staff, UserProfile
from xadmin.plugins.auth import UserAdmin


class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


class GlobalSettings(object):
    site_title = "食堂管理系统后台"
    site_footer = "cateringmanagement"
    # menu_style = "accordion"


class VerifyCodeAdmin(object):
    list_display = ['code', 'mobile', "add_time"]  # list_display 属性包含需要展示在页面的相关字段


class StaffAdmin(object):
    list_display = ['windows', 'user']
    list_filter = ['windows__name']
    search_fields = ['windows__name']


xadmin.site.register(VerifyCode, VerifyCodeAdmin)
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)
xadmin.site.register(Staff, StaffAdmin)
