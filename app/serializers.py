from rest_framework import serializers

from app.models import Manufacture
from app.models import Supplier
from app.models import Location
from app.models import Agent
from app.models import Capacity
from app.models import Type
from app.models import FireExtinguisher


class ManufactureSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Manufacture
        fields = '__all__'


class SupplierSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Supplier
        fields = '__all__'


class LocationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'


class AgentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Agent
        fields = '__all__'


class CapacitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Capacity
        fields = '__all__'


class TypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Type
        fields = '__all__'


class FireExtinguisherSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = FireExtinguisher
        fields = '__all__'
