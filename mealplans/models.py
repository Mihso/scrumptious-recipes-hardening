from email.charset import add_charset, add_codec
from msilib import add_data
import datetime
from django.db import models

from django.conf import settings

USER_MODEL = settings.AUTH_USER_MODEL
# Create your models here.


class Mealplan(models.Model):
    name = models.CharField(max_length=120)
    owner = models.ForeignKey(
        USER_MODEL,
        on_delete=models.CASCADE,
    )
    date = models.DateField()
    recipes = models.ManyToManyField("recipes.Recipe", related_name="recipes")
