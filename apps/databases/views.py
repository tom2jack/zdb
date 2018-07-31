from django.shortcuts import render
from rest_framework import viewsets

from .models import InstancesGroup, Instances, Mysqldbs, Mysqlusers, Privileges
from .serializers import InstancesGroupSerializer, InstancesSerializer, MysqldbsSerializer, MysqlusersSerializer, \
    PrivilegesSerializer

class InstancesGroupViewSet(viewsets.ModelViewSet):
    """
    list mysql instance group
    """
    queryset = InstancesGroup.objects.all()
    serializer_class = InstancesGroupSerializer

class InstancesViewSet(viewsets.ModelViewSet):
    """
    list mysql instance
    """
    queryset = Instances.objects.all()
    serializer_class = InstancesSerializer

class MysqldbsViewSet(viewsets.ModelViewSet):
    """
    list mysql databases
    """
    queryset = Mysqldbs.objects.all()
    serializer_class = MysqldbsSerializer

class MysqlusersViewSet(viewsets.ModelViewSet):
    """
    list mysql users
    """
    queryset = Mysqlusers.objects.all()
    serializer_class = MysqlusersSerializer

class PrivilegesViewSet(viewsets.ModelViewSet):
    """
    list mysql users
    """
    queryset = Privileges.objects.all()
    serializer_class = PrivilegesSerializer
