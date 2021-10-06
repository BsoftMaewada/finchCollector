from django.urls import path
from . import views

urlpatterns = [
# path('route string', name of view function, name="string name of route"),
# example
#defining the home page
    path('', views.Home.as_view(), name='home'),
# Define route with a path of about/. 
# Name the route 'about'.
# Map the route to a view named views.about.
    path('about/', views.About.as_view(), name='about'),
    #rout for finch index
    path('finches/', views.Finches.as_view(), name='finches')
    
]
