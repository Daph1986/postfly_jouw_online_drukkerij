from django.contrib import admin
from .models import Category, Product, PrintingMethod, Size, ProductTag


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
		'category',
        'price',
    )

    ordering = ('sku',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )

    ordering = ('friendly_name',)


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(PrintingMethod)
admin.site.register(Size)
admin.site.register(ProductTag)
