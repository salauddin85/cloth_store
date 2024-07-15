from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from rest_framework import serializers
class Customer(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    account_no = models.CharField(max_length=20,null=True,blank=True)
    balance = models.DecimalField(decimal_places=2,max_digits=10,null=True,blank=True)
    mobaile_no = models.CharField(max_length=11)


    def __str__(self) :
        return f"{self.user.first_name} {self.user.last_name}"

