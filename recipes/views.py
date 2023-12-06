from django.http import HttpResponse
from django.shortcuts import render
from .models import Recipe, Product
from .utils import show_recipes_without_product, cook_recipe, add_product_to_recipe



def validate_request(request):

    if request := request.GET:
        print(request)
        return request

    return None


def show_recipes(request):

    """ /show_recipes/?product_id=1&exclude=1 """

    request_ = validate_request(request)

    result = show_recipes_without_product(*request_.values())

    data = {
        'title': 'Рецепты',
        'recipes': result
    }

    return render(request, "recipes/index.html", context=data)


def add_product(request):

    """ /add_product/?recipe_id=1&product_id=1&weight=500 """
    
    request_ = validate_request(request)

    result = add_product_to_recipe(*request_.values())

    data = {
        'title': 'Добавление продуктов',
        'result': result,
        
    }

    return render(request, "recipes/add_products.html", context=data)


def cook_products(request):
    
    """/cook_products/?recipe_id=5"""

    request_ = validate_request(request)

    result = cook_recipe(*request_.values())
    print(result)

    data = {
        'title': 'Приготовление продуктов',
        'products': result
    }

    return render(request, "recipes/cook_products.html", context=data)


def index(request):
    return HttpResponse("Hello")