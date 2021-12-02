from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('specifications/', views.specs, name='specs'),
    path('bleed/', views.bleed, name='bleed'),
    path('file_type/', views.file_type, name='file_type'),
    path('deep_black/', views.deep_black, name='deep_black'),
    path('ink_coverage/', views.ink_coverage, name='ink_coverage'),
    path('job_options/', views.job_options, name='job_options'),
    path('color/', views.color, name='color'),
    path('outlines/', views.outlines, name='outlines'),
    path('foil/', views.foil, name='foil'),
    path('overprint/', views.overprint, name='overprint'),
    path('resolution/', views.resolution, name='resolution'),
    path('templates/', views.templates, name='templates'),
    path('faq/', views.faq, name='faq'),
    path('team/', views.team, name='team'),
    path('printing_house/', views.printing_house, name='printing_house'),
    path('our_concept/', views.our_concept, name='our_concept'),
]
