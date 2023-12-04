from django.contrib import admin
from .models import Recipe, Product, RecipeDescription
# Register your models here.


class Description(admin.StackedInline):
    model = RecipeDescription


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    inlines = (Description, )
    list_display = ['id', 'name', 'get_products']
    list_display_links = ['name']

    @admin.display(description="Продукты")
    def get_products(self, instance):
        return [product for product in instance.description.select_related('product')]


@admin.register(RecipeDescription)
class RecipeDescriptionAdmin(admin.ModelAdmin):
    list_display = ['id', 'product', 'product_id', 'recipe', 'recipe_id','weight']
    list_display_links = ['recipe']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'quantity_cooked']
    list_display_links = ['name']
