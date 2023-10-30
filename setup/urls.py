from django.contrib import admin
from django.urls import path

from app.views import fire_extinguishers

urlpatterns = [
    path('admin/', admin.site.urls),
    path('extinguishers/', fire_extinguishers),
]
