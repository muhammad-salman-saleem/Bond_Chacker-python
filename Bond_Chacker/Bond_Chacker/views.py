#  I was created this file
from django.http import HttpResponse
from django.shortcuts import render



def home(request):
    return render(request,'home.html')
    # return HttpResponse("Home Salman Saleem")

def product(request):
    return render(request,'product.html')

def about(request):
    return render(request,'about_us.html')

def contacts(request):
    return render(request,'contect_us.html')

def login(request):
    return render(request,'login_form.html')