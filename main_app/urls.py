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
    path('index/', views.Index.as_view(), name='index'),
    # path('index/<int:finches_id>/', views.finches_detail, name='detail'),
   
    path('index/create/', views.FinchCreate.as_view(), name='finch_form'),
    # Our new Route including the pk param
    path('index/<int:pk>/update', views.FinchUpdate.as_view(), name='finch_form'),
    path('index/<int:pk>/delete', views.FinchDelete.as_view(), name='finch_delete'),
    
    
]
