from django import forms
from . import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class VehicleForm(forms.ModelForm):
    class Meta:
        model = models.VehicleModel
        fields = '__all__'

