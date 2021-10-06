from django.shortcuts import render
from django.views import View #View class to handle requests
from django.http import HttpResponse #a class to handle sending a type of response  

# Create your views here.
class Home(View): # Defining the home view function
    def get(self, request):
        return HttpResponse('<h1> Home Page </h1>')

class About(View):  # Defining the about view function
    def get (self, request):
        return HttpResponse('<h1> About the finchCollector </h1>')