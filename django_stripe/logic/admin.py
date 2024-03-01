from django.contrib import admin

from .models import Item, Order, Discount, Tax

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'price', 'currency')


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'created_at', 'tax', 'discount')
    fields = ('items',)


@admin.register(Discount)
class DiscountAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'value')


@admin.register(Tax)
class TaxAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'value')
