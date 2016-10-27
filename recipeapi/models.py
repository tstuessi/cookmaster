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
    date_created = models.DateTimeField(auto_now_add=True)
    last_edited = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

# the ingredient has a many to one relationship to Recipe
class Ingredient(models.Model):
    name = models.CharField(max_length=200)
    numerator = models.IntegerField()
    denom = models.IntegerField()
    unit = models.CharField(max_length=200)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)

    def __str__(self):
        val = ""
        if self.numerator % self.denom == 0:
            val = str(self.numerator % self.denom)
        else:
            val = "{}/{}".format(self.numerator, self.denom)
        return "{} {} of {}".format(val, self.unit, self.name)

class Step(models.Model):
    number = models.IntegerField()
    text = models.TextField()
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)

