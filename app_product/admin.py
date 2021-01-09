from django.contrib import admin
from .models import (Product, ProductMeta, Brand, Category,
                     Shop, ShopProduct, Gallery, Comment, Like)
from image_cropping import ImageCroppingMixin


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


class GalleryAdmin(admin.TabularInline):
    model = Gallery
    readonly_fields = ('picture',)
    extra = 0


@admin.register(Product)
class ProductAdmin(ImageCroppingMixin, admin.ModelAdmin):
    list_display = ('brand', 'category', 'name', 'picture')
    list_per_page = 10
    list_filter = ('brand',)
    search_fields = ('name', 'detail')
    inlines = [
        ProductMetaAdmin,
        GalleryAdmin,
        CommentAdmin,
        LikeAdmin
    ]


@admin.register(Brand)
class BrandAdmin(ImageCroppingMixin, admin.ModelAdmin):
    list_display = ('name', 'picture')
    list_per_page = 10


@admin.register(Category)
class CategoryAdmin(ImageCroppingMixin, admin.ModelAdmin):
    list_display = ('name', 'slug', 'parent', 'picture')
    list_per_page = 10
    list_editable = ('parent',)


class ShopProductAdmin(admin.TabularInline):
    model = ShopProduct
    extra = 0


@admin.register(Shop)
class ShopAdmin(ImageCroppingMixin, admin.ModelAdmin):
    list_display = ('name', 'slug', 'picture')
    list_per_page = 10
    inlines = [ShopProductAdmin]
