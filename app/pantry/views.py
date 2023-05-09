from django.shortcuts import render
from django.http import HttpResponse

from .models import *
from django.contrib.auth.models import User
from .forms import IngredientForm

def index(request):
        return render(request, "pantry/pantry.html", {})

def show(req):
        return HttpResponse(f'v')

def modify(req):
        return HttpResponse(f'W')

def add_ingredient(request):
        curr_user = request.user

        if not curr_user.is_authenticated:
                return render(request, "pantry/cosntruction.html", {})
        if request.method == 'POST':
                form = IngredientForm(request.POST)
                if form.is_valid():
                       name  = form.cleaned_data['name']
                       desc  = form.cleaned_data['description']
                       cate  = form.cleaned_data['category']
                       units = form.cleaned_data['units']
                       quant = form.cleaned_data['quantity']
                       new_ingredient = Ingredient(name=name, description=desc, category=cate, units=units)
                       new_ingredient.save()
                       curr_user = User.objects.get(pk=curr_user.id)
                       user_pantry = Pantry(user_id=curr_user, ingredient_id=new_ingredient, quantity=quant)
                       user_pantry.save() 
        else:
                form = IngredientForm()
        return render(request, "pantry/add_ingredient.html", {'form': form})