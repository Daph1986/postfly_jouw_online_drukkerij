from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('user_profile', views.profile, name='profile'),
    path('order_detail/<order_number>',
         views.order_detail, name='order_detail'),
]
