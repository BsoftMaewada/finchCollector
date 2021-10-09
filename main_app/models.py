from django.db import models
#import the reverse function
from django.urls import reverse

# Create your models here.
class Finch(models.Model):
    name = models.CharField(max_length=100)
    scientific_name = models.CharField(max_length=100)
    adult_size = models.IntegerField()
    lifespan = models.TextField(max_length=250)
    create_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'finch_id': self.id})

