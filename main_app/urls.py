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
    path('birds/<int:bird_id>/add_feeding', views.add_feeding, name='add_feeding'),
    path('birds/<int:bird_id>/assoc_toy/<int:toy_id>/', views.assoc_toy, name='assoc_toy'),
    path('birds/<int:bird_id>/remove_assoc_toy/<int:toy_id>/', views.remove_assoc_toy, name='remove_assoc_toy'),
    path('toys/', views.ToyList.as_view(), name='toys_index'),
    path('toys/<int:pk>/', views.ToyDetail.as_view(), name='toy_detail'),
    path('toys/create/', views.ToyCreate.as_view(), name='toy_create'),
    path('toy/<int:pk>/update', views.ToyUpdate.as_view(), name='toy_update'),
    path('toy/<int:pk>/delete', views.ToyDelete.as_view(), name='toy_delete'),
    path('accounts/signup', views.signup, name='signup'),
    path('birds/<int:bird_id>/add_photo', views.add_photo, name='add_photo'),
]
