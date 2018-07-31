# -*- coding: utf-8 -*-
from rest_framework import serializers

from .models import InstancesGroup, Instances, Mysqldbs, Mysqlusers, Privileges

class InstancesGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = InstancesGroup
        fields = "__all__"

class InstancesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instances
        fields = "__all__"

class MysqldbsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mysqldbs
        fields = "__all__"

class MysqlusersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mysqlusers
        fields = "__all__"

class PrivilegesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Privileges
        fields = "__all__"

