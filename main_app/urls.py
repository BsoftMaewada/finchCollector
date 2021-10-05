from django.urls import path
from . import views

urlpatterns = [
    # path('route string', name of view function, name="string name of route"),
    # example
    #path('artists/', views.Artist_List.as_view(), name="artist_list"),
    #added the new path
    path('', views.Home.as_view(), name='home'),
]
