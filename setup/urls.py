from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from app.views import FireExtinguishersViewSet, TypeViewSet

router = routers.DefaultRouter()
router.registry(r'extinguishers', FireExtinguishersViewSet)
router.registry(r'extinguishers/types', TypeViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
