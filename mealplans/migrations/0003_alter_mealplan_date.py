# Generated by Django 4.0.3 on 2022-06-09 00:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mealplans', '0002_rename_meal_plan_mealplan'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mealplan',
            name='date',
            field=models.DateField(auto_now=True),
        ),
    ]