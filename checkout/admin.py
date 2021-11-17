from django.contrib import admin
from .models import Order, OrderLineItem


class OrderLineItemAdminInline(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdminInline,)

    readonly_fields = ('order_number', 'date',
                       'order_total', 'tax', 'grand_total',
                       'original_cart', 'stripe_pid', 'artwork')

    fields = ('order_number', 'user_profile', 'date',
              'first_name', 'last_name', 'company_name',
              'email', 'phone_number', 'country',
              'postcode', 'town_or_city', 'street_address1',
              'street_address2',
              'order_total', 'tax', 'grand_total',
              'original_cart', 'stripe_pid', 'artwork')

    list_display = ('order_number', 'date', 'first_name',
                                    'last_name', 'company_name',
                    'order_total', 'tax',
                    'grand_total',)

    ordering = ('-date',)


admin.site.register(Order, OrderAdmin)
