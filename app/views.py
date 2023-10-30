from rest_framework import viewsets

from app.models import FireExtinguisher
from app.models import Type
from app.models import Capacity
from app.models import Agent
from app.models import Location
from app.models import Supplier
from app.models import Manufacture
from app.serializers import ManufactureSerializer
from app.serializers import TypeSerializer
from app.serializers import CapacitySerializer
from app.serializers import AgentSerializer
from app.serializers import LocationSerializer
from app.serializers import SupplierSerializer
from app.serializers import FireExtinguisherSerializer


class FireExtinguishersViewSet(viewsets.ModelViewSet):
    serializer_class = FireExtinguisherSerializer
    queryset = FireExtinguisher.objects.all()


class TypeViewSet(viewsets.ModelViewSet):
    serializer_class = TypeSerializer
    queryset = Type.objects.all()


class CapacityViewSet(viewsets.ModelViewSet):
    serializer_class = CapacitySerializer
    queryset = Capacity.objects.all()


class AgentViewSet(viewsets.ModelViewSet):
    serializer_class = AgentSerializer
    queryset = Agent.objects.all()


class LocationViewSet(viewsets.ModelViewSet):
    serializer_class = LocationSerializer
    queryset = Location.objects.all()


class SupplierViewSet(viewsets.ModelViewSet):
    serializer_class = SupplierSerializer
    queryset = Supplier.objects.all()


class ManufactureViewSet(viewsets.ModelViewSet):
    serializer_class = ManufactureSerializer
    queryset = Manufacture.objects.all()
