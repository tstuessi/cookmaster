from django.shortcuts import render, get_object_or_404
from .models import Recipe, Ingredient, Step

from django.http import HttpResponse, JsonResponse

from .utils import process_ingredient, process_step

# Create your views here.

#def get_recipe(request, recipe):
#    recipe_name = re.sub('\-+', ' ', recipe)
#    recipe_dict = dict()
#    return HttpResponse(recipe_name)

def index(request):
    context = dict()

    # get all the current available recipes
    recipes = Recipe.objects.all()
    context["recipe_list"] = [r for r in recipes]
    return render(request, "recipeapi/index.html", context)

def recipe(request, recipe_id):
    context = dict()
    
    rec_obj = get_object_or_404(Recipe, pk=recipe_id)

    context["recipe"] = rec_obj
    context["ingredients"] = [x for x in Ingredient.objects.filter(recipe=rec_obj)]
    context["steps"] = Step.objects.filter(recipe=rec_obj).order_by('number')

    return render(request, "recipeapi/recipe.html", context)

def new_recipe(request):
    if request.method == "POST":
        # Create the new recipe
        recipe = Recipe(name=request.POST["recipename"], recipe_yield=request.POST["recipeyield"], cooking_time=request.POST["cookingtime"])

        recipe.save()

        # split the ingredients and process them
        ingredients = request.POST["ingredients"]
        temp_list = [x for x in ingredients.split('\n') if x != ""]
        ingredient_list = []
        for i in temp_list:
            ingredient = process_ingredient(i, recipe)
            ingredient_list.append(ingredient)

        # save them all at once so I can parse them quickly
        for i in ingredient_list:
            i.save()

        # split up the steps and save them
        steps = request.POST["steps"]
        temp_list = [x for x in steps.split('\n') if x != ""]
        i = 1
        step_list = []
        for step in temp_list:
            step_list.append(process_step(step, recipe, i))
            i += 1

        for step in step_list:
            step.save()
        return render(request, "recipeapi/newrecipe.html", {"saved": True})

    else:
        # render the form page
        context = None
        return render(request, "recipeapi/newrecipe.html", context)
