from django.urls import path, include

from app.urls import router
from app.views import CustomAuthToken

urlpatterns = [
    path('', include(router.urls)),
    path(r'api-token-auth', CustomAuthToken.as_view())
]
