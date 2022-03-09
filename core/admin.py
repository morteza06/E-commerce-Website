from django.contrib import admin

from core.models import Item, Order, OrderItem

admin.site.register(Item)
admin.site.register(OrderItem)
admin.site.register(Order)