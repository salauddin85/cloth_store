from rest_framework import viewsets
from cloth_product.models import Product
from cloth_product.serialaizers import ProductSerializer
from cloth_category.models import Category
class ShowAllProductViewset(viewsets.ModelViewSet):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer



    def get_queryset(self): 
        queryset = super().get_queryset()
        user_slug = self.request.query_params.get('category_slug')
        if user_slug:
            queryset = queryset.filter(category_id = user_slug)
            
        return  queryset
