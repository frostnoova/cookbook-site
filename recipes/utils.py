from .models import Recipe, Product, RecipeDescription


def add_product_to_recipe(parameters):
    pass


def cook_recipe(parameters):
    pass

def show_recipes_without_product(_, product_id, exclude, weight=10):
    
    product_id = int(product_id[0])
    exclude = bool(exclude[0])
    
    print(f"{product_id = }, {exclude = }")
    if exclude:
        return Recipe.objects.prefetch_related('description').exclude(products__id=product_id, description__weight__lte=weight)

    return Recipe.objects.prefetch_related('description').filter(products__id=product_id, description__weight__lte=weight)



