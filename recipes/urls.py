from django.urls import path
from recipes import views

urlpatterns = [
    path("add_product/", views.add_product, name='add_product'),
    path("show_recipes/", views.show_recipes, name='show_recipes'),
    path("cook_products/", views.cook_products, name='cook_products'),
    path("", views.index, name='index')
]