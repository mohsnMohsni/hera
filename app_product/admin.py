from django.contrib import admin
from .models import (Product, ProductMeta, Brand, Category, Value,
                     Shop, ShopProduct, Gallery, Comment, Like)
from image_cropping import ImageCroppingMixin


class ProductChoiceMetaAdmin(admin.TabularInline):
    """
    Tabular inline admin for manage Value model, then add to Product Admin
    """
    model = Value
    extra = 0


@admin.register(ProductMeta)
class ProductMetaAdmin(admin.ModelAdmin):
    """
    Tabular inline admin for manage ProductMeta model, then add to Product Admin
    """
    list_display = ('label',)
    inlines = [
        ProductChoiceMetaAdmin
    ]


class CommentAdmin(admin.TabularInline):
    """
    Tabular inline admin for manage Comment model, then add to Product Admin
    """
    model = Comment
    exclude = ('text',)
    extra = 0


class LikeAdmin(admin.TabularInline):
    """
    Tabular inline admin for manage Like model, then add to Product Admin
    """
    model = Like
    extra = 0


class GalleryAdmin(admin.TabularInline):
    """
    Tabular inline admin for manage Gallery model, then add to Product Admin
    """
    model = Gallery
    extra = 0


@admin.register(Product)
class ProductAdmin(ImageCroppingMixin, admin.ModelAdmin):
    """
    Product admin, which to use for mange Product data,
    and inherited from ImageCroppingMixin to add crop image Feature
    """
    list_display = ('brand', 'category', 'name', 'like_count', 'picture')
    prepopulated_fields = {'slug': ('name',)}
    list_per_page = 8
    list_filter = ('brand',)
    search_fields = ('name', 'detail')
    inlines = [
        # ProductMetaAdmin,
        GalleryAdmin,
        CommentAdmin,
        LikeAdmin
    ]


@admin.register(Brand)
class BrandAdmin(ImageCroppingMixin, admin.ModelAdmin):
    """
    Brand admin, which to use for mange Brand data,
    and inherited from ImageCroppingMixin to add crop image Feature
    """
    list_display = ('name', 'picture')
    list_per_page = 8


@admin.register(Category)
class CategoryAdmin(ImageCroppingMixin, admin.ModelAdmin):
    """
    Category admin, which to use for mange Category data,
    and inherited from ImageCroppingMixin to add crop image Feature
    """
    list_display = ('name', 'slug', 'parent', 'picture')
    prepopulated_fields = {'slug': ('name',)}
    list_filter = ('parent',)
    list_per_page = 8
    list_editable = ('parent',)


class ShopProductAdmin(admin.TabularInline):
    """
    Tabular inline admin for manage Shop model, then add to Shop Admin
    """
    model = ShopProduct
    extra = 0


@admin.register(Shop)
class ShopAdmin(ImageCroppingMixin, admin.ModelAdmin):
    """
    Shop admin, which to use for mange Shop data,
    and inherited from ImageCroppingMixin to add crop image Feature
    """
    list_display = ('name', 'slug', 'picture')
    prepopulated_fields = {'slug': ('name',)}
    list_per_page = 8
    inlines = [ShopProductAdmin]
