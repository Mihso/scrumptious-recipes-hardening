from django import template

register = template.Library()


def resize_to(ingredients, arg):
    print("value:", ingredients)
    print("arg:", arg)

    serve = ingredients.recipe.servings
    if serve != None and arg != None:
        try:
            ratio = int(arg) / serve
            return ingredients.amount * ratio
        except:
            pass
    return ingredients.amount


register.filter(resize_to)
