from django.shortcuts import redirect, render, reverse, HttpResponse, get_object_or_404
from django.contrib import messages
from products.models import Product


def view_cart(request):
    """View that renders the shopping cart contents page"""

    return render(request, 'cart/cart.html')


def add_to_cart(request, product_id):
    """Add a product to the shopping cart"""

    product = get_object_or_404(Product, pk=product_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    if product_id in list(cart.keys()):
        cart[product_id] += quantity
    else:
        cart[product_id] = quantity
        messages.success(request, f'Successfully added {product.name} {product.size} {product.quantity} pieces to your cart')

    request.session['cart'] = cart
    return redirect(redirect_url)


def delete_from_cart(request, product_id):
    """Deleting a product from the shopping cart"""

    try:
        product = get_object_or_404(Product, pk=product_id)
        cart = request.session.get('cart', {})
        cart.pop(product_id)
        messages.success(
            request, f'{product.name} {product.size} {product.quantity} pieces was successfully removed from your cart')

        request.session['cart'] = cart
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(
            request, f'Error while deleting product {e}')
        return HttpResponse(status=500)