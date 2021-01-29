from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name='home'),
    path('main_office/', views.main_datasets, name='main'),
    path('regional_office/', views.regional_datasets, name='regional'),
    path('field_office/', views.field_datasets, name='field'),
    path('county_data/', views.county_datasets, name='county'),
]
