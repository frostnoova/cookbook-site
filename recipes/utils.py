from .models import Recipe, RecipeDescription
from django.db import IntegrityError


def add_product_to_recipe(recipe_id, product_id, weight):
    
    recipe_id, product_id, weight = map(int, (recipe_id, product_id, weight))

    try:
        product_object, status =  RecipeDescription.objects.select_related('recipe').select_related('product').update_or_create(recipe_id=recipe_id, 
                                                                                                                                product_id=product_id, 
                                                                                                                                defaults={"weight": weight})
    except IntegrityError:
        return "Такого рецепта нет!"

    if status:
        return f'Продукт {product_object.product.name} добавлен в рецепт'
    
    return f'Вес продукта "{product_object.product.name}" обновлен' 
    


def cook_recipe(recipe_id):

    products = RecipeDescription.objects.select_related('product').select_for_update().filter(recipe_id=recipe_id)
    


    return products

def show_recipes_without_product(product_id, exclude, weight=10):

    product_id, exclude = map(int, (product_id, exclude))

    print(f"{product_id = }, {exclude = }")
    if exclude:
        print("exclude")
        return Recipe.objects.prefetch_related('description').exclude(products__id=product_id, description__weight__lte=weight)

    return Recipe.objects.prefetch_related('description').filter(products__id=product_id, description__weight__lte=weight)

