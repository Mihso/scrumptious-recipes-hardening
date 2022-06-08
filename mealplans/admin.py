from django.contrib import admin

from mealplans.models import Mealplan

# Register your models here.
class MealPlanAdmin(admin.ModelAdmin):
    pass


admin.site.register(Mealplan, MealPlanAdmin)
