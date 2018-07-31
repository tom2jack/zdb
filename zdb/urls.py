from django.conf.urls import url, include
import xadmin
from rest_framework.documentation import include_docs_urls
from rest_framework.routers import DefaultRouter

from cmdb.views import ZonesViewSet, ServersViewSet, BusinessViewSet
from databases.views import InstancesGroupViewSet, InstancesViewSet, MysqldbsViewSet, MysqlusersViewSet, PrivilegesViewSet

router = DefaultRouter()
router.register(r'zones', ZonesViewSet, base_name='zones')
router.register(r'servers', ServersViewSet, base_name='servers')
router.register(r'business', BusinessViewSet, base_name='business')
router.register(r'instancegroups', InstancesGroupViewSet, base_name='instancegroups')
router.register(r'instances', InstancesViewSet, base_name='instances')
router.register(r'mysqldbs', MysqldbsViewSet, base_name='mysqldbs')
router.register(r'mysqlusers', MysqlusersViewSet, base_name='mysqlusers')
router.register(r'privileges', PrivilegesViewSet, base_name='privileges')



urlpatterns = [
    url(r'^xadmin/', xadmin.site.urls),
    url(r'^', include(router.urls)),
    url(r'docs/', include_docs_urls(title="zdb")),
]
