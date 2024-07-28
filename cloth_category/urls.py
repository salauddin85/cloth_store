from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import CategoryApiView
router = DefaultRouter()

router.register('list',CategoryApiView, basename='product')

urlpatterns = [
    path('', include(router.urls)),
]
