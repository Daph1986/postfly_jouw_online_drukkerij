from django.shortcuts import get_object_or_404
from django.conf import settings

from products.models import Product
from decimal import Decimal

def cart_contents(request):

	cart_items = []
	total = 0
	tax = 0
	product_count = 0
	cart = request.session.get('cart', {})

	for product_id, quantity in cart.items():
		product = get_object_or_404(Product, pk=product_id)
		total += quantity * product.price
		tax = total * Decimal(settings.TAX_PERCENTAGE / 100)
		product_count += quantity
		cart_items.append({
			'product_id': product_id,
			'quantity': quantity,
			'product': product,
		})

	grand_total = total + tax

	context = {
		'cart_items': cart_items,
    'total': total,
		'tax': tax,
		'grand_total': grand_total,
    'product_count': product_count,
	}

	return context
