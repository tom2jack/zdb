#!/usr/bin/env python
# encoding: utf-8

import xadmin
from .models import InstancesGroup, Instances, Mysqldbs, Mysqlusers, Privileges

class InstancesGroupAdmin(object):
    list_display = ["name", "business", "add_time"]
    list_filter = ["name", ]
    search_fields = ['name', ]

class InstancesAdmin(object):
    list_display = ["name", "group", "role", "server", "port", "memory", "admin_user", "admin_pass", "status",
                    "add_time"]
    list_filter = ["name", "group", "server"]
    search_fields = ["name", "group", "server"]

class MysqldbsAdmin(object):
    list_display = ["name", "status", "desc", "instance", "add_time"]
    list_filter = ["name", "instance"]
    search_fields = ["name", "instance"]

class MysqlusersAdmin(object):
    list_display = ["name", "passwd", "from_ip", "status", "instance", "add_time"]
    list_filter = ["name", "from_ip"]
    search_fields = ["name", "from_ip"]

class PrivilegesAdmin(object):
    list_display = ["user", "instance", "db", "privi"]
    list_filter = ["user", "instance", "db", "privi"]
    search_fields = ["user", "instance", "db", "privi"]

xadmin.site.register(InstancesGroup, InstancesGroupAdmin)
xadmin.site.register(Instances, InstancesAdmin)
xadmin.site.register(Mysqldbs, MysqldbsAdmin)
xadmin.site.register(Mysqlusers, MysqlusersAdmin)
xadmin.site.register(Privileges, PrivilegesAdmin)


