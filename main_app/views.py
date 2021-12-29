from django.shortcuts import render
from django.views import View #View class to handle requests
from django.views.generic.base import TemplateView
from django.http import HttpResponse #a class to handle sending a type of response  
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from .models import Finch

from django.urls import reverse


# Create your views here.
class Home(TemplateView): # Defining the home view function
    # def get(self, request):
    #     return HttpResponse('home.html')
    template_name = 'home.html'

class About(TemplateView):  # Defining the about view function
    # def get (self, request):
    #     return HttpResponse('about.html')
    template_name = 'about.html'

# def finches_index(request):
#         return render(request, '/index.html', {'finches': finches_index } )

# class Finchs(TemplateView):  # Defining the finches view function
#     template_name = 'index.html'
    
# class Finch():
#     def __init__(self, name, img, scientific_name, adult_size, lifespan):
#         self.name = name
#         self.image = img
#         self.scientific_name = scientific_name
#         self.adult_size = adult_size
#         self.lifespan = lifespan
        
        
# finchs = [
#    Finch ('Zebra','https://www.thespruce.com/thmb/zfkyfYJP-hgOcr-M0ddH7oChjCk=/1000x1000/smart/filters:no_upscale()/zebra-finch-male-f8dec4180a224389ae226e6a621d4fbd.jpg','Poephla guttata', '4 inches','3-15 years'), 
#    Finch ('Gouldian',' https://upload.wikimedia.org/wikipedia/commons/3/3e/Male_adult_Gouldian_Finch.jpg','Erythrura gouldiae', '5-6 inches', '6-8 years'),
#    Finch ('Society',' https://cdn.pixabay.com/photo/2016/05/17/20/44/bullfinch-1399055_960_720.jpg', 'Lonchura domestica','4-5 inches',' 4-7 years'),
#    Finch ('Star',' https://i1.sndcdn.com/artworks-000004630272-yp1ehy-t500x500.jpg','Neochmia Ruficauda','5-6 inches','4-8 years'), 
#    Finch ('Owl','https://www.thesprucepets.com/thmb/gFc-hUYEG4AL6qFK4IqbEzDavYA=/2118x2118/smart/filters:no_upscale()/GettyImages-691285968-cf3b79a20ba44bb6857ffca7053227b9.jpg ','Taeniopygia bichenovii',' 3-4 inches ','up to 10 years'), 
#    Finch ('Strawberry','https://www.cheapmacawsonline.com/wp-content/uploads/2020/03/Buy-Strawberry-finches-for-sale.jpg ','Amandava amandava','3-4 inches','7-10 years'), 
#    Finch ('Spice','https://www.fredmiranda.com/forum/ufiles/68/1005068.jpg','Lonchura punctulata','6 inches','6-8 years'), 
# ]

class Index(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        print(Finch)
        context = super().get_context_data(**kwargs)
        context["finchs"] = Finch.objects.all()
        return context
    
# class FinchDetail(DetailView):
#     model = Finch
#     template_name = "finch_detail.html"

class FinchCreate(CreateView):
    model = Finch
    fields = ['name','img']
    template_name = "finch_form.html"
    success_url = "/finch_detail/"
     # this will get the pk from the route and redirect to artist view
    # def get_success_url(self):
    #     return reverse('index', kwargs={'pk': self.object.pk})

class FinchUpdate(UpdateView):
    model = Finch
    fields = ['scientific_name', 'adult_size', 'lifespan',]
    template_name = "finch_form.html"
    success_url = "/finch_detail/"
    # def get_success_url(self):
    #     return reverse('/index/', kwargs={'pk': self.object.pk})
    
class FinchDelete(DeleteView):
    # model = Finch
    # # fields = ['name','img', 'scientific_name', 'adult_size', 'lifespan',]
    # template_name = "finch_delete.html"
    # success_url = "/finch_detail/"
    
   

    model = Finch
    fields = ['name','img', 'scientific_name', 'adult_size', 'lifespan',]
    template_name = "finch_detail.html"
    success_url = "/finch_detail/"

class FinchDetail(DetailView):
    model = Finch
    template_name = "finch_detail.html"
