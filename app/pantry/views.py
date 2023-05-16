from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import logout

from .models import *
from django.contrib.auth.models import User
from .forms import IngredientForm, PantryItemForm

def index(request):
        return render(request, "pantry/pantry.html", {})

def show(req):
        return HttpResponse(f'v')

def modify(req):
        return HttpResponse(f'W')

def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('')

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
                       return redirect("/pantry/") 
        else:
                form = IngredientForm()
        return render(request, "pantry/add_ingredient.html", {'form': form})


def myPantry(request):
    items = pantry_item.objects.all()
    context = {'pantry_items': items}

    return render(request, 'mypantry.html', context)

def addItem(request):
    form = PantryItemForm()

    if request.method == "POST":
        form = PantryItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('my-pantry')
        
    context = {'form': form}
    return render(request, 'item_form.html', context)

def deleteItem(request, pk):
    item = pantry_item.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('my-pantry')
    return render(request, 'delete.html', {'obj':item})

def editItem(request, pk):
    item = pantry_item.objects.get(id=pk)
    form = PantryItemForm(instance=item)

    if request.method == "POST":
        form = PantryItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('my-pantry')

    context = {'form': form}
    return render(request, 'item_form.html', context)
