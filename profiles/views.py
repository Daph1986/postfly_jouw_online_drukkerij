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


def dashboard(request):
	""" A view that displays the dashboad for the customer """
	profile = get_object_or_404(UserProfile, user=request.user)
	orders = profile.orders.all().order_by('-date')
	paginator = Paginator(orders, 6)
	page_number = request.GET.get('page')
	page_object = paginator.get_page(page_number)
	total_orders = orders.count()

	template = 'profiles/dashboard.html'
	context = {
        'orders': orders,
		'page_object': page_object,
        'total_orders': total_orders,
        'on_profile_page': True
    }

	return render(request, template, context)


def order_detail(request, order_number):
	""" Displays the order details of a specific order """
	order = get_object_or_404(Order, order_number=order_number)
	
	template = 'checkout/checkout_success.html'
	context = {
        'order': order,
        'from_profile': True,
    }

	return render(request, template, context)
