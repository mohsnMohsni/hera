from django.contrib import admin
from .models import (Product, ProductMeta, Brand, Category,
                     Shop, ShopProduct, Image, Comment, Like)


class ProductMetaAdmin(admin.TabularInline):
    model = ProductMeta
    readonly_fields = ('label', 'value')
    extra = 0


class CommentAdmin(admin.TabularInline):
    model = Comment
    readonly_fields = ('user', 'rate')
    exclude = ('text',)
    extra = 0


class LikeAdmin(admin.TabularInline):
    model = Like
    readonly_fields = ('user', 'condition')
    extra = 0


class ImageAdmin(admin.TabularInline):
    model = Image
    readonly_fields = ('picture',)
    extra = 0


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('brand', 'category', 'name', 'product_picture')
    list_per_page = 10
    list_filter = ('brand',)
    search_fields = ('name', 'detail')
    inlines = [
        ProductMetaAdmin,
        ImageAdmin,
        CommentAdmin,
        LikeAdmin
    ]


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('name', 'logo')
    list_per_page = 10


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'parent', 'category_picture')
    list_per_page = 10
    list_editable = ('parent',)


class ShopProductAdmin(admin.TabularInline):
    model = ShopProduct
    extra = 0


@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'shop_picture')
    list_per_page = 10
    inlines = [ShopProductAdmin]
