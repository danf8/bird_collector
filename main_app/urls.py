from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('about/', views.about),
    path('birds/', views.birds_index, name='birds_index'),
]
