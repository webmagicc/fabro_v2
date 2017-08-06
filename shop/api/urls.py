from rest_framework.routers import DefaultRouter
from django.conf.urls import url, include
from .views import *

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'brands', CategoryViewSet)
router.register(r'products', ProductViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]