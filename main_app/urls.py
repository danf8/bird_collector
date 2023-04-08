from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('about/', views.about),
    path('birds/', views.birds_index, name='birds_index'),
    path('birds/<int:bird_id>/', views.birds_detail, name='birds_detail'),
    path('birds/create/', views.BirdCreate.as_view(), name='bird_create'),
    path('bird/<int:pk>/update/', views.BirdUpdate.as_view(), name='bird_update'),
    path('bird/<int:pk>/delete', views.BirdDelete.as_view(), name='bird_delete' ),
    path('toys/', views.ToyList.as_view(), name='toys_index')
]
