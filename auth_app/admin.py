from django.contrib import admin
from .models import Account
# # # Register your models here.

class AccountAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'account_no', 'balance', 'created_on']

    def first_name(self, obj):
        return obj.user.first_name

    def last_name(self, obj):
        return obj.user.last_name

    def email(self, obj):
        return obj.user.email

            
admin.site.register(Account, AccountAdmin)

# admin.site.register(Account)