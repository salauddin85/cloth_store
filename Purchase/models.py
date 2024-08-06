from django.db import models
from django.contrib.auth.models import User 
from auth_app.models import Account
from cloth_product.models import Product
from Transactions.constants import TRANSACTION_TYPE
# Create your models here.
class PurchaseModel(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)


    def __str__(self) -> str:
        return f'{self.user.first_name} {self.user.last_name} product id: {self.product.pk}'