from django.shortcuts import render
from django.views import View #View class to handle requests
from django.http import HttpResponse #a class to handle sending a type of response  

# Create your views here.
class Home(View):
    def get(self, request):
        return HttpResponse('finchCollector Home')
