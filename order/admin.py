import datetime

from django.urls import reverse

from django.contrib import admin
from .models import Order, OrderItem 

# Register your models here.

def order_name(obj):
    return '%s %s' % (obj.first_name, obj.last_name)
order_name.short_description = 'Name'

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']

def admin_order_shipped(modelAdmin, request, queryset):
    for order in queryset:
        order.shipped_date = datetime.datetime.now()
        order.status = Order.SHIPPED
        order.save()
    return

def admin_order_arrived(modelAdmin, request, queryset):
    for order in queryset:
        order.shipped_date = datetime.datetime.now()
        order.status = Order.ARRIVED
        order.save()
    return

admin_order_shipped.short_description = 'Set shipped'
admin_order_arrived.short_description = 'Set arrived'

class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', order_name, 'status', 'created_at']
    list_filter = ['created_at', 'status']
    search_fields = ['first_name', 'address']
    inlines = [OrderItemInline]
    actions = [admin_order_shipped, admin_order_arrived]


admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem)