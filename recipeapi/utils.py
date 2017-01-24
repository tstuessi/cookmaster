# This file will handle parsing recipe ingredients
import ingredient_parser.ingredient_parser.en as ip

from .models import Ingredient, Step

def process_ingredient(i, recipe):
    # parse the ingredient
    temp = ip.parse(i, expanded=True)

    # parse the quantity
    amt = temp["quantity"]

    unit = temp["unit"]
    name = temp["name"]

    return Ingredient(name=name, amount=amt, unit=unit, recipe=recipe)


def process_step(step, recipe, number):
    step_words = step.split(" ")

    # check if first is numbered
    try:
        float(step_words[0])
        del step_words[0]
    except ValueError:
        pass

    text = " ".join(step_words)
    return Step(number=number, text=text, recipe=recipe)
