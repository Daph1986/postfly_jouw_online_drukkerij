from django.http import request
from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.views.generic import View

from .forms import OrderForm
from .models import Order, OrderLineItem
from products.models import Product
from profiles.forms import UserProfileForm
from profiles.models import UserProfile
from cart.contexts import cart_contents

import stripe
import json

@require_POST
def cache_checkout_data(request):
    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(pid, metadata={
            'cart': json.dumps(request.session.get('cart', {})),
            'save_info': request.POST.get('save_info'),
            'username': request.user,
        })
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, 'Our apologies, your payment cannot be \
            processed at the moment. Please try again later.')
        return HttpResponse(content=e, status=400)


class CheckoutView(View):

    def __init__(self, request):
        self.request = request

    def _send_confirmation_email(self, order):
        """ Sends the user a confirmation email """
        client_email = order.email
        subject = render_to_string(
			'checkout/confirmation_emails/confirmation_email_subject.txt',
			{'order': order})
        body = render_to_string(
			'checkout/confirmation_emails/confirmation_email_body.txt',
			{'order': order, 'contact_email': settings.DEFAULT_FROM_EMAIL})

        send_mail(
            subject,
            body,
            settings.DEFAULT_FROM_EMAIL,
            [client_email]
        )

    def checkout(self, request):
        stripe_public_key = settings.STRIPE_PUBLIC_KEY
        stripe_secret_key = settings.STRIPE_SECRET_KEY

        if request.method == 'POST':
            cart = request.session.get('cart', {})
        
            form_data = {
                'first_name': request.POST['first_name'],
                'last_name': request.POST['last_name'],
                'email': request.POST['email'],
                'company_name': request.POST['company_name'],
                'street_address1': request.POST['street_address1'],
                'street_address2': request.POST['street_address2'],
                'postcode': request.POST['postcode'],
                'town_or_city': request.POST['town_or_city'],
                'country': request.POST['country'],
                'phone_number': request.POST['phone_number'],
            }
            order_form = OrderForm(form_data)
            if order_form.is_valid():
                order = order_form.save(commit=False)
                pid = request.POST.get('client_secret').split('_secret')[0]
                order.stripe_pid = pid
                order.original_cart = json.dumps(cart)
                order.save()
                for product_id, quantity in cart.items():
                    try:
                        product = Product.objects.get(id=product_id)
                        if isinstance(quantity, int):
                            order_line_item = OrderLineItem(
                                order=order,
                                product=product,
                                quantity=quantity,
                            )
                            order_line_item.save()
                    except Product.DoesNotExist:
                        messages.error(request, (
                            "One of the products in your cart hasn't been found in our database."
                            "Please contact us for assistance!")
                        )
                        order.delete()
                        return redirect(reverse('view_cart'))

                self._send_confirmation_email(order)
                request.session['save_info'] = 'save_info' in request.POST
                return redirect(reverse('checkout_success', args=[order.order_number]))
            else:
                messages.error(request, 'There was an error with your form. \
                    Please check your information to be sure everything is correct.')
        else:
            cart = request.session.get('cart', {})
            if not cart:
                messages.error(request, "Your shopping cart is empty at this moment")
                return redirect(reverse('products'))

            current_cart = cart_contents(request)
            total = current_cart['grand_total']
            stripe_total = round(total * 100)
            stripe.api_key = stripe_secret_key
            intent = stripe.PaymentIntent.create(
                amount=stripe_total,
                currency=settings.STRIPE_CURRENCY,
            )

            if request.user.is_authenticated:
                try:
                    profile = UserProfile.objects.get(user=request.user)
                    order_form = OrderForm(initial={
                        'email': profile.user.email,
                        'company_name': profile.default_company_name,
                        'street_address1': profile.default_street_address1,
                        'street_address2': profile.default_street_address2,
                        'postcode': profile.default_postcode,
                        'town_or_city': profile.default_town_or_city,
                        'country': profile.default_country,
                        'phone_number': profile.default_phone_number,
                    })
                except UserProfile.DoesNotExist:
                    order_form = OrderForm()
            else:
                order_form = OrderForm()

        if not stripe_public_key:
            messages.warning(request, 'Stripe public key is missing. \
                Check if you have set it in your environment')

        template = 'checkout/checkout.html'
        context = {
            'order_form': order_form,
            'stripe_public_key': stripe_public_key,
            'client_secret': intent.client_secret,
        }

        return render(request, template, context)


def checkout_success(request, order_number):
    """ Handles successful checkouts """
    save_info = request.session.get('save_info')
    order = get_object_or_404(Order, order_number=order_number)

    if request.user.is_authenticated:
        profile = UserProfile.objects.get(user=request.user)
        # Attach the user's profile to the order
        order.user_profile = profile
        order.save()

    # Save the user's info
    if save_info:
        profile_data = {
            'default_company_name': order.company_name,
            'default_street_address1': order.street_address1,
            'default_street_address2': order.street_address2,
            'default_postcode': order.postcode,
            'default_town_or_city': order.town_or_city,
            'default_country': order.country,
            'default_phone_number': order.phone_number,
        }
        user_profile_form = UserProfileForm(profile_data, instance=profile)
        if user_profile_form.is_valid():
            user_profile_form.save()

    messages.success(request, f'Your order has been processed successfully. \
        Your order number is {order_number}. An order confirmation has \
        been sent to: {order.email}.')

    if 'cart' in request.session:
        del request.session['cart']

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
    }

    return render(request, template, context)