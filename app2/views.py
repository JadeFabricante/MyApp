from django.shortcuts import render

def home(request):
    return render(request, 'app2/home.html')

def technology(request):
    return render(request, 'app2/technology.html')

def business(request):
    return render(request, 'app2/business.html')