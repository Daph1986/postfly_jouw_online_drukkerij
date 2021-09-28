from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.db.models import Q
from .models import Product, Category, Size

# Create your views here.

def all_products(request):
	"""View to return all products"""

	products = Product.objects.all()
	query = None
	categories = None
	size = None

	if request.GET:
		if 'category' in request.GET:
			categories =  request.GET['category'].split(',')
			products = products.filter(category__name__in=categories)
			categories = Category.objects.filter(name__in=categories)

		if 'size' in request.GET:
			size = request.GET['size'].split(',')
			products = products.filter(size__in=size)
			size = Size.objects.filter(size__in=size)  

		if 'q' in request.GET:
			query = request.GET['q']
			if not query:
				messages.error(request, "No search criteria has been entered!")
				return redirect(reverse('products'))

			queries = Q(name__icontains=query) | Q(sku__icontains=query)
			products = products.filter(queries)

	context = {
		'products': products,
		'search_term': query,
		'current_categories': categories,
		'current_size': size,
	}

	return render(request, 'products/products.html', context)
