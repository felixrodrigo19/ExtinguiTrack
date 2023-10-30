from django.http import JsonResponse
from rest_framework import viewsets

from app.models import FireExtinguisher, Type
from app.serializers import ManufactureSerializer, TypeSerializer


class FireExtinguishersViewSet(viewsets.ModelViewSet):
    serializer_class = ManufactureSerializer
    queryset = FireExtinguisher.objects.all()


class TypeViewSet(viewsets.ModelViewSet):
    serializer_class = TypeSerializer
    queryset = Type.objects.all()
