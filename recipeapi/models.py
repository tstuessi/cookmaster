from django.db import models

# Create your models here.

# Recipe Spec Layout:
# Recipe: {
#   name: String,
#   date_created: DateTime,
#   last_edited: DateTime,
#   ingredients: [
#       {
#           name: String,
#           numerator: Number
#           denom: Number
#           unit: String,
#       }
#   ],
#   steps: [
#       {
#           number: Number
#           text: String
#       }
#   ],
#}
class Recipe(models.Model):
    name = models.CharField(max_length=200)
    recipe_yield = models.CharField(max_length=200)
    cooking_time = models.CharField(max_length=200)
    date_created = models.DateTimeField(auto_now_add=True)
    last_edited = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

# the ingredient has a many to one relationship to Recipe
class Ingredient(models.Model):
    name = models.CharField(max_length=200)
    amount = models.CharField(max_length=200)
    unit = models.CharField(max_length=200)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)

    def __str__(self):
        if self.unit != "":
            adj = " of "
        else:
            adj = " "
        return ("{} {}{}{}".format(self.amount, self.unit, adj,  self.name)).strip()

class Step(models.Model):
    number = models.IntegerField()
    text = models.TextField()
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)

    def __str__(self):
        return "{}. {}".format(self.number, self.text)
