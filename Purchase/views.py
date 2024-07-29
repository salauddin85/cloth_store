from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from .models import PurchaseModel
from .serialaizers import PurchaseSerializer
from cloth_product.models import Product
from auth_app.models import Account
from rest_framework.permissions import IsAuthenticated

class PurchaseProductView(viewsets.ModelViewSet):
    queryset = PurchaseModel.objects.all()
    serializer_class = PurchaseSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return PurchaseModel.objects.all()

    # @action(detail=False, methods=['post'], url_path='purchase')
    def purchase_product(self, request):
        product_id = request.data.get('product_id')
        
        if not product_id:
            return Response({'error': "No product id found"}, status=status.HTTP_400_BAD_REQUEST)

        # Retrieve the product
        product = get_object_or_404(Product, id=product_id)

        # Retrieve the requested user account
        try:
            requested_user = Account.objects.get(user=self.request.user)
        except Account.DoesNotExist:
            return Response({'error': "No Account Match"}, status=status.HTTP_400_BAD_REQUEST)

        # Perform purchase logic
        if requested_user.balance > product.price and product.quantity > 0:
            requested_user.balance -= product.price
            product.quantity -= 1
            requested_user.save()
            product.save()

            # Create purchase record
            PurchaseModel.objects.create(
                user=self.request.user,
                account=requested_user,
                product=product,
            )
        else:
            return Response({'error': "You Cannot Purchase for your balance and product not sufficient"}, status=status.HTTP_400_BAD_REQUEST)

        return Response({'success': "Purchase completed successfully"}, status=status.HTTP_200_OK)
