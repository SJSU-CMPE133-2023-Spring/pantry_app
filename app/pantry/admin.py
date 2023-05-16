from django.contrib import admin

# Register your models here.
from .models import Pantry, Ingredient,Recipe, pantry_item, Category

admin.site.register(Pantry)
admin.site.register(Ingredient)
admin.site.register(Recipe)

admin.site.register(pantry_item)
admin.site.register(Category)
