from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='app2_home'),
    path('technology/', views.technology, name='app2_technology'),
    path('business/', views.business, name='app2_business'),
]