from django.urls import path
from . import views
from .views import CheckoutView

urlpatterns = [
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('checkout_success/<order_number>', views.checkout_success, name='checkout_success'),
    path('cache_checkout_data/', views.cache_checkout_data, name='cache_checkout_data'),
]