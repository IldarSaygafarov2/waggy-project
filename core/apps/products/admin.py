from django.contrib import admin

from .models import Product, ProductTag, ProductBrand, ProductImage


@admin.register(ProductTag)
class ProductTagAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'created_at']
    list_display_links = ['id', 'name']


@admin.register(ProductBrand)
class ProductBrandAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'created_at']
    list_display_links = ['id', 'name']


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'slug', 'price', 'brand']
    list_editable = ['price', 'brand']
    prepopulated_fields = {"slug": ("name",)}
    list_filter = ['brand', 'created_at']
    search_fields = ['name']
    inlines = [
        ProductImageInline
    ]
