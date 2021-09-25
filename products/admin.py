from django.contrib import admin
from .models import Category, Product, PrintingMethod, Size, ProductTag


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
		'category',
        'price'
    )

    ordering = ('sku',)


admin.site.register(Product, ProductAdmin)
admin.site.register(Category)
admin.site.register(PrintingMethod)
admin.site.register(Size)
admin.site.register(ProductTag)
