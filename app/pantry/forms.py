from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import pantry_item
from django.forms import ModelForm


class IngredientForm(forms.Form):
    name = forms.CharField(label="ingredient name", max_length=200)
    description = forms.CharField(label="description", max_length=500)
    category    = forms.CharField(label="category", max_length=50)
    units       = forms.CharField(label="unit measurement", max_length=50)
    quantity    = forms.IntegerField(label="quanity")

class PantryItemForm(ModelForm):
    class Meta:
        model = pantry_item
        fields = '__all__'