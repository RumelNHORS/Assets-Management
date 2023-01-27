from django.contrib import admin
from . models import AssetsModel, CheckIn, CheckOut

@admin.register(AssetsModel)

class CustomerAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'date', 'asset', 'brand', 'quantity']

@admin.register(CheckIn)
class CheckInAdmin(admin.ModelAdmin):
    list_display = ['id', 'customer_name', 'email', 'asset', 'checkin_date']
    search_fields = ('customer_name', 'phone')
    
@admin.register(CheckOut)
class CheckInAdmin(admin.ModelAdmin):
    list_display = ['id', 'customer_name', 'email', 'asset', 'checkout_date']
    search_fields = ('customer_name', 'phone')