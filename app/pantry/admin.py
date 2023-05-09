from django.contrib import admin

# Register your models here.
from .models import Pantry, Ingredient,Recipe

admin.site.register(Pantry)
admin.site.register(Ingredient)
admin.site.register(Recipe)
