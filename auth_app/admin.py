from django.contrib import admin

# Register your models here.
from .import models 
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['first_name','last_name','email','mobaile_no']

    def first_name(self,obj):
        return obj.user.first_name
    def last_name(self,obj):
        return obj.user.last_name
    
    def email(self,obj):
        return obj.user.email
admin.site.register(models.Customer,CustomerAdmin)