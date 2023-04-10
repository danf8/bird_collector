from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.

class Toy(models.Model):
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=20)

    def get_absolute_url(self):
        return reverse('toy_detail', kwargs={'pk': self.id})
    
    def __str__(self):
        return self.name

class Bird(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    age = models.IntegerField(default=0)
    toys = models.ManyToManyField(Toy)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('birds_detail', kwargs={'bird_id': self.id})

    def __str__(self):
        return self.name

class Feeding(models.Model):
    MEALS = (
        ('B', 'Breakfast'),
        ('L', 'Lunch'),
        ('D', 'Dinner'),
    )
    date = models.DateField('feeding date')
    meal = models.CharField(max_length=1, choices=MEALS, default=MEALS[0][0], verbose_name='meal type')
    bird = models.ForeignKey(Bird, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_meal_display()} on {self.date}"
    
    class Meta:
        ordering = '-date',
    
class Photo(models.Model):
    url = models.CharField(max_length=225)
    bird = models.ForeignKey(Bird, on_delete=models.CASCADE)

    def __STR__(self):
        return f"Photo for bird_id: {self.bird_id} @{self.url}"



