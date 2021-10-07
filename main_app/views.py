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
    def __init__(self, name, scientific_name, adult_size, lifespan):
        self.name = name
        self.scientific_name = scientific_name
        self.adult_size = adult_size
        self.lifespan = lifespan
finches = [
   Finch('Zebra', 'Poephla guttata', '4 inches','3 to 15 years'), 
   Finch ('Gouldian','Erythrura gouldiae', '5 to 6 inches', '6 to 8 years'),
   Finch ('Society', 'Lonchura domestica','4-5 inches, 0.6-0.7 grams',' 4-7 years'),
   Finch ('Star','Neochmia Ruficauda','5-6 inches','4 to 8 years'), 
   Finch ('Owl','Taeniopygia bichenovii',' 3 to 4 inches long. About 15 to 17 grams (half an ounce)','p to 10 years'), 
   Finch ('Strawberry','Amandava amandava','3-4 inches','7-10 years'), 
   Finch ('Spice','Lonchura punctulata','6 inches','6 to 8 years'), 
]
class Finches(TemplateView):  # Defining the finches view function
    template_name = 'finches.html'