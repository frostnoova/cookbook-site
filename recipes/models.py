from django.db import models


class Product(models.Model):

    name = models.CharField('Название продукта', max_length=100, db_index=True)
    quantity_cooked = models.PositiveSmallIntegerField('Приготовлено блюд',default=0)

    class Meta:
        ordering = ('name', )

    def __str__(self):
        return f'{self.name}'


class Recipe(models.Model):

    name = models.CharField('Название рецепта', max_length=100, db_index=True, unique=True)
    products = models.ManyToManyField(Product, through='RecipeDescription')

    def __str__(self):
        return f'{self.name}'


class RecipeDescription(models.Model):

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='description')
    weight = models.PositiveSmallIntegerField('Вес в граммах')
    

    class Meta:
        # constraints = [
        #     models.UniqueConstraint(
        #         fields=('product', 'recipe'),
        #         name='unique_recipe_description')
        # ]

        ordering = ('recipe_id', )

    def __str__(self):
        return f'{self.product.name} {self.weight} г'
