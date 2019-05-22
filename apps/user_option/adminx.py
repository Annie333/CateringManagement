#!/usr/bin/env python
# encoding: utf-8

import xadmin
from .models import UserGoodsFav, LeavingMessage, UserAddress, UserWindowsFav


class UserGoodsFavAdmin(object):
    list_display = ['user', 'goods', "add_time"]
    search_fields = ["goods__name", "user__name"]
    list_filter = ['user__name', 'goods__name', "add_time"]


class UserWindowsFavAdmin(object):
    list_display = ['user', 'windows', "add_time"]
    search_fields = ["windows__name", "user__name"]
    list_filter = ['user__name', 'windows__name', "add_time"]


class UserLeavingMessageAdmin(object):
    list_display = ['user', 'msg_type', "message", "add_time", "windows", "subject"]
    search_fields = ['user__name', 'msg_type', "message", "windows__name", "subject"]
    list_filter = ['user__name', 'msg_type', "message", "windows__name", "subject"]


class UserAddressAdmin(object):
    list_display = ["signer_name", "signer_mobile", "district", "address", "province", "city"]
    search_fields = ["signer_name", "signer_mobile", "district", "address", "province", "city"]
    list_filter = ["signer_name", "signer_mobile", "district", "address", "province", "city"]


xadmin.site.register(UserGoodsFav, UserGoodsFavAdmin)
xadmin.site.register(UserAddress, UserAddressAdmin)
xadmin.site.register(LeavingMessage, UserLeavingMessageAdmin)
xadmin.site.register(UserWindowsFav, UserWindowsFavAdmin)
