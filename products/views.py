from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.db.models import Q
from .models import Product

# Create your views here.

def all_products(request):
	"""View to return all products"""

	products = Product.objects.all()
	query = None

	if request.GET:
		if 'q' in request.GET:
			query = request.GET['q']
			if not query:
				messages.error(request, "No search criteria has been entered!")
				return redirect(reverse('products'))

			queries = Q(name__icontains=query) | Q(sku__icontains=query)
			products = products.filter(queries)

	context = {
		'products': products,
		'search_term': query
	}

	return render(request, 'products/products.html', context)
