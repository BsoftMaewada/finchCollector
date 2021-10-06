from django.shortcuts import render
from django.views import View #View class to handle requests
from django.views.generic.base import TemplateView
from django.http import HttpResponse #a class to handle sending a type of response  

# Create your views here.
class Home(TemplateView): # Defining the home view function
    # def get(self, request):
    #     return HttpResponse('home.html')
    template_name = 'home.html'

class About(TemplateView):  # Defining the about view function
    # def get (self, request):
    #     return HttpResponse('about.html')
    template_name = 'about.html'

def finches_views(request):
    return render(request, 'finches/finches.html', {'finches': finches})

class Finch:
    def __init__(self, name, breed, decription, age):
        self.name = name
        self.breed = breed
        self.decription = decription
        self.age = age
finches = [
   Finch('Zebra'), 
   Finch ('Gouldian'),
   Finch ('Society'),
   Finch ('Star'), 
   Finch ('Owl'), 
   Finch ('Strawberry'), 
   Finch ('Spice'), 
]
class Finches(TemplateView):  # Defining the finches view function
    template_name = 'finches.html'