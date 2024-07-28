from django.urls import path, include

from django.contrib import admin
from rest_framework.routers import DefaultRouter
from .views import ShowAllProductViewset

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('auth_app.urls')),
    path('category_product/<slug:category_slug>',ShowAllProductViewset.as_view({'get': 'list'}), name='category_wise_product'),
    path('products/',include("cloth_product.urls")),
    path('categories/',include("cloth_category.urls")),
    path('purchases/',include("Purchase.urls")),
    path('transactions/',include("Transactions.urls")),
    # path('accounts/',include("account.urls")),

    
]

urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
