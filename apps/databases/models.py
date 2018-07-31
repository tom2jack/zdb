# -*- coding: utf-8 -*-
from django.db import models
from datetime import datetime

from cmdb.models import Servers, Business

class InstancesGroup(models.Model):
    name = models.CharField(default="", max_length=30, verbose_name="实例组名称")
    business = models.ForeignKey(Business, default=5)
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "实例组管理"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Instances(models.Model):
    ROLE = (
        (1, "master"),
        (2, "slave"),
        (3, "standby slave"),
    )
    name = models.CharField(default="", max_length=30, verbose_name="实例名称")
    group = models.ForeignKey(InstancesGroup)
    role = models.SmallIntegerField(choices=ROLE, verbose_name="实例角色")
    server = models.ForeignKey(Servers)
    port = models.IntegerField(null=False, verbose_name="实例端口")
    memory = models.IntegerField(verbose_name="实例内存")
    admin_user = models.CharField(default="", max_length=30, verbose_name="管理用户")
    admin_pass = models.CharField(default="", max_length=30, verbose_name="管理密码")
    status = models.SmallIntegerField(verbose_name="实例状态")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "实例管理"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Mysqldbs(models.Model):
    name = models.CharField(default="", max_length=30, verbose_name="库名")
    status = models.SmallIntegerField(verbose_name="状态")
    desc = models.TextField(verbose_name="业务用途")
    instance = models.ForeignKey(Instances)
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "业务库管理"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

class Mysqlusers(models.Model):
    name = models.CharField(default="", max_length=30, verbose_name="用户名")
    passwd = models.CharField(max_length=30, verbose_name="密码")
    from_ip = models.GenericIPAddressField(default='0.0.0.0', verbose_name="来源IP")
    status = models.SmallIntegerField(verbose_name="用户状态")
    instance = models.ForeignKey(Instances)
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "用户管理"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Privileges(models.Model):
    PRIVI = (
        (1, "读写"),
        (2, "只读"),
    )
    user = models.ForeignKey(Mysqlusers)
    instance = models.ForeignKey(Instances, null=True)
    db = models.ForeignKey(Mysqldbs)
    privi = models.SmallIntegerField(choices=PRIVI, default=1, verbose_name="读写权限")

    class Meta:
        unique_together = ('user', 'instance', 'db')
        verbose_name = "权限管理"
        verbose_name_plural = verbose_name


