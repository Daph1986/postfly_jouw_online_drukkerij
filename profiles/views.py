from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

from .models import UserProfile
from .forms import UserProfileForm

from checkout.models import Order


@login_required
def profile(request):
	""" Displays the user's profile """
	profile = get_object_or_404(UserProfile, user=request.user)

	if request.method == 'POST':
		form = UserProfileForm(request.POST, instance=profile)
		if form.is_valid():
			form.save()
			messages.success(request, 'Your profile is updated successfully')
		else:
			messages.error(request, 'Sorry, failed to update your profile, please check the form!')
	else:
		form = UserProfileForm(instance=profile)

	template = 'profiles/profile.html'
	context = {
		'form': form,
	}

	return render(request, template, context)


@login_required
def dashboard(request):
	""" A view that displays the dashboad for the customer """
	profile = get_object_or_404(UserProfile, user=request.user)
	order_list = profile.orders.all().order_by('-date')
	order_list_admin = Order.objects.all().order_by('-date')
	paginator = Paginator(order_list, 10)
	paginator_admin = Paginator(order_list_admin, 10)
	page_number = request.GET.get('page')
	page_object = paginator.get_page(page_number)
	page_object_admin = paginator_admin.get_page(page_number)
	total_orders = order_list.count()
	total_orders_admin = order_list_admin.count()

	template = 'profiles/dashboard.html'
	context = {
        'order_list': order_list,
		'order_list_admin': order_list_admin,
		'page_object': page_object,
		'page_object_admin': page_object_admin,
		'total_orders': total_orders,
		'total_orders_admin': total_orders_admin,
		'on_profile_page': True
    }

	return render(request, template, context)


@login_required
def order_detail(request, order_number):
	""" Displays the order details of a specific order """
	order = get_object_or_404(Order, order_number=order_number)
	
	template = 'checkout/checkout_success.html'
	context = {
        'order': order,
        'from_profile': True,
    }

	return render(request, template, context)
