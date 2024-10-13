from django.shortcuts import render

# Create your views here.

def home1(request):
    return render(request, 'home1.html')

def secretary(request):
    return render(request, 'secretary.html')

def finance(request):
    return render(request, 'finance.html')

def president(request):
    return render(request, 'president.html')