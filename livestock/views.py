from django.shortcuts import render
from django.views.generic.list import ListView
from .models import AnimalProfile
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

# Create your views here.

class FarmersAnimals(ListView):
    model = AnimalProfile
    context_object_name = 'animals'


class CreateAnimalProfile(CreateView):
    model = AnimalProfile
    fields = '__all__'
    success_url = reverse_lazy('animal-profile')
