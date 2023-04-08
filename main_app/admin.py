from django.contrib import admin

# Register your models here.
from .models import Bird, Toy

admin.site.register([Bird, Toy])