from django import forms
from django.contrib import admin
from .models import Product
from .constraints import SIZE
class ProductAdminForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        widgets = {
            'size': forms.CheckboxSelectMultiple(choices=SIZE),
        }

class ProductAdmin(admin.ModelAdmin):
    form = ProductAdminForm

admin.site.register(Product, ProductAdmin)

# admin.site.register(Product)