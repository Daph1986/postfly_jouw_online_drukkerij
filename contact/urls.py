from django.urls import path
from . import views

urlpatterns = [
    path('', views.contact, name='contact'),
    path('sample_kit/', views.sample_kit, name='sample_kit'),
    path('quotation/', views.quotation, name='quotation'),
]
