from django.db import models
from django import forms
from django.contrib.auth.models import User

# Create your models here.


class AnimalProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    kind_of_animal = models.CharField(max_length=30)
    age = models.IntegerField()
    sex_of_animal = models.CharField(default = 'female', null= False, max_length=20)
    created= models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)