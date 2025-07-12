from django.contrib import admin
from django.urls import path, include, re_path
from women.views import *

# from rest_framework.routers import DefaultRouter, SimpleRouter

# router = SimpleRouter()
# router.register(r'api/v1/women', WomenViewSet, basename='women')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/drf-auth/', include('rest_framework.urls')),
    path('api/v1/women/', WomenAPIList.as_view(), name='women-list'),
    path('api/v1/women/<int:pk>/', WomenAPIUpdate.as_view(), name='women-update'),
    path('api/v1/women/delete/<int:pk>/', WomenAPIDestroy.as_view(), name='women-delete'),
    # path('api/v1/women/example/', WomenViewSet.as_view({'get': 'example'}), name='women-example'),
    # path('api-token-auth/', CustomAuthToken.as_view(), name='api_token_auth'),
    path('api/v1/auth/', include('djoser.urls')),  # new
    re_path(r'^auth/', include('djoser.urls.authtoken')),  # new
]
