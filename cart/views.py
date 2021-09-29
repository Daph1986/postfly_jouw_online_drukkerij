from django.shortcuts import redirect, render


def view_cart(request):
    """View that renders the shopping cart contents page"""

    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    """Add a product to the shopping bag"""

    quantity = None
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    if item_id in list(cart.keys()):
        cart[item_id] += quantity
    else:
        cart[item_id] = quantity

    request.session['cart'] = cart
    print(request.session['cart'])
    return redirect(redirect_url)
