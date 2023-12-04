# cookbook-site


```
python -m venv env

source env/bin/activate

pip install -r requirements.txt

python manage.py runserver
```

- admin root
- password root


### Таблица рецептов включая заданные параметры или не включая

```
http://127.0.0.1:8000/show_recipes/?product_id=1&exclude=1
```

### Добавление продукта или обновление веса
```
http://127.0.0.1:8000/add_product/?recipe_id=1&product_id=1&weight=500 
```

### Приготовление рецепта
```
http://127.0.0.1:8000/cook_products/?recipe_id=5
```

- product_id id : int
- recipe_id : int
- exclude : 1 or 0 
- weight: int
