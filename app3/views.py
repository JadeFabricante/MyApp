from django.shortcuts import render

def home(request):
    return render(request, 'app3/home.html')

def services(request):
    return render(request, 'app3/services.html')

def about(request):
    return render(request, 'app3/about.html')