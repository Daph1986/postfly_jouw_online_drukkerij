from django.shortcuts import render


def view_cart(request):
    """View that renders the shopping cart contents page"""

    return render(request, 'cart/cart.html')