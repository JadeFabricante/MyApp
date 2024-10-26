from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='app3-home'),
    path('services/', views.services, name='app3-services'),
    path('about/', views.about, name='app3-about'),
]