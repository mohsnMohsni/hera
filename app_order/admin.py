from django.contrib import admin
from .models import Cart, CartItem, Order, OrderItem, Payment


class BasketItemAdmin(admin.TabularInline):
    model = CartItem
    extra = 0


@admin.register(Cart)
class BasketAdmin(admin.ModelAdmin):
    list_display = ('user',)
    list_per_page = 10
    inlines = [BasketItemAdmin]


class OrderItemAdmin(admin.TabularInline):
    model = OrderItem
    readonly_fields = ('shop_product', 'count', 'price')
    extra = 0


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('create_at', 'description')
    date_hierarchy = 'create_at'
    list_per_page = 10
    inlines = [OrderItemAdmin]


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('user', 'order', 'amount')
    list_per_page = 10
