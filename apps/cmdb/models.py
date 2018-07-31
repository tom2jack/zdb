#! -*-coding:utf8 -*-
from django.db import models
from datetime import datetime


class Zones(models.Model):
    """
    机房地区
    """
    CITY = (
        (1, "杭州"),
        (2, "北京"),
        (3, "上海"),
    )
    STATUS = (
        (1, "正常"),
        (2, "下线"),
    )
    name = models.CharField(default="", max_length=30, verbose_name="机房名称")
    city = models.IntegerField(choices=CITY, verbose_name="机房地区")
    status = models.SmallIntegerField(choices=STATUS, verbose_name="机房状态")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "机房管理"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Servers(models.Model):
    ip = models.GenericIPAddressField(null=False, verbose_name="主机IP")
    port = models.IntegerField(null=False, verbose_name="主机端口")
    user = models.CharField(max_length=30, null=False, verbose_name="ssh用户")
    user_pass = models.CharField(max_length=30, null=False, verbose_name="ssh密码")
    host_name = models.CharField(max_length=50, null=True, verbose_name="主机名")
    memory = models.IntegerField(verbose_name="主机内存")
    cpu = models.IntegerField(verbose_name="主机CPU")
    raid = models.SmallIntegerField(verbose_name="RAID种类")
    disk = models.IntegerField(verbose_name="磁盘大小")
    zone = models.ForeignKey(Zones)
    status = models.SmallIntegerField(verbose_name="主机状态")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "主机管理"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.ip


class Business(models.Model):
    """
    业务状态
    """
    STATUS = (
        (1, "正常"),
        (2, "下线"),
    )
    name = models.CharField(default="", max_length=30, verbose_name="业务名称")
    status = models.SmallIntegerField(choices=STATUS, verbose_name="业务状态")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "业务线管理"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name





