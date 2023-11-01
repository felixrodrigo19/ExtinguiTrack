from django.urls import path, include

from app.urls import router

urlpatterns = [
    path('', include(router.urls)),
]
