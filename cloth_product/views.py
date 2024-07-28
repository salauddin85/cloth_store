from django.shortcuts import render
from rest_framework import viewsets
from .models import Product,Wishlist,Review
from .serialaizers import WishlistSerializer,ReviewSerializer,ProductSerializer


class ProductViewset(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # print(queryset)

class WishlistViewset(viewsets.ModelViewSet):
    queryset = Wishlist.objects.all()
    serializer_class = WishlistSerializer


class ReviewViewset(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer