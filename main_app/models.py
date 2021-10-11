from django.db import models
#import the reverse function
from django.urls import reverse

# Create your models here.
class Finch(models.Model):
    name = models.CharField(max_length=100)
    img = models.CharField(max_length=250, default=None)
    scientific_name = models.CharField(max_length=100)
    adult_size = models.TextField(max_length=10)
    lifespan = models.TextField(max_length=250)
    create_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
    # def filter_absolute_url(self):
    #     return reverse('detail', kwargs={'finch_id': self.id})
    class Meta:
            ordering = ['name']

