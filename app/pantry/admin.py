from django.contrib import admin

# Register your models here.
from .models import Pantry, Ingredient

admin.site.register(Pantry)
admin.site.register(Ingredient)