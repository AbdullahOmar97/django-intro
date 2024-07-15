from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html')

def page2(request):
    return render(request, 'page2.htm')

def page3(request):
    return render(request, 'page3.html')