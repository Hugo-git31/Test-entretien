from django.contrib import admin
from django.urls import path
from django.views.generic import RedirectView
from countries import views

urlpatterns = [
    path('', RedirectView.as_view(url='countries/')), 
    path('admin/', admin.site.urls),
    path('countries/', views.country_list, name='country_list'),
    path('countries/<str:cca3>/', views.country_detail, name='country_detail'),
    path('stats/', views.country_stats, name='country_stats'),
]