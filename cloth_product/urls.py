from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import ProductViewset,WishlistViewset,ReviewViewset

router = DefaultRouter()
router.register('product', ProductViewset,basename='product')
router.register('wishlist', WishlistViewset, basename='wishlist')
router.register('review', ReviewViewset, basename='review')


urlpatterns = [
    path('', include(router.urls)),
]
