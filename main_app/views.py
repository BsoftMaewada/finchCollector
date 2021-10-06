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