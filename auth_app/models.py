from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Account(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    account_no = models.IntegerField(unique=True,auto_created=True) 
    balance = models.DecimalField(decimal_places=2,max_digits=10,default=0)   
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self) :
        return f"{self.user.first_name} {self.user.last_name}  {self.account_no} "

    # def save(self, *args, **kwargs):
    #     if not self.account_no:
    #         self.account_no = Account.objects.count() + 1  # simplistic auto account number
    #     super().save(*args, **kwargs)