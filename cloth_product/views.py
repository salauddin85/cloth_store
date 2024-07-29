from django.shortcuts import render
from rest_framework import viewsets
from .models import Product,Wishlist,Review
from .serialaizers import WishlistSerializer,ReviewSerializer,ProductSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly

class ProductViewset(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    # print(queryset)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class WishlistViewset(viewsets.ModelViewSet):
    queryset = Wishlist.objects.all()
    serializer_class = WishlistSerializer
    permission_classes = [IsAuthenticated]


    def perform_create(self, serializer):
        user = self.request.user
        if Wishlist.objects.filter(user=user).exists():
            return Response({'error': "A wishlist for this user already exists."}, status=400)
        serializer.save(user=user)



class ReviewViewset(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]