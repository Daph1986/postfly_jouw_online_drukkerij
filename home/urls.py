from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('aanleveren/', views.specs, name='specs'),
    path('bleed/', views.bleed, name='bleed'),
]