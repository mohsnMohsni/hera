from django.contrib import admin
from .models import Cart, CartItem, Order, OrderItem, Payment


class BasketItemAdmin(admin.TabularInline):
    """
    Tabular inline admin for manage BasketItem model, then add to Basket Admin
    """
    model = CartItem
    extra = 0


@admin.register(Cart)
class BasketAdmin(admin.ModelAdmin):
    """
    Basket admin, which to use for mange Basket data
    """
    list_display = ('user',)
    list_per_page = 10
    inlines = [BasketItemAdmin]


class OrderItemAdmin(admin.TabularInline):
    """
    Tabular inline admin for manage OrderItem model, then add to Order Admin
    """
    model = OrderItem
    readonly_fields = ('shop_product', 'count', 'price')
    extra = 0


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    """
    Order admin, which to use for mange Order data
    """
    list_display = ('create_at', 'description')
    date_hierarchy = 'create_at'
    list_per_page = 10
    inlines = [OrderItemAdmin]


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    """
    Payment admin, which to use for mange Payment data
    """
    list_display = ('user', 'order', 'amount')
    list_per_page = 10
