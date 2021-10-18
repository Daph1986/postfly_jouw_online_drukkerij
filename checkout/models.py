from django.db import models
from django.db.models import Sum
from django.conf import settings

import datetime

from products.models import Product

def generate_order_number():
    """ Creates a custom order number that starts at 8000. """
    last_order = Order.objects.all().order_by('order_number').last()
    current_year = str(datetime.date.today().strftime('%y'))

    if not last_order:
        return 'AMB' + current_year + '-8000'
    elif str(last_order.order_number[3:7]) != current_year:
        return 'AMB' + current_year + '-8000'

    current_order = int(last_order.order_number[9:13])
    next_order = current_order + 1
    new_order_number = 'AMB' + current_year + str(next_order).zfill(4)

    return new_order_number


class Order(models.Model):
	order_number = models.CharField(max_length=10, 
                                    null=False, editable=False)
	first_name = models.CharField(max_length=40, null=False, blank=False)
	last_name = models.CharField(max_length=40, 
                                 null=False, blank=False, default=None)
	company_name = models.CharField(max_length=50, null=True, blank=True)
	email = models.EmailField(max_length=254, null=False, blank=False)
	phone_number = models.CharField(max_length=20, null=False, blank=False)
	country = models.CharField(max_length=40, null=False, blank=False)
	postcode = models.CharField(max_length=20, null=True, blank=True)
	town_or_city = models.CharField(max_length=40, null=False, blank=False)
	street_address1 = models.CharField(max_length=80, null=False, blank=False)
	street_address2 = models.CharField(max_length=80, null=True, blank=True)
	date = models.DateTimeField(auto_now_add=True)
	order_total = models.DecimalField(max_digits=10, decimal_places=2, 
                                      null=False, default=0)
	tax = models.DecimalField(max_digits=10, decimal_places=2, 
                              null=False, default=0)
	grand_total = models.DecimalField(max_digits=10, decimal_places=2, 
                                      null=False, default=0)

	def update_total(self):
		""" Update grand total when new product is added. """

		self.order_total = self.lineitems.aggregate(Sum('lineitem_total'))[
			'lineitem_total__sum']
		self.grand_total = self.order_total + self.tax
		self.save()

	def save(self, *args, **kwargs):
		""" Override the save method to set the order number """
		if not self.order_number:
			self.order_number = self._generate_order_number()
		super().save(*args, **kwargs)

	def __str__(self):
		return self.order_number


class OrderLineItem(models.Model):
    order = models.ForeignKey(Order, null=False, blank=False,
                              on_delete=models.CASCADE, 
                              related_name='lineitems')
    product = models.ForeignKey(Product, null=False, blank=False, 
    							on_delete=models.CASCADE)
    quantity = models.IntegerField(null=False, blank=False, default=0)
    lineitem_total = models.DecimalField(max_digits=6, decimal_places=2, 
                                         null=False, blank=False, 
                                         editable=False)

    def save(self, *args, **kwargs):
        """ Overrides the original save method for the lineitem total and update order total. """

        self.lineitem_total = self.product.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f'SKU {self.product.sku} on order {self.order.order_number}'