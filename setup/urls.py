from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from app.views import FireExtinguishersViewSet, TypeViewSet

router = routers.DefaultRouter()
router.register(r'extinguishers', FireExtinguishersViewSet)
router.register(r'extinguishers/types', TypeViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
