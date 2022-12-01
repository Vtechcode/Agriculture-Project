from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.FarmersAnimals.as_view(), name='animal-profile'),
    path('create', views.CreateAnimalProfile.as_view(), name='create-profile'),
]