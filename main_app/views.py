from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
# from django.http import HttpResponse
from .models import Bird, Toy, Photo
from .forms import FeedingForm
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

import uuid
import boto3

S3_BASE_URL = 'https://s3.us-east-2.amazonaws.com/'
BUCKET = 'birdcollector-0410'

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def birds_index(request):
    birds = Bird.objects.all()
    return render(request, 'birds/index.html', {'birds': birds})

def birds_detail(request, bird_id):
    bird = Bird.objects.get(id=bird_id)
    feeding_form = FeedingForm()
    bird_toy_ids = bird.toys.all().values_list('id')
    toys_bird_doesnt_have = Toy.objects.exclude(id__in=bird_toy_ids)
    return render(request, 'birds/detail.html', {'bird': bird, 'feeding_form': feeding_form, 'toys': toys_bird_doesnt_have})

def add_feeding(request, bird_id):
    form = FeedingForm(request.POST)
    if form.is_valid():
        new_feeding = form.save(commit=False)
        new_feeding.bird_id = bird_id
        new_feeding.save()
    return redirect('birds_detail', bird_id=bird_id)

def assoc_toy(request, bird_id, toy_id):
    bird = Bird.objects.get(id=bird_id)
    bird.toys.add(toy_id)
    return redirect('birds_detail', bird_id=bird_id)

def remove_assoc_toy(request, bird_id, toy_id):
    bird = Bird.objects.get(id=bird_id)
    bird.toys.remove(toy_id)
    return redirect('birds_detail', bird_id=bird_id)

def signup(request): 
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('birds_index')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form, 'error': error_message})

def add_photo(request, bird_id):
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        try:
            s3.upload_fileobj(photo_file, BUCKET, key)
            url = f"{S3_BASE_URL}{BUCKET}/{key}"
            Photo.objects.create(url=url, bird_id=bird_id)
        except Exception as error:
            print('photo upload failed')
            print(error)
    return redirect('birds_detail', bird_id=bird_id)


class BirdCreate(CreateView):
    model = Bird
    fields = ('name', 'breed', 'description', 'age')
    template_name = 'birds/bird_form.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
              
        
class BirdUpdate(UpdateView):
    model = Bird
    fields = ('description', 'age')
    template_name = 'birds/bird_form.html'

class BirdDelete(DeleteView):
    model = Bird
    success_url = '/birds/'
    template_name = 'birds/bird_confirm_delete.html'

class ToyList(ListView):
    model = Toy
    template_name = 'toys/toy_list.html'

class ToyDetail(DetailView):
    model = Toy
    template_name = 'toys/toy_detail.html'

class ToyCreate(CreateView):
    model = Toy
    fields = '__all__'
    template_name = 'toys/toy_form.html'

class ToyUpdate(UpdateView):
    model = Toy
    fields = '__all__'
    template_name = 'toys/toy_form.html'

class ToyDelete(DeleteView):
    model = Toy
    success_url = '/toys/'
    template_name = 'toys/toy_confirm_delete.html'