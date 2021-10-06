from django.urls import path
from . import views

urlpatterns = [
    # path('route string', name of view function, name="string name of route"),
    # example
   
    #defining the home page
    path('', views.Home.as_view(), name='home'),
    path('about/', views.About.as_view(), name='about'),
    
]
