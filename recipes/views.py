from django.shortcuts import render
from .models import Recipe, Product
from .utils import show_recipes_without_product, cook_recipe, add_product_to_recipe


functions_ = {'show_recipes': show_recipes_without_product,
              'cook_recipe': cook_recipe,
              'add_product': add_product_to_recipe}

bools_ = {'true':True,
          'false': False}

def recipes(request):
   
    if func := request.GET.get('func'):
        print(request.GET)
        recipes_ = functions_[func](*request.GET.values())
    else:
        recipes_ = None

    print(recipes_)

    data = {
        'title': 'Рецепты',
        'recipes': recipes_
    }

    return render(request, "recipes/index.html", context=data)


def products(request):
    
    products_ = Product.objects.all()

    data = {
        'title': 'Продукты',
        'products': products_
    }

    return render(request, "recipes/products.html", context=data)