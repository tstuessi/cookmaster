from django.shortcuts import render
from .models import Recipe, Ingredient, Step

import re

from django.http import HttpResponse

# Create your views here.

#def get_recipe(request, recipe):
#    recipe_name = re.sub('\-+', ' ', recipe)
#    recipe_dict = dict()
#    return HttpResponse(recipe_name)
    
def index(request):
    print("this was called!")
    return HttpResponse("Okay")
