from django.db import models

# Create your models here.
#dummy user (not actual)
class User(models.Model):
    username   = models.CharField(max_length=100)
    email      = models.CharField(max_length=200)
    password   = models.CharField(max_length=150)


class Ingredient(models.Model):
    name        = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    category    = models.CharField(max_length=50)

    def __str__(self):
        return f'''\
name: {self.name}
description: {self.description}
category: {self.category}'''

class Pantry(models.Model):
    user_id       = models.ForeignKey(User, on_delete=models.CASCADE)
    ingredient_id = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    


# TODO proper implementation of user model 
