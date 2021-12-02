from django.urls import path
from . import views

urlpatterns = [
    path('', views.contact, name='contact'),
    path('monstermap/', views.sample_kit, name='sample_kit'),
    path('offerte/', views.quotation, name='quotation'),
]
