# Generated by Django 4.2.7 on 2023-12-03 13:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0006_alter_recipedescription_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipedescription',
            name='recipe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='description', to='recipes.recipe'),
        ),
    ]