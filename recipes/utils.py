from django.db import IntegrityError
from django.db.models.expressions import F, Subquery
from django.db.models.query_utils import Q
from .models import Product, Recipe, RecipeDescription



def add_product_to_recipe(recipe_id, product_id, weight):

    recipe_id, product_id, weight = map(int, (recipe_id, product_id, weight))

    try:
        product_object, status =  RecipeDescription.objects.select_related('product').update_or_create(recipe_id=recipe_id, 
                                                                                                        product_id=product_id, 
                                                                                                        defaults={"weight": weight})
    except IntegrityError:
        return "Такого рецепта нет!"

    if status:
        return f'Продукт {product_object.product.name} добавлен в рецепт'
    
    return f'Вес продукта "{product_object.product.name}" обновлен' 


def cook_recipe(recipe_id, update_value=1):

    recipe_id = int(recipe_id)

    products_id = RecipeDescription.objects.select_related('product').filter(recipe_id=recipe_id).values_list('product_id', flat=True)

    return Product.objects.filter(id__in=products_id).update(quantity_cooked=F('quantity_cooked')+update_value)


def show_recipes_without_product(product_id, weight=10):

    product_id = int(product_id)
    
    products_id = Recipe.objects.prefetch_related('description').filter(Q(products__id=product_id) & Q(description__weight__gte=weight)).values_list('id', flat=True)

    return Recipe.objects.exclude(id__in = products_id).values('id', "name")