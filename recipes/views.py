from django.shortcuts import render


def home(request):

    data = {
        'title': 'Рецепты',

    }

    return render(request, "recipes/index.html", context=data)


def products(request):

    data = {
        'title': 'Продукты',

    }

    return render(request, "recipes/products.html", context=data)