#!/usr/bin/env python
# encoding: utf-8

import xadmin
from .models import Staff


class StaffAdmin(object):
    list_display = ['wid', 'name', "birthday", "sex", "mobile", "enter_date"]


xadmin.site.register(Staff, StaffAdmin)
