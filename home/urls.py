from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('aanleveren/', views.specs, name='specs'),
    path('bleed/', views.bleed, name='bleed'),
    path('bestandstype/', views.file_type, name='file_type'),
    path('diep_zwart/', views.deep_black, name='deep_black'),
    path('inktbezetting/', views.ink_coverage, name='ink_coverage'),
    path('joboptions/', views.job_options, name='job_options'),
    path('kleur/', views.color, name='color'),
    path('lettercontouren/', views.outlines, name='outlines'),
]