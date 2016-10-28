from django.shortcuts import render
from .models import Recipe, Ingredient, Step

from django.views.decorators import csrf_exempt

import re

from django.http import HttpResponse, JsonResponse

# Create your views here.

#def get_recipe(request, recipe):
#    recipe_name = re.sub('\-+', ' ', recipe)
#    recipe_dict = dict()
#    return HttpResponse(recipe_name)

@csrf_exempt
def index(request):
    print("this was called!")
    return JsonResponse({"info":"Okay"})
