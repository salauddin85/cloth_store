from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly
from rest_framework import viewsets
# Create your views here.
from .serializers import CategorySerializer
from .models import Category
class CategoryApiView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializers_class = CategorySerializer
    
    