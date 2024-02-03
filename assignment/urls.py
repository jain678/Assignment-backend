from django.contrib import admin
from django.urls import path,include
# from .api 
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('authenticate/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('authenticate/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/',include('api.urls')),
]
