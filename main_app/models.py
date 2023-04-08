from django.db import models
from django.urls import reverse

# Create your models here.

class Toy(models.Model):
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=20)

    def get_absolute_url(self):
        return reverse('toys_detail', kwargs={'pk': self.id})
    
    def __str__(self):
        return self.name

class Bird(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    age = models.IntegerField(default=0)

    def get_absolute_url(self):
        return reverse('birds_detail', kwargs={'bird_id': self.id})

    def __str__(self):
        return self.name



