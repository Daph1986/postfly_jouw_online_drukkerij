from django.shortcuts import get_object_or_404, render, redirect, reverse
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower

from products.forms import ProductForm
from .models import Product, Category, Size

# Create your views here.

def all_products(request):
	"""View to return all products"""

	products = Product.objects.all()
	query = None
	categories = None
	size = None
	sort = None
	direction = None

	if request.GET:
		if 'sort' in request.GET:
			sortkey = request.GET['sort']
			sort = sortkey
			if sortkey == 'name':
				sortkey = 'lower_name'
				products = products.annotate(lower_name=Lower('name'))
			if sortkey == 'category':
				sortkey = 'category__name'
			if 'direction' in request.GET:
				direction = request.GET['direction']
				if direction == 'desc':
					sortkey = f'-{sortkey}'
			products = products.order_by(sortkey)

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

	current_sorting = f'{sort}_{direction}'

	context = {
		'products': products,
		'search_term': query,
		'current_categories': categories,
		'current_size': size,
		'current_sorting': current_sorting,
	}

	return render(request, 'products/products.html', context)


def add_product(request):
	""" For admin use to add a product to the store """
	if request.method == "POST":
		form = ProductForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request, 'Success, the product was added to the store!')
			return redirect(reverse('products'))
		else:
			messages.error(request, 'Sorry, your attempt to add the product failed, please check your form!')
	else:
		form = ProductForm()

	template = 'products/add_product.html'
	context = {
		'form': form,
	}

	return render(request, template, context)


def update_product(request, product_id):
	""" For admin use to update a product in the store """
	product = get_object_or_404(Product, pk=product_id)
	if request.method == 'POST':
		form = ProductForm(request.POST, instance=product)
		if form.is_valid():
			form.save()
			messages.success(request, 'Product has been updated succesfully!')
		else:
			messages.error(request, 'Sorry, your attempt to update the product failed, please check your form!')
	else:
		form = ProductForm(instance=product)
		messages.info(request, f'You are updating {product.sku}')

	template = 'products/update_product.html'
	context = {
        'form': form,
        'product': product,
    }

	return render(request, template, context)


def delete_product(request, product_id):
	""" For admin use to delete a product in the store """
	product = get_object_or_404(Product, pk=product_id)
	product.delete()
	messages.success(request, 'Product has been deleted succesfully!')
	return redirect(reverse('products'))
