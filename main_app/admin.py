from django.contrib import admin

# Register your models here.
from .models import Bird, Toy, Feeding

admin.site.register([Bird, Toy, Feeding])