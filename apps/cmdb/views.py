# -*- coding: utf-8 -*-
from rest_framework.response import Response
from rest_framework import mixins
from rest_framework import filters
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.throttling import UserRateThrottle

from rest_framework_extensions.cache.mixins import CacheResponseMixin

from .models import Zones, Servers, Business
from .serializers import ZonesSerializer, ServersSerializer, BusinessSerializer


class ZonesViewSet(viewsets.ModelViewSet):
    """
    list zones
    """
    queryset = Zones.objects.all()
    serializer_class = ZonesSerializer

class ServersViewSet(viewsets.ModelViewSet):
    """
    list servers
    """
    queryset = Servers.objects.all()
    serializer_class = ServersSerializer

class BusinessViewSet(viewsets.ModelViewSet):
    """
    list business
    """
    queryset = Business.objects.all()
    serializer_class = BusinessSerializer
