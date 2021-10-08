from django.db import models

# Create your models here.

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
