from rest_framework import routers

from app.views import FireExtinguishersViewSet
from app.views import TypeViewSet
from app.views import LocationViewSet
from app.views import SupplierViewSet
from app.views import ManufactureViewSet
from app.views import AgentViewSet
from app.views import CapacityViewSet

router = routers.DefaultRouter()
router.register(r'extinguishers', FireExtinguishersViewSet)
router.register(r'types', TypeViewSet)
router.register(r'location', LocationViewSet)
router.register(r'manufacture', ManufactureViewSet)
router.register(r'agents', AgentViewSet)
router.register(r'capacity', CapacityViewSet)
router.register(r'suppliers', SupplierViewSet)
