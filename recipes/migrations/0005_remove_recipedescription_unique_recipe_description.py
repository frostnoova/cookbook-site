# Generated by Django 4.2.7 on 2023-12-03 09:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0004_alter_recipedescription_options_alter_product_name_and_more'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='recipedescription',
            name='unique_recipe_description',
        ),
    ]