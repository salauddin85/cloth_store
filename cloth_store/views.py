from rest_framework import viewsets
from cloth_product.models import Product
from cloth_product.serialaizers import ProductSerializer
from cloth_category.models import Category
class ShowAllProductViewset(viewsets.ModelViewSet):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer



    def get_queryset(self): 
        queryset = super().get_queryset()
        user_slug = self.kwargs.get('category_slug')
        if user_slug:
            category = Category.objects.get(slug = user_slug)
            return Product.objects.filter(category = category)
        return  queryset
