from django.db import models



"""
To apply any changes in here:
 1. python manage.py makemigrations
 2. python manage.py migrate 
"""
class User(models.Model):
    username   = models.CharField(max_length=100)
    email      = models.CharField(max_length=200)
    password   = models.CharField(max_length=150)


class Ingredient(models.Model):
    name        = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    category    = models.CharField(max_length=50)
    units       = models.CharField(max_length=50)

    def __str__(self):
        return f'''\
name: {self.name}
description: {self.description}
category: {self.category}'''

class Pantry(models.Model):
    user_id       = models.ForeignKey(User, on_delete=models.CASCADE)
    ingredient_id = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity      = models.IntegerField(default=0)
    

class Recipe(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title

class RecipeIngredients(models.Model):
    recipe     = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingreidnet = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity   = models.CharField(max_length=50)


# TODO proper implementation of user model 
