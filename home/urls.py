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
    path('cold_foil/', views.foil, name='foil'),
    path('overprint/', views.overprint, name='overprint'),
    path('resolutie/', views.resolution, name='resolution'),
    path('templates/', views.templates, name='templates'),
    path('faq/', views.faq, name='faq'),
    path('team/', views.team, name='team'),
    path('eigen_drukkerij/', views.printing_house, name='printing_house'),
    path('ons_concept/', views.our_concept, name='our_concept'),
    path('contact/', views.contact, name='contact'),
    path('monstermap/', views.sample_kit, name='sample_kit'),
    path('offerte/', views.quotation, name='quotation'),
]