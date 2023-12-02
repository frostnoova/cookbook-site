from django.db import models


class Product(models.Model):

    name = models.CharField('Name Product', max_length=100, db_index=True)
    quantity_cooked = models.PositiveSmallIntegerField(default=0)

    class Meta:
        ordering = ('name', )

    def __str__(self):
        return f'{self.name}: quantity cooked {self.quantity_cooked}'


class Recipe(models.Model):

    name = models.CharField('Name Recipe', max_length=100, db_index=True)
    products = models.ManyToManyField(Product, through='RecipeDescription')

    def __str__(self):
        return f'{self.name}'


class RecipeDescription(models.Model):

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='description')
    weight = models.PositiveSmallIntegerField('Weight in grams')
    

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=('product', 'recipe'),
                name='unique_recipe_description')
        ]

    def __str__(self):
        return f'{self.recipe.name} ({self.product.name} {self.weight} grams)'
