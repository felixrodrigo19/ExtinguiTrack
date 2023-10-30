from django.urls import path, include
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
router.register(r'extinguishers/types', TypeViewSet)
router.register(r'extinguishers/location', LocationViewSet)
router.register(r'extinguishers/manufacture', ManufactureViewSet)
router.register(r'extinguishers/agents', AgentViewSet)
router.register(r'extinguishers/capacity', CapacityViewSet)
router.register(r'suppliers', SupplierViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
