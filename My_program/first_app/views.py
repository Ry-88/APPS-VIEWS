from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

# Create your views here.

def home_page(request:HttpRequest):

    return HttpResponse("Hello World, This is my new HOME !")

def about_page(request:HttpRequest):
    
    return HttpResponse("This page out of service... Try Again Later")

