from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='app1_home'),
    path('about/', views.about, name='app1_about'),
    path('contact/', views.contact, name='app1_contact'),
]