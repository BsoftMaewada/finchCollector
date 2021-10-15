from django.contrib import admin
#import the Finch Model from manage.py
from .models import  Finch 

# Register your models here.
admin.site.register(Finch) #this will add the model to the admin

