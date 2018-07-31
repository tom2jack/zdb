# -*- coding: utf-8 -*-
from rest_framework import serializers

from .models import Zones, Servers, Business


class ZonesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Zones
        fields = "__all__"


class ServersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Servers
        fields = "__all__"

class BusinessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Business
        fields = "__all__"



