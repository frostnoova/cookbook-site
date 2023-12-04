from .models import Recipe, RecipeDescription
from django.core.exceptions import ObjectDoesNotExist
from django.db import transaction


def add_product_to_recipe(recipe_id, product_id, weight):
    
    recipe_id, product_id, weight = map(int, (recipe_id, product_id, weight))
    print(f"{recipe_id = }, {product_id = }, {weight = }")

    try:
        Recipe.objects.get(id=recipe_id)

    except ObjectDoesNotExist:
        return 'Такого рецепта нет!'

    filter_ = RecipeDescription.objects.select_related('product').select_for_update().filter(recipe_id=recipe_id, product_id=product_id)
    print(filter_)
    if len(filter_):

        name = filter_[0].product.name
        filter_.update(recipe_id=recipe_id,product_id=product_id, weight=weight)
        return f'Вес продукта "{name}" обновлен'
    
    filter_.create(recipe_id=recipe_id, product_id=product_id, weight=weight)
    
    return 'Продукт добавлен в рецепт'


def cook_recipe(recipe_id):

    products = RecipeDescription.objects.select_related('product').select_for_update().filter(recipe_id=recipe_id)
    
    with transaction.atomic():
        for model in products.iterator():
            model.product.quantity_cooked += 1
            model.product.save()

    return products

def show_recipes_without_product(product_id, exclude, weight=10):

    product_id, exclude = map(int, (product_id, exclude))

    print(f"{product_id = }, {exclude = }")
    if exclude:
        print("exclude")
        return Recipe.objects.prefetch_related('description').exclude(products__id=product_id, description__weight__lte=weight)

    return Recipe.objects.prefetch_related('description').filter(products__id=product_id, description__weight__lte=weight)

